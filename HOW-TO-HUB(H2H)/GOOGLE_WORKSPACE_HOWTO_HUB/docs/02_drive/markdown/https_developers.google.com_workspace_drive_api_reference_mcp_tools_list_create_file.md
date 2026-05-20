<div id="main-content" class="devsite-main-content" role="main" has-book-nav="" has-sidebar="">

<div class="devsite-sidebar">

<div class="devsite-sidebar-content">

</div>

</div>

<div class="devsite-article-meta nocontent" role="navigation" nosnippet="">

- <a href="https://developers.google.com/" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="1" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="1" data-track-metadata-eventdetail="">Home</a>

- <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true">

  </div>

  <a href="https://developers.google.com/workspace" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="2" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="2" data-track-metadata-eventdetail="Google Workspace">Google Workspace</a>

- <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true">

  </div>

  <a href="https://developers.google.com/workspace/drive" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="3" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="3" data-track-metadata-eventdetail="Google Drive">Google Drive</a>

- <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true">

  </div>

  <a href="https://developers.google.com/workspace/drive/api/guides/configure-mcp-server" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="4" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="4" data-track-metadata-eventdetail="">MCP server</a>

</div>

Send feedback

# MCP Tools Reference: drivemcp.googleapis.com <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

<div id="/workspace/drive/api/reference/mcp/tools_list/create_file" class="section">

<div id="GENERIC" class="section">

## Tool: `create_file`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Call this tool to create or upload a File to Google Drive.

If uploading a file, the content needs to be base64 encoded into the `content` field regardless of the mimetype of the file being uploaded.

Returns a single File object upon successful creation.

The following Google Drive first-party mime types can be created without providing content:

- `application/vnd.google-apps.document`
- `application/vnd.google-apps.spreadsheet`
- `application/vnd.google-apps.presentation`

By default, the following conversions will be made for the following mime types:

- `text/plain` to `application/vnd.google-apps.document`
- `text/csv` to `application/vnd.google-apps.spreadsheet`

To disable conversions for first-party mime types, set `disable_conversion_to_google_type` to true.

Folders can be created by setting the mime type to `application/vnd.google-apps.folder`.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `create_file` MCP tool.

</div>

<div id="MCP_CURL_REQUEST" class="section">

<table class="properties responsive fixed">
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Curl Request</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin: 0; padding: 0"><div>
&#10;</div>
<pre class="devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded="" data-syntax="Bash"><code>curl --location &#39;https://drivemcp.googleapis.com/mcp&#39; \
--header &#39;content-type: application/json&#39; \
--header &#39;accept: application/json, text/event-stream&#39; \
--data &#39;{
  &quot;method&quot;: &quot;tools/call&quot;,
  &quot;params&quot;: {
    &quot;name&quot;: &quot;create_file&quot;,
    &quot;arguments&quot;: {
      // provide these details according to the tool MCP specification
    }
  },
  &quot;jsonrpc&quot;: &quot;2.0&quot;,
  &quot;id&quot;: 1
}&#39;
                </code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Input.Schema" class="section">

## Input Schema

<div id="Input.Schema.description" class="section">

Request to upload a file.

</div>

<div id="Input.Schema.CreateFileRequest" class="section">

### CreateFileRequest

</div>

<div id="Input.Schema.SCHEMA_REPRESENTATION" class="section">

