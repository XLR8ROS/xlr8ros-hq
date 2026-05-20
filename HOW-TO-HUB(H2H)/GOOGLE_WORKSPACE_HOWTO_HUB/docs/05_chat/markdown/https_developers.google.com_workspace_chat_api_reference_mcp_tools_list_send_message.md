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

<div id="/workspace/chat/api/reference/mcp/tools_list/send_message" class="section">

<div id="GENERIC" class="section">

## Tool: `send_message`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Sends a Google Chat message to a conversation.

This tool uses a conversation ID, an optional thread ID, and a message text as inputs. Conversation ID's can be found using the search_conversations tool. It returns the created message.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `send_message` MCP tool.

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
    &quot;name&quot;: &quot;send_message&quot;,
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

Request to send a message to a Google Chat conversation.

</div>

<div id="Input.Schema.SendMessageRequest" class="section">

### SendMessageRequest

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
  &quot;conversationId&quot;: string,
  &quot;threadId&quot;: string,
  &quot;messageText&quot;: string
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
<td><code translate="no" dir="ltr">conversationId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The ID of the conversation (e.g., 'spaces/AAAA...') to send the message to.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">threadId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. The ID of the thread (e.g., 'spaces/AAAA.../threads/BBBB...') to send the message to. If not set, the message will be sent to a new thread.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">messageText</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The main content of the message. Basic formatting can be added using a subset of Markdown. For information about how to format messages, see <a href="https://developers.google.com/workspace/chat/format-messages">Format messages</a>. The following formatting is supported:</p>
<ul>
<li><strong>Bold:</strong> <code translate="no" dir="ltr">*text*</code></li>
<li><strong>Italic:</strong> <code translate="no" dir="ltr">_text_</code></li>
<li><strong>Strikethrough:</strong> <code translate="no" dir="ltr">~text~</code></li>
<li><strong>Monospace:</strong> <code translate="no" dir="ltr">text</code></li>
<li><strong>Monospace block:</strong></li>
</ul>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>```
line 1
line 2
```</code></pre>
<ul>
<li><strong>Bulleted list:</strong></li>
</ul>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>* item 1
* item 2</code></pre>
<ul>
<li><strong>Block quote:</strong> <code translate="no" dir="ltr">&gt; quoted text</code></li>
<li><strong>Hyperlink:</strong> <code translate="no" dir="ltr">&lt;url|display text&gt;</code></li>
<li><strong>Mention user:</strong> <code translate="no" dir="ltr">&lt;users/{user_id}&gt;</code></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Response to sending a message to a Google Chat conversation.

</div>

<div id="Output.Schema.SendMessageResponse" class="section">

### SendMessageResponse

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
  &quot;message&quot;: {
    object (ChatMessage)
  }
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
<td><code translate="no" dir="ltr">message</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/chat/api/reference/mcp/tools_list/list_messages#Output.Schema.ChatMessage"><code translate="no" dir="ltr">ChatMessage</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The message that was sent.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ChatMessage" class="section">

