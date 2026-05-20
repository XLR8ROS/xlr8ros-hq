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

<div id="/workspace/gmail/api/reference/mcp/tools_list/list_drafts" class="section">

<div id="GENERIC" class="section">

## Tool: `list_drafts`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Lists draft emails from the authenticated user's Gmail account.

This tool can filter drafts based on a query string and supports pagination. It returns a list of drafts, including their IDs and subjects. `page_token` can be used to paginate the results. To retrieve subsequent pages of results, use the `page_token` returned in the previous response.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `list_drafts` MCP tool.

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
    &quot;name&quot;: &quot;list_drafts&quot;,
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

Request message for ListDrafts RPC.

</div>

<div id="Input.Schema.ListDraftsRequest" class="section">

### ListDraftsRequest

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
&#10;  &quot;pageSize&quot;: integer
&#10;  &quot;pageToken&quot;: string
&#10;  &quot;query&quot;: string
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
<tr id="Input.Schema.FIELDS.ONEOF" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_page_size</code>.</p>
<p><code translate="no" dir="ltr">_page_size</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section">
<td><code translate="no" dir="ltr">pageSize</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Optional. The maximum number of drafts to return. If unspecified, defaults to 20. The maximum allowed value is 50.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_page_token</code>.</p>
<p><code translate="no" dir="ltr">_page_token</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">pageToken</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. A token received from a previous list_drafts call to retrieve the next page of results. Leave empty to fetch the first page. This is primarily used for pagination to continue fetching results from where the previous <code translate="no" dir="ltr">ListDraft</code> call left off, especially when the number of drafts matching the query exceeds the page_size limit.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF_2" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_query</code>.</p>
<p><code translate="no" dir="ltr">_query</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">query</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Examples: "subject:OneMCP Update" "from:<a href="mailto:gduser1@workspacesamples.dev">gduser1@workspacesamples.dev</a>" "to:<a href="mailto:gduser2@workspacesamples.dev">gduser2@workspacesamples.dev</a> AND newer_than:7d" "project proposal has:attachment" "is:unread"</p>
<p>A space or a dash (<code translate="no" dir="ltr">-</code>) will separate a number while a dot (<code translate="no" dir="ltr">.</code>) will be a decimal. For example, <code translate="no" dir="ltr">01.2047-100</code> is considered two numbers: <code translate="no" dir="ltr">01.2047</code> and <code translate="no" dir="ltr">100</code>.</p>
<p>Note: If we want to ensure all drafts for the query are returned, we can paginate the results by making repeated calls to the tool until the response contains an empty list of drafts.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Response message for ListDrafts RPC.

</div>

<div id="Output.Schema.ListDraftsResponse" class="section">

### ListDraftsResponse

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
  &quot;drafts&quot;: [
    {
      object (Draft)
    }
  ],
  &quot;nextPageToken&quot;: string
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
<td><code translate="no" dir="ltr">drafts[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/gmail/api/reference/mcp/tools_list/create_draft#Output.Schema.Draft"><code translate="no" dir="ltr">Draft</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>List of drafts.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">nextPageToken</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>A token that can be used in a subsequent call to retrieve the next page of drafts. If the number of drafts matching the query exceeds the page_size limit, the response will contain a <code translate="no" dir="ltr">next_page_token</code>. To retrieve the next page of results, pass this token in the <code translate="no" dir="ltr">page_token</code> field of the next <code translate="no" dir="ltr">ListDraftsRequest</code>.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Draft" class="section">

### Draft

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
<p>The unique identifier of the draft resource.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">subject</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The subject line of the draft message.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">threadId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The ID of the thread this draft belongs to.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_3">
<td><code translate="no" dir="ltr">toRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>List of 'To' recipient email addresses extracted from headers.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_4">
<td><code translate="no" dir="ltr">ccRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>List of 'Cc' recipient email addresses extracted from headers.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_5">
<td><code translate="no" dir="ltr">bccRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>List of 'Bcc' recipient email addresses extracted from headers.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_6">
<td><code translate="no" dir="ltr">plaintextBody</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Plain text body content, if available.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_7">
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
