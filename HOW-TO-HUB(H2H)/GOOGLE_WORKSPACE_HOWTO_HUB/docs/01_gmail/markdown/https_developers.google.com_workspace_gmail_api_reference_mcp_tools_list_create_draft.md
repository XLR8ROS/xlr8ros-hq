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

  <a href="https://developers.google.com/workspace/gmail" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="3" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="3" data-track-metadata-eventdetail="Gmail">Gmail</a>

- <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true">

  </div>

  <a href="https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="4" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="4" data-track-metadata-eventdetail="">MCP server</a>

</div>

Send feedback

# MCP Tools Reference: gmailmcp.googleapis.com <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

<div id="/workspace/gmail/api/reference/mcp/tools_list/create_draft" class="section">

<div id="GENERIC" class="section">

## Tool: `create_draft`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Creates a new draft email in the authenticated user's Gmail account.

This tool takes recipient addresses, a subject, and body content as inputs. It returns the ID of the created Gmail draft. If the draft is created as a reply to an existing message, the ID of the original message should be passed to the tool in the replyToMessageId field. Creating drafts with attachments is not supported yet.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `create_draft` MCP tool.

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
<pre class="devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded="" data-syntax="Bash"><code>curl --location &#39;https://gmailmcp.googleapis.com/mcp/v1&#39; \
--header &#39;content-type: application/json&#39; \
--header &#39;accept: application/json, text/event-stream&#39; \
--data &#39;{
  &quot;method&quot;: &quot;tools/call&quot;,
  &quot;params&quot;: {
    &quot;name&quot;: &quot;create_draft&quot;,
    &quot;arguments&quot;: {
      // provide these details according to the tool&#39;s MCP specification
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

Request message for CreateDraft RPC.

</div>

<div id="Input.Schema.CreateDraftRequest" class="section">

### CreateDraftRequest

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
  &quot;to&quot;: [
    string
  ],
  &quot;cc&quot;: [
    string
  ],
  &quot;bcc&quot;: [
    string
  ],
  &quot;subject&quot;: string,
  &quot;body&quot;: string,
  &quot;htmlBody&quot;: string,
  &quot;replyToMessageId&quot;: string
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
<td><code translate="no" dir="ltr">to[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The primary recipients of the email draft. Each string MUST be a valid plain email address (e.g., "user@example.com"). The "Name <a href="mailto:email@example.com">email@example.com</a>" format is NOT supported by this tool.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">cc[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. The carbon copy recipients of the email draft. Each string MUST be a valid plain email address (e.g., "user@example.com"). The "Name <a href="mailto:email@example.com">email@example.com</a>" format is NOT supported by this tool.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">bcc[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. The blind carbon copy recipients of the email draft. Each string MUST be a valid plain email address (e.g., "user@example.com"). The "Name <a href="mailto:email@example.com">email@example.com</a>" format is NOT supported by this tool.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">subject</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. The subject line of the email. Defaults to empty if not provided.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_4">
<td><code translate="no" dir="ltr">body</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. The main body content of the email draft. If html_body is also provided, this field is treated as the plain-text alternative.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_5">
<td><code translate="no" dir="ltr">htmlBody</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The HTML content of the email draft. If provided, this will be used as the rich-text version of the email.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_6">
<td><code translate="no" dir="ltr">replyToMessageId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. The ID of the message to reply to. If provided, this will be used as the reply-to message ID for the email draft, and the <code translate="no" dir="ltr">body</code> and <code translate="no" dir="ltr">html_body</code> will be appended to the original message body.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Details of a draft.

</div>

<div id="Output.Schema.Draft" class="section">

### Draft

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
  &quot;subject&quot;: string,
  &quot;threadId&quot;: string,
  &quot;toRecipients&quot;: [
    string
  ],
  &quot;ccRecipients&quot;: [
    string
  ],
  &quot;bccRecipients&quot;: [
    string
  ],
  &quot;plaintextBody&quot;: string,
  &quot;date&quot;: string
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
<p>The unique identifier of the draft resource.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">subject</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The subject line of the draft message.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">threadId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The ID of the thread this draft belongs to.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">toRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>List of 'To' recipient email addresses extracted from headers.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_4">
<td><code translate="no" dir="ltr">ccRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>List of 'Cc' recipient email addresses extracted from headers.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_5">
<td><code translate="no" dir="ltr">bccRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>List of 'Bcc' recipient email addresses extracted from headers.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_6">
<td><code translate="no" dir="ltr">plaintextBody</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Plain text body content, if available.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_7">
<td><code translate="no" dir="ltr">date</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Date of the draft in ISO 8601 format (YYYY-MM-DD).</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="GENERIC_3" class="section">

### Tool Annotations

Destructive Hint: ❌ \| Idempotent Hint: ❌ \| Read Only Hint: ❌ \| Open World Hint: ❌

</div>

</div>

</div>

Send feedback

<div class="devsite-floating-action-buttons">

</div>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-13 UTC."\],\[\],\[\]\]

</div>

</div>
