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

  <a href="https://developers.google.com/workspace/chat" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="3" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="3" data-track-metadata-eventdetail="Google Chat">Google Chat</a>

- <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true">

  </div>

  <a href="https://developers.google.com/workspace/chat/api/guides/configure-mcp-server" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="4" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="4" data-track-metadata-eventdetail="">MCP server</a>

</div>

Send feedback

# MCP Tools Reference: chatmcp.googleapis.com <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

<div id="/workspace/chat/api/reference/mcp/tools_list/search_conversations" class="section">

<div id="GENERIC" class="section">

## Tool: `search_conversations`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Searches for Google Chat conversations by display name.

If only participants are provided, this tool finds 1:1 direct messages (if one participant is provided) or group chats (if multiple participants are provided) that include the specified participants and the calling user.

If only a query is provided, this tool searches for conversations where the query is a case-insensitive substring of the conversation's display name.

If both participants and query are provided, this tool finds conversations by participants and then filters them by display name.

If neither participants nor query are provided, this tool lists all conversations the calling user is a member of.

This tool only lists conversations the calling user is a member of.

IMPORTANT: An empty 'conversations' list does not mean there are no more results overall. If 'next_page_token' is present, more pages can be fetched. If you get an empty list but a 'next_page_token', ask the user if you should continue the searching.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `search_conversations` MCP tool.

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
<pre class="devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded="" data-syntax="Bash"><code>curl --location &#39;https://chatmcp.googleapis.com/mcp/v1&#39; \
--header &#39;content-type: application/json&#39; \
--header &#39;accept: application/json, text/event-stream&#39; \
--data &#39;{
  &quot;method&quot;: &quot;tools/call&quot;,
  &quot;params&quot;: {
    &quot;name&quot;: &quot;search_conversations&quot;,
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

Request message for FindConversations RPC.

</div>

<div id="Input.Schema.SearchConversationsRequest" class="section">

### SearchConversationsRequest

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
  &quot;spaceNameQuery&quot;: string,
  &quot;pageSize&quot;: integer,
  &quot;pageToken&quot;: string,
  &quot;participants&quot;: [
    string
  ]
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
<td><code translate="no" dir="ltr">spaceNameQuery</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. The text to search for within the space display names.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">pageSize</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Optional. The maximum number of spaces to return. The service may return fewer than this value. If unspecified, at most 100 spaces will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">pageToken</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. A page token, received from a previous <code translate="no" dir="ltr">search_conversations</code> call. Provide this to retrieve the subsequent page.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">participants[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. List of email addresses of the participants to filter the conversations, excluding the caller.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Response message for FindConversations RPC.

</div>

<div id="Output.Schema.SearchConversationsResponse" class="section">

### SearchConversationsResponse

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
  &quot;conversations&quot;: [
    {
      object (Conversation)
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
<td><code translate="no" dir="ltr">conversations[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/chat/api/reference/mcp/tools_list/search_conversations#Output.Schema.Conversation"><code translate="no" dir="ltr">Conversation</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>List of conversation objects that match the search criteria.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">nextPageToken</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>A token that can be sent as <code translate="no" dir="ltr">page_token</code> to retrieve the next page. If this field is omitted, there are no subsequent pages.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Conversation" class="section">

### Conversation

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
  &quot;conversationId&quot;: string,
  &quot;displayName&quot;: string,
  &quot;conversationType&quot;: enum (ConversationType),
  &quot;lastActiveTimestamp&quot;: string
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
<td><code translate="no" dir="ltr">conversationId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The ID of the conversation (e.g., "spaces/AAAAAAAAA").</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">displayName</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The display name of the conversation.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">conversationType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><a href="/workspace/chat/api/reference/mcp/tools_list/search_conversations#Output.Schema.ConversationType"><code translate="no" dir="ltr">ConversationType</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The type of conversation (DIRECT_MESSAGE, GROUP_CHAT, or NAMED_SPACE).</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_3">
<td><code translate="no" dir="ltr">lastActiveTimestamp</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp"><code translate="no" dir="ltr">Timestamp</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>The last active time of the conversation in ISO 8601 format.</p>
<p>Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: <code translate="no" dir="ltr">"2014-10-02T15:01:23Z"</code>, <code translate="no" dir="ltr">"2014-10-02T15:01:23.045123456Z"</code> or <code translate="no" dir="ltr">"2014-10-02T15:01:23+05:30"</code>.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Timestamp" class="section">

### Timestamp

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
  &quot;seconds&quot;: string,
  &quot;nanos&quot;: integer
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
<td><code translate="no" dir="ltr">seconds</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://developers.google.com/discovery/v1/type-format"><code class="apitype" translate="no" dir="ltr">int64</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_1">
<td><code translate="no" dir="ltr">nanos</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ConversationType" class="section">

### ConversationType

</div>

<div id="Output.Schema.description_1" class="section">

Defines the type of conversation.

</div>

<div id="Output.Schema.ENUM_VALUES" class="section">

<table id="Output.Schema.ENUM_VALUES-table" class="constants responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.ENUM_VALUES.CONVERSATION_TYPE_UNSPECIFIED">
<td><code class="apitype" translate="no" dir="ltr">CONVERSATION_TYPE_UNSPECIFIED</code></td>
<td>Unspecified.</td>
</tr>
<tr id="Output.Schema.ENUM_VALUES.NAMED_SPACE">
<td><code class="apitype" translate="no" dir="ltr">NAMED_SPACE</code></td>
<td>A named space.</td>
</tr>
<tr id="Output.Schema.ENUM_VALUES.GROUP_CHAT">
<td><code class="apitype" translate="no" dir="ltr">GROUP_CHAT</code></td>
<td>A group chat between three or more people.</td>
</tr>
<tr id="Output.Schema.ENUM_VALUES.DIRECT_MESSAGE">
<td><code class="apitype" translate="no" dir="ltr">DIRECT_MESSAGE</code></td>
<td>A direct message between two humans, or a human and a Chat app.</td>
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

Last updated 2026-05-08 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-08 UTC."\],\[\],\[\]\]

</div>

</div>
