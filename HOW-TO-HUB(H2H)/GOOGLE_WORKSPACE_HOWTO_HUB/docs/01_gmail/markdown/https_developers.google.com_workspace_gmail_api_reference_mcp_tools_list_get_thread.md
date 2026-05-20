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

<div id="/workspace/gmail/api/reference/mcp/tools_list/get_thread" class="section">

<div id="GENERIC" class="section">

## Tool: `get_thread`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Retrieves a specific email thread from the authenticated user's Gmail account, including a list of its messages.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `get_thread` MCP tool.

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
    &quot;name&quot;: &quot;get_thread&quot;,
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

Request message for GetThread RPC.

</div>

<div id="Input.Schema.GetThreadRequest" class="section">

### GetThreadRequest

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
  &quot;threadId&quot;: string,
  &quot;messageFormat&quot;: enum (MessageFormat)
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
<td><code translate="no" dir="ltr">threadId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The unique identifier of the thread to fetch.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">messageFormat</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><a href="/workspace/gmail/api/reference/mcp/tools_list/get_thread#Input.Schema.MessageFormat"><code translate="no" dir="ltr">MessageFormat</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional. Specifies the format of the messages returned within the thread. Defaults to FULL_CONTENT. Note: If you need body content or attachments, use FULL_CONTENT. When using MINIMAL, the plaintext_body and attachment_ids fields will not be populated. If you are unsure which format to use, rely on the default behavior by using FULL_CONTENT.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Input.Schema.MessageFormat" class="section">

### MessageFormat

</div>

<div id="Input.Schema.description_1" class="section">

Enum to control the level of detail for messages in the thread.

</div>

<div id="Input.Schema.ENUM_VALUES" class="section">

<table id="Input.Schema.ENUM_VALUES-table" class="constants responsive fixed" style="width:25%;">
<colgroup>
<col style="width: 25%" />
<col />
</colgroup>
<thead>
<tr>
<th colspan="2">Enums</th>
</tr>
</thead>
<tbody>
<tr id="Input.Schema.ENUM_VALUES.MESSAGE_FORMAT_UNSPECIFIED">
<td><code class="apitype" translate="no" dir="ltr">MESSAGE_FORMAT_UNSPECIFIED</code></td>
<td>Defaults to FULL_CONTENT.</td>
</tr>
<tr id="Input.Schema.ENUM_VALUES.MINIMAL">
<td><code class="apitype" translate="no" dir="ltr">MINIMAL</code></td>
<td>Returns message snippets and key headers (Subject, From, To, Cc, Date).</td>
</tr>
<tr id="Input.Schema.ENUM_VALUES.FULL_CONTENT">
<td><code class="apitype" translate="no" dir="ltr">FULL_CONTENT</code></td>
<td>Returns all information in "MINIMAL" plus the full body content of each message.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Thread containing a list of messages.

</div>

<div id="Output.Schema.Thread" class="section">

### Thread

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
  &quot;messages&quot;: [
    {
      object (Message)
    }
  ]
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
<p>The unique identifier of the thread.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">messages[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/gmail/api/reference/mcp/tools_list/send_message#Output.Schema.Message"><code translate="no" dir="ltr">Message</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>A list of messages in the thread, ordered chronologically.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Message" class="section">

### Message

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
  &quot;id&quot;: string,
  &quot;snippet&quot;: string,
  &quot;subject&quot;: string,
  &quot;sender&quot;: string,
  &quot;toRecipients&quot;: [
    string
  ],
  &quot;ccRecipients&quot;: [
    string
  ],
  &quot;date&quot;: string,
  &quot;plaintextBody&quot;: string,
  &quot;attachmentIds&quot;: [
    string
  ]
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
<td><code translate="no" dir="ltr">id</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The unique identifier of the message.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">snippet</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Snippet of the message body.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">subject</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The message subject extracted from headers:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_3">
<td><code translate="no" dir="ltr">sender</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Sender email address.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_4">
<td><code translate="no" dir="ltr">toRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>To recipient email addresses.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_5">
<td><code translate="no" dir="ltr">ccRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>CC recipient email addresses.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_6">
<td><code translate="no" dir="ltr">date</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Date of the message in ISO 8601 format (YYYY-MM-DD).</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_7">
<td><code translate="no" dir="ltr">plaintextBody</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Full body content, only populated if MessageFormat was FULL_CONTENT.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_8">
<td><code translate="no" dir="ltr">attachmentIds[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Output only. The attachment ids, only populated if MessageFormat was FULL_CONTENT.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="GENERIC_3" class="section">

### Tool Annotations

Destructive Hint: ❌ \| Idempotent Hint: ✅ \| Read Only Hint: ✅ \| Open World Hint: ❌

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