<table class="properties responsive fixed">
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin: 0; padding: 0"><div>
&#10;</div>
<pre style="border: 0;margin: 0;" translate="no" dir="ltr" data-is-upgraded=""><code>{
  &quot;title&quot;: string,
  &quot;mimeType&quot;: string,
  &quot;content&quot;: string,
  &quot;parentId&quot;: string,
  &quot;disableConversionToGoogleType&quot;: boolean
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Input.Schema.FIELDS" class="section">

<table id="Input.Schema.FIELDS-table" class="properties responsive fixed" style="width:25%;">
<colgroup>
<col style="width: 25%" />
<col />
</colgroup>
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<tbody>
<tr id="Input.Schema.FIELDS.field_section">
<td><code translate="no" dir="ltr">title</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The title of the file.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">mimeType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The mime type of the file to upload.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">content</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The content of the file encoded as base64. The content field should always be base64 encoded regardless of the mime type of the file.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">parentId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The parent id of the file.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_4">
<td><code translate="no" dir="ltr">disableConversionToGoogleType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>If true, the file will not be converted to a Google type. Has no effect for mime types that do not have a Google equivalent.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

A file resource.

</div>

<div id="Output.Schema.File" class="section">

### File

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION" class="section">

<table class="properties responsive fixed">
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin: 0; padding: 0"><div>
&#10;</div>
<pre style="border: 0;margin: 0;" translate="no" dir="ltr" data-is-upgraded=""><code>{
  &quot;id&quot;: string,
  &quot;title&quot;: string,
  &quot;parentId&quot;: string,
&#10;  &quot;mimeType&quot;: string
&#10;  &quot;fileSize&quot;: string
&#10;  &quot;description&quot;: string
&#10;  &quot;fileExtension&quot;: string
&#10;  &quot;contentSnippet&quot;: string
&#10;  &quot;viewUrl&quot;: string
&#10;  &quot;sharedWithMeTime&quot;: string
&#10;  &quot;createdTime&quot;: string
&#10;  &quot;modifiedTime&quot;: string
&#10;  &quot;viewedByMeTime&quot;: string
&#10;  &quot;owner&quot;: string
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS" class="section">

<table id="Output.Schema.FIELDS-table" class="properties responsive fixed" style="width:25%;">
<colgroup>
<col style="width: 25%" />
<col />
</colgroup>
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<tbody>
<tr id="Output.Schema.FIELDS.field_section">
<td><code translate="no" dir="ltr">id</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The id of the file that was fetched.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">title</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The title of the file.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">parentId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The (optional) id of the parent of the file.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_mime_type</code>.</p>
<p><code translate="no" dir="ltr">_mime_type</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">mimeType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The mime type of the file.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_file_size</code>.</p>
<p><code translate="no" dir="ltr">_file_size</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_4">
<td><code translate="no" dir="ltr">fileSize</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://developers.google.com/discovery/v1/type-format"><code class="apitype" translate="no" dir="ltr">int64</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>The size in bytes of the file.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_2" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_description</code>.</p>
<p><code translate="no" dir="ltr">_description</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_5">
<td><code translate="no" dir="ltr">description</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The description of the file.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_3" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_file_extension</code>.</p>
<p><code translate="no" dir="ltr">_file_extension</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_6">
<td><code translate="no" dir="ltr">fileExtension</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The original file extension of the file, this is only populated for files with content stored in Drive.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_4" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_content_snippet</code>.</p>
<p><code translate="no" dir="ltr">_content_snippet</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_7">
<td><code translate="no" dir="ltr">contentSnippet</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Generated snippet about the content of the file.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_5" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_view_url</code>.</p>
<p><code translate="no" dir="ltr">_view_url</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_8">
<td><code translate="no" dir="ltr">viewUrl</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The URL to view the file.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_6" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_shared_with_me_time</code>.</p>
<p><code translate="no" dir="ltr">_shared_with_me_time</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_9">
<td><code translate="no" dir="ltr">sharedWithMeTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp"><code translate="no" dir="ltr">Timestamp</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>The time that the file was shared with the requester.</p>
<p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_7" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_created_time</code>.</p>
<p><code translate="no" dir="ltr">_created_time</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_10">
<td><code translate="no" dir="ltr">createdTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp"><code translate="no" dir="ltr">Timestamp</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>The time that the file was created.</p>
<p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_8" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_modified_time</code>.</p>
<p><code translate="no" dir="ltr">_modified_time</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_11">
<td><code translate="no" dir="ltr">modifiedTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp"><code translate="no" dir="ltr">Timestamp</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>The most recent time at which the file was modified.</p>
<p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_9" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_viewed_by_me_time</code>.</p>
<p><code translate="no" dir="ltr">_viewed_by_me_time</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_12">
<td><code translate="no" dir="ltr">viewedByMeTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp"><code translate="no" dir="ltr">Timestamp</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>The most recent time at which the file was viewed by requester.</p>
<p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_10" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_owner</code>.</p>
<p><code translate="no" dir="ltr">_owner</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_13">
<td><code translate="no" dir="ltr">owner</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The email address of the owner of the file.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Timestamp" class="section">

### Timestamp

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_1" class="section">

<table class="properties responsive fixed">
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>JSON representation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="margin: 0; padding: 0"><div>
&#10;</div>
<pre style="border: 0;margin: 0;" translate="no" dir="ltr" data-is-upgraded=""><code>{
  &quot;seconds&quot;: string,
  &quot;nanos&quot;: integer
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_1" class="section">

<table id="Output.Schema.FIELDS_1-table" class="properties responsive fixed" style="width:25%;">
<colgroup>
<col style="width: 25%" />
<col />
</colgroup>
<thead>
<tr>
<th colspan="2">Fields</th>
</tr>
</thead>
<tbody>
<tr id="Output.Schema.FIELDS_1.field_section">
<td><code translate="no" dir="ltr">seconds</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://developers.google.com/discovery/v1/type-format"><code class="apitype" translate="no" dir="ltr">int64</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">nanos</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="GENERIC_3" class="section">

### Tool Annotations

Destructive Hint: ❌ \| Idempotent Hint: ❌ \| Read Only Hint: ❌ \| Open World Hint: ✅

</div>

</div>

</div>

Send feedback

<div class="devsite-floating-action-buttons">

</div>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-04-14 UTC."\],\[\],\[\]\]

</div>

</div>
