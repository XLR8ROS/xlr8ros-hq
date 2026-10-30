"""Offline regression tests for one-way, auto-updated XOS YAML mirrors."""
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "sync_canon_mirrors.py"
spec = importlib.util.spec_from_file_location("xos_canon_sync", SOURCE)
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class CanonMirrorTests(unittest.TestCase):
    def test_hq_literal_no_generated_header(self):
        yaml_text = (
            "status: authoritative\n"
            "source_of_truth: true\n"
            "render:\n  mode: literal\n  markdown_path: Constitution.md\n"
            "content: |\n  # Constitution\n  The source is authority.\n"
        )
        value = sync.rendered_content(
            sync.HQ, "canon/constitution.yaml", yaml_text,
            "Constitution.md", "none"
        )
        self.assertEqual(value, b"# Constitution\nThe source is authority.\n")

    def test_sead_generated_comment_matches_upstream_contract(self):
        yaml_text = (
            "status: authoritative\n"
            "source_of_truth: true\n"
            "render:\n  mode: literal\n  markdown_path: Division SOP 4 XOS SEAD.md\n"
            "content: |\n  # SEAD SOP\n  Verbatim content.\n"
        )
        content = sync.rendered_content(
            "XLR8ROS/XLR8ROS_SEAD",
            "canon/sead-division-sop.yaml", yaml_text,
            "Division SOP 4 XOS SEAD.md", "sead-generated"
        )
        self.assertEqual(
            content,
            b"<!-- Generated readable copy. Authoritative YAML: "
            b"XLR8ROS/XLR8ROS_SEAD/canon/sead-division-sop.yaml. "
            b"Do not edit independently. -->\n\n"
            b"# SEAD SOP\nVerbatim content.\n"
        )

    def test_mismatched_authority_refused(self):
        yaml_text = (
            "source_of_truth: false\n"
            "render:\n  mode: literal\n  markdown_path: Document.md\n"
            "content: |\n  Wrong\n"
        )
        with self.assertRaises(ValueError):
            sync.rendered_content(sync.HQ, "canon/document.yaml", yaml_text,
                                  "Document.md", "none")

    def test_exact_match_is_idempotent(self):
        with patch.object(sync, "remote_bytes", return_value=(b"expected", "sha-1")):
            with patch.object(sync, "github_api") as api:
                self.assertEqual(sync.ensure("owner/repo", "file.md", b"expected", False),
                                 "match")
                api.assert_not_called()

    def test_drift_in_check_mode_never_writes(self):
        with patch.object(sync, "remote_bytes", return_value=(b"old", "sha-1")):
            with patch.object(sync, "github_api") as api:
                self.assertEqual(sync.ensure("owner/repo", "file.md", b"new", True),
                                 "drift")
                api.assert_not_called()

    def test_update_is_followed_by_exact_readback(self):
        states = [(b"stale", "sha-old"), (b"desired", "sha-new")]
        with patch.object(sync, "remote_bytes", side_effect=states):
            with patch.object(sync, "github_api") as api:
                self.assertEqual(sync.ensure("owner/repo", "canon.md", b"desired", False),
                                 "verified")
                args, kwargs = api.call_args
                self.assertEqual(kwargs["method"], "PUT")
                self.assertEqual(kwargs["payload"]["sha"], "sha-old")
                self.assertEqual(kwargs["payload"]["branch"], "main")

    def test_incorrect_readback_is_failure(self):
        states = [(b"stale", "old-sha"), (b"still-stale", "wrong-sha")]
        with patch.object(sync, "remote_bytes", side_effect=states):
            with patch.object(sync, "github_api"):
                with self.assertRaises(RuntimeError):
                    sync.ensure("owner/repo", "canon.md", b"expected", False)

    def test_missing_file_can_be_created(self):
        states = [(None, None), (b"new", "sha-new")]
        with patch.object(sync, "remote_bytes", side_effect=states):
            with patch.object(sync, "github_api") as api:
                self.assertEqual(sync.ensure("owner/repo", "canon.md", b"new", False),
                                 "verified")
                _, kwargs = api.call_args
                self.assertNotIn("sha", kwargs["payload"])

    def test_path_scope_and_duplicate_target_protection(self):
        for path in ["/absolute.md", "foo/../root.md", "foo//bar.md",
                     "foo\\windows.md", ""]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                sync.validate_path(path)
        with TemporaryDirectory() as temp:
            path = Path(temp) / "registry.yaml"
            path.write_text(
                "schema: xos.canon-synchronization/v1\n"
                "canonical_repository: XLR8ROS/xlr8ros-hq\n"
                "artifacts:\n"
                "  a:\n"
                "    source: canon/a.yaml\n"
                "    hq_markdown: A.md\n"
                "    downstream:\n"
                "      - repository: XLR8ROS/xlr8ros-hq\n"
                "        path: A.md\n",
                encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                sync.load_registry(path)

    def test_real_registry_covers_current_codi_and_external_sead(self):
        artifacts = sync.load_registry()
        entries = {name: (src, targets) for name, src, targets in artifacts}
        for name in ("constitution", "global-memory-contract",
                     "xos-hq-operations-control-sop"):
            targets = entries[name][1]
            self.assertTrue(any(repo == "XLR8ROS/CodiCore" for repo, _ in targets))
            self.assertTrue(any(repo == "XLR8ROS/ALPHACORE-SR." for repo, _ in targets))
            self.assertTrue(any(repo == "XLR8ROS/COCOCORE" for repo, _ in targets))
        for name in ("sead-division-sop", "position-sop-chief-of-sead"):
            source, targets = entries[name]
            self.assertEqual(source[0], "XLR8ROS/XLR8ROS_SEAD")
            self.assertTrue(any(repo == "XLR8ROS/CodiCore" for repo, _ in targets))


    def test_approved_president_sop_mirrors_from_governed_yaml(self):
        entries = {name: (source, targets) for name, source, targets in sync.load_registry()}
        self.assertIn("position-sop-president", entries)
        source, targets = entries["position-sop-president"]
        self.assertEqual(source[1], "canon/position-sop-president.yaml")
        self.assertEqual(targets, [
            (sync.HQ, "Position SOP 4 President.md"),
            ("XLR8ROS/ALPHACORE-SR.", "Position SOP 4 President.md"),
        ])
        self.assertIn("position-sop-svp-executive-affairs", entries)
        proposed_source, proposed_targets = entries["position-sop-svp-executive-affairs"]
        self.assertEqual(proposed_source[1], "canon/position-sop-svp-executive-affairs.yaml")
        self.assertIn(("XLR8ROS/COCOCORE", "Position SOP 4 Senior VP of Executive Affairs.md"), proposed_targets)
        proposal = sync.yaml.safe_load((sync.ROOT / proposed_source[1]).read_text(encoding="utf-8"))
        self.assertEqual(proposal.get("status"), "proposed_reg_review")
        self.assertIs(proposal.get("source_of_truth"), False)
        yaml_text = (sync.ROOT / source[1]).read_text(encoding="utf-8")
        approved = sync.yaml.safe_load(yaml_text)
        self.assertEqual(approved.get("status"), "authoritative")
        self.assertTrue(approved.get("source_of_truth"))
        result = sync.rendered_content(*source[:2], yaml_text, source[2], source[3])
        self.assertEqual(result, (sync.ROOT / source[2]).read_bytes())

    def test_proposed_personal_sop_is_not_authoritative(self):
        text = (
            "status: proposed_reg_review\n"
            "source_of_truth: false\n"
            "render:\n  mode: literal\n  markdown_path: Position SOP 4 President.md\n"
            "content: |\n  # Proposed President\n"
        )
        with self.assertRaises(ValueError):
            sync.rendered_content(sync.HQ, "canon/position-sop-president.yaml",
                                  text, "Position SOP 4 President.md", "none")

    def test_pending_personal_sop_skips_writes(self):
        yaml_text = (
            "status: proposed_reg_review\n"
            "source_of_truth: false\n"
            "render:\n  mode: literal\n  markdown_path: Draft.md\n"
            "content: |\n  # Draft\n"
        )
        with TemporaryDirectory() as temp:
            home = Path(temp)
            (home / "canon").mkdir()
            (home / "canon" / "draft.yaml").write_text(yaml_text, encoding="utf-8")
            old_root = sync.ROOT
            old_token = sync.TOKEN
            try:
                sync.ROOT = home
                sync.TOKEN = "test-without-real-network"
                with patch.object(sync, "load_registry", return_value=[
                    ("draft", (sync.HQ, "canon/draft.yaml", "Draft.md", "none"),
                     [("owner/repo", "Draft.md")])
                ]):
                    with patch.object(sync, "ensure") as ensure:
                        self.assertEqual(sync.synchronize("sync"), 0)
                        ensure.assert_not_called()
            finally:
                sync.ROOT = old_root
                sync.TOKEN = old_token


    def test_approved_reference_preserves_original_company_contract(self):
        yaml_text = (
            "status: authoritative-reference\\n"
            "source_of_truth: true\\n"
            "render:\\n  mode: literal\\n  markdown_path: reference/Test.md\\n"
            "content: |\\n  # Shared reference\\n"
        )
        rendered = sync.rendered_content(sync.HQ, "canon/reference.yaml", yaml_text,
                                          "reference/Test.md", "none")
        self.assertEqual(rendered, b"# Shared reference\\n")



if __name__ == "__main__":
    unittest.main()
