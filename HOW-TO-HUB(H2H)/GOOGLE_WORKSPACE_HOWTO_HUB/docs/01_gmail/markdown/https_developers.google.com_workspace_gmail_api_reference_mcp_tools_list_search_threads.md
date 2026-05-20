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

<div id="/workspace/gmail/api/reference/mcp/tools_list/search_threads" class="section">

<div id="GENERIC" class="section">

## Tool: `search_threads`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Lists email threads from the authenticated user's Gmail account.

This tool can filter threads based on a query string and supports pagination. It returns a list of threads, including their IDs and related messages. Each related message contains details like a snippet of the message body, the subject, the sender, the recipients etc. Note that the full message bodies are not returned by this tool; use the 'get_thread' tool with a thread ID to fetch the full message body if needed. Threads with excluded criteria may still appear in the results. This occurs because Gmail identifies matching messages first. For example, if you search for -is:starred, Gmail will find an entire thread if it contains at least one unstarred message, even if other emails in that same conversation are starred.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `search_threads` MCP tool.

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
    &quot;name&quot;: &quot;search_threads&quot;,
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

Request message for SearchThreads RPC.

</div>

<div id="Input.Schema.SearchThreadsRequest" class="section">

### SearchThreadsRequest

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
&#10;  &quot;includeTrash&quot;: boolean
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
<p>Optional. The maximum number of threads to return. If unspecified, defaults to 20. The maximum allowed value is 50.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_page_token</code>.</p>
<p><code translate="no" dir="ltr">_page_token</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">pageToken</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. Page token to retrieve a specific page of results in the list. Leave empty to fetch the first page. This is primarily used for pagination to continue fetching results from where the previous <code translate="no" dir="ltr">SearchThreads</code> call left off, especially when the number of threads matching the query exceeds the page_size limit.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF_2" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_query</code>.</p>
<p><code translate="no" dir="ltr">_query</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">query</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. A query string to filter the threads. Natural language queries must be pre-converted into Gmail syntax queries to use this tool. If omitted, all threads (excluding spam and trash by default) are listed.</p>
<p>Supported Operators by Category:</p>
<p>Sender &amp; Recipient: from: - Sent from a specific person. to: - Sent to a specific person. cc: - Specific people in Cc. bcc: - Specific people in Bcc. deliveredto: - Delivered to a specific address. list: - From a specific mailing list.</p>
<p>Time &amp; Date: after:YYYY/MM/DD / newer:YYYY/MM/DD - Received after a date. before:YYYY/MM/DD / older:YYYY/MM/DD - Received before a date. older_than: - Older than a duration (e.g., 1y, 2d). newer_than: - Newer than a duration.</p>
<p>Content: subject: - Words in the subject line. has: - Has specific content types (attachment, drive, youtube, document). filename: - Attachment with a specific name or type. "&lt;word/phrase&gt;" - Search for an exact word or phrase. (e.g., "holiday", "holiday vacation"). + - Match a word exactly. (e.g., +holiday, +unicorn) rfc822msgid: - Specific message ID header. AROUND - Find words near each other (e.g., holiday AROUND 10 vacation).</p>
<p>Labels &amp; Categories: label: - Under a specific label. The tool accepts label IDs, not display names. Use the list_labels tool to get the ID. category: - In a category (primary, social, promotions, updates, forums, reservations, purchases). in: - Search in specific labels (archive, snoozed, trash, sent, inbox). E.g., <code translate="no" dir="ltr">in:trash</code>, <code translate="no" dir="ltr">in:inbox</code>. Note: Drafts, archived, and sent messages are included by default; use <code translate="no" dir="ltr">-in:draft</code>, <code translate="no" dir="ltr">-in:archive</code>, and <code translate="no" dir="ltr">-in:sent</code> to exclude them. Use <code translate="no" dir="ltr">in:inbox</code> to restrict search to the inbox only. has:userlabels - Has any user labels. has:nouserlabels - Does not have any user labels. has:*-star - Specific star colors (if enabled, e.g., has:yellow-star). in:draft - Search in drafts. -in:draft means exclude drafts from the search results. in:sent - Search in sent messages. in:anywhere - Search in all folders (including spam and trash).</p>
<p>Status: is: - Search by status (important, starred, unread, read, muted).</p>
<p>Size: size: - Specific size in bytes. larger: / smaller: - Larger or smaller than a size (e.g., 10M for 10 MB).</p>
<p>Logic &amp; Grouping: AND - Match all criteria (default behavior). OR or { } - Match one or more criteria (e.g., from:amy OR from:david, {from:amy from:david}). - (minus) - Exclude criteria (e.g., -movie). ( ) - Group multiple search terms (e.g., subject:(dinner film)).</p>
<p>Examples: "subject:OneMCP Update" "from:<a href="mailto:user@example.com">user@example.com</a>" "to:<a href="mailto:user2@example.com">user2@example.com</a> AND newer_than:7d" "project proposal has:attachment" "is:unread -in:draft"</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF_3" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_include_trash</code>.</p>
<p><code translate="no" dir="ltr">_include_trash</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">includeTrash</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Optional. Include drafts from TRASH in the results. Defaults to false.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Response message for SearchThreads RPC.

</div>

<div id="Output.Schema.SearchThreadsResponse" class="section">

### SearchThreadsResponse

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
  &quot;threads&quot;: [
    {
      object (Thread)
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
<td><code translate="no" dir="ltr">threads[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/gmail/api/reference/mcp/tools_list/get_thread#Output.Schema.Thread"><code translate="no" dir="ltr">Thread</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>List of thread summaries.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">nextPageToken</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>A token that can be used in a subsequent call to retrieve the next page of threads. Present only if there are more results. If the number of threads matching the query exceeds the page_size limit, the response will contain a <code translate="no" dir="ltr">next_page_token</code>. To retrieve the next page of results, pass this token in the <code translate="no" dir="ltr">page_token</code> field of the next <code translate="no" dir="ltr">SearchThreadsRequest</code>.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Thread" class="section">

### Thread

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
<p>The unique identifier of the thread.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
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

<div id="Output.Schema.SCHEMA_REPRESENTATION_2" class="section">

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

<div id="Output.Schema.FIELDS_2" class="section">

<table id="Output.Schema.FIELDS_2-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_2.field_section">
<td><code translate="no" dir="ltr">id</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The unique identifier of the message.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_1">
<td><code translate="no" dir="ltr">snippet</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Snippet of the message body.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_2">
<td><code translate="no" dir="ltr">subject</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The message subject extracted from headers:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_3">
<td><code translate="no" dir="ltr">sender</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Sender email address.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_4">
<td><code translate="no" dir="ltr">toRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>To recipient email addresses.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_5">
<td><code translate="no" dir="ltr">ccRecipients[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>CC recipient email addresses.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_6">
<td><code translate="no" dir="ltr">date</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Date of the message in ISO 8601 format (YYYY-MM-DD).</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_7">
<td><code translate="no" dir="ltr">plaintextBody</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Full body content, only populated if MessageFormat was FULL_CONTENT.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_8">
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
