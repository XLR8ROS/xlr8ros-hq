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

<div id="/workspace/gmail/api/reference/mcp/tools_list/create_label" class="section">

<div id="GENERIC" class="section">

## Tool: `create_label`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Creates a new label in the authenticated user's Gmail account.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `create_label` MCP tool.

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
    &quot;name&quot;: &quot;create_label&quot;,
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

Request message for CreateLabel RPC.

</div>

<div id="Input.Schema.CreateLabelRequest" class="section">

### CreateLabelRequest

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
  &quot;displayName&quot;: string,
&#10;  &quot;color&quot;: {
    object (LabelColor)
  }
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
<td><code translate="no" dir="ltr">displayName</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The display name of the label to create.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_color</code>.</p>
<p><code translate="no" dir="ltr">_color</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">color</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/gmail/api/reference/mcp/tools_list/list_labels#Output.Schema.LabelColor"><code translate="no" dir="ltr">LabelColor</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional. The color of the label.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Input.Schema.LabelColor" class="section">

### LabelColor

</div>

<div id="Input.Schema.SCHEMA_REPRESENTATION_1" class="section">

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
  &quot;textColor&quot;: string,
  &quot;backgroundColor&quot;: string
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Input.Schema.FIELDS_1" class="section">

<table id="Input.Schema.FIELDS_1-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Input.Schema.FIELDS_1.field_section">
<td><code translate="no" dir="ltr">textColor</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The text color of the label, represented as a hex string (e.g., "#000000").</p></td>
</tr>
<tr id="Input.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">backgroundColor</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The background color of the label, represented as a hex string (e.g., "#ffffff").</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Details of a label.

</div>

<div id="Output.Schema.Label" class="section">

### Label

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
  &quot;labelId&quot;: string,
  &quot;name&quot;: string,
  &quot;color&quot;: {
    object (LabelColor)
  },
&#10;  &quot;threadsTotal&quot;: integer
&#10;  &quot;threadsUnread&quot;: integer
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
<td><code translate="no" dir="ltr">labelId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The unique identifier of the label.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">name</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The human-readable display name of the label.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">color</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/gmail/api/reference/mcp/tools_list/list_labels#Output.Schema.LabelColor"><code translate="no" dir="ltr">LabelColor</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional. The color of the label.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_threads_total</code>.</p>
<p><code translate="no" dir="ltr">_threads_total</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">threadsTotal</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>The total number of threads under the label.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_threads_unread</code>.</p>
<p><code translate="no" dir="ltr">_threads_unread</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_4">
<td><code translate="no" dir="ltr">threadsUnread</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>The number of unread threads under the label.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.LabelColor" class="section">

### LabelColor

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
  &quot;textColor&quot;: string,
  &quot;backgroundColor&quot;: string
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
<td><code translate="no" dir="ltr">textColor</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The text color of the label, represented as a hex string (e.g., "#000000").</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">backgroundColor</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The background color of the label, represented as a hex string (e.g., "#ffffff").</p></td>
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