### ChatMessage

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
  &quot;messageId&quot;: string,
  &quot;threadId&quot;: string,
  &quot;plaintextBody&quot;: string,
  &quot;sender&quot;: {
    object (User)
  },
  &quot;createTime&quot;: string,
  &quot;threadedReply&quot;: boolean,
  &quot;attachments&quot;: [
    {
      object (ChatAttachmentMetadata)
    }
  ],
  &quot;reactionSummaries&quot;: [
    {
      object (ReactionSummary)
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
<td><code translate="no" dir="ltr">messageId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Resource name of the message. Format: <code translate="no" dir="ltr">spaces/{space}/messages/{message}</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">threadId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The thread this message belongs to. This will be empty if the message is unthreaded. Format: spaces/{space}/threads/{thread}</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">plaintextBody</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Plain text body of the message.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_3">
<td><code translate="no" dir="ltr">sender</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/chat/api/reference/mcp/tools_list/list_messages#Output.Schema.User"><code translate="no" dir="ltr">User</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The sender of the message.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_4">
<td><code translate="no" dir="ltr">createTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Output only. Timestamp when the message was created.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_5">
<td><code translate="no" dir="ltr">threadedReply</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Whether message is a thread reply.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_6">
<td><code translate="no" dir="ltr">attachments[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/chat/api/reference/mcp/tools_list/list_messages#Output.Schema.ChatAttachmentMetadata"><code translate="no" dir="ltr">ChatAttachmentMetadata</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Attachments included in the message.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_7">
<td><code translate="no" dir="ltr">reactionSummaries[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/chat/api/reference/mcp/tools_list/list_messages#Output.Schema.ReactionSummary"><code translate="no" dir="ltr">ReactionSummary</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The emoji reactions summary included in the message.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.User" class="section">

### User

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
  &quot;userId&quot;: string,
  &quot;displayName&quot;: string,
  &quot;email&quot;: string,
  &quot;userType&quot;: enum (UserType)
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
<td><code translate="no" dir="ltr">userId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Resource name of a Chat user. Format: users/{user}.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_1">
<td><code translate="no" dir="ltr">displayName</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The display name of a Chat user.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_2">
<td><code translate="no" dir="ltr">email</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The email address of the user. This field is only populated when the user type is HUMAN.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_3">
<td><code translate="no" dir="ltr">userType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><a href="/workspace/chat/api/reference/mcp/tools_list/list_messages#Output.Schema.UserType"><code translate="no" dir="ltr">UserType</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The type of the user.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ChatAttachmentMetadata" class="section">

### ChatAttachmentMetadata

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_3" class="section">

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
  &quot;attachmentId&quot;: string,
  &quot;filename&quot;: string,
  &quot;mimeType&quot;: string,
  &quot;source&quot;: enum (Source)
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_3" class="section">

<table id="Output.Schema.FIELDS_3-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_3.field_section">
<td><code translate="no" dir="ltr">attachmentId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Resource name of the attachment. Format: spaces/{space}/messages/{message}/attachments/{attachment}.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_1">
<td><code translate="no" dir="ltr">filename</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Name of the attachment.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_2">
<td><code translate="no" dir="ltr">mimeType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Content type (MIME type).</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_3">
<td><code translate="no" dir="ltr">source</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><a href="/workspace/chat/api/reference/mcp/tools_list/list_messages#Output.Schema.Source"><code translate="no" dir="ltr">Source</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The source of the attachment.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ReactionSummary" class="section">

### ReactionSummary

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_4" class="section">

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
  &quot;emoji&quot;: string,
  &quot;count&quot;: integer
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_4" class="section">

<table id="Output.Schema.FIELDS_4-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_4.field_section">
<td><code translate="no" dir="ltr">emoji</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The emoji unicode string or custom emoji name.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section_1">
<td><code translate="no" dir="ltr">count</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>The total number of reactions using the associated emoji.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.UserType" class="section">

### UserType

</div>

<div id="Output.Schema.description_1" class="section">

The type of a Google Chat user.

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
<tr id="Output.Schema.ENUM_VALUES.USER_TYPE_UNSPECIFIED">
<td><code class="apitype" translate="no" dir="ltr">USER_TYPE_UNSPECIFIED</code></td>
<td>Unspecified.</td>
</tr>
<tr id="Output.Schema.ENUM_VALUES.HUMAN">
<td><code class="apitype" translate="no" dir="ltr">HUMAN</code></td>
<td>Human user.</td>
</tr>
<tr id="Output.Schema.ENUM_VALUES.APP">
<td><code class="apitype" translate="no" dir="ltr">APP</code></td>
<td>App user.</td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Source" class="section">

### Source

</div>

<div id="Output.Schema.description_2" class="section">

The source of the attachment.

</div>

<div id="Output.Schema.ENUM_VALUES_1" class="section">

<table id="Output.Schema.ENUM_VALUES_1-table" class="constants responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.ENUM_VALUES_1.SOURCE_UNSPECIFIED">
<td><code class="apitype" translate="no" dir="ltr">SOURCE_UNSPECIFIED</code></td>
<td>Reserved.</td>
</tr>
<tr id="Output.Schema.ENUM_VALUES_1.DRIVE_FILE">
<td><code class="apitype" translate="no" dir="ltr">DRIVE_FILE</code></td>
<td>The file is a Google Drive file.</td>
</tr>
<tr id="Output.Schema.ENUM_VALUES_1.UPLOADED_CONTENT">
<td><code class="apitype" translate="no" dir="ltr">UPLOADED_CONTENT</code></td>
<td>The file is uploaded to Chat.</td>
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

Last updated 2026-05-08 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-08 UTC."\],\[\],\[\]\]

</div>

</div>
