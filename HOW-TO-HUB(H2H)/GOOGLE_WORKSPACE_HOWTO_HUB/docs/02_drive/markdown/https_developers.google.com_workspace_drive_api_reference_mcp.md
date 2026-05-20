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

# MCP Reference: drivemcp.googleapis.com <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

<div id="/workspace/drive/api/reference/mcp/index" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

This is an MCP server provided by Drive API. The server provides tools for developers to build LLM applications on top of Drive.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [configure the Drive MCP server](https://developers.google.com/workspace/drive/api/guides/configure-mcp-server) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

<div id="rest_endpoints">

</div>

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Drive API MCP server has the following global MCP endpoint:

- https://drivemcp.googleapis.com/mcp/v1

## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The drivemcp.googleapis.com MCP server has the following tools:

<div id="toolsSection" class="section">

<table id="toolsSection-table" class="properties responsive fixed" style="width:25%;">
<colgroup>
<col style="width: 25%" />
<col />
</colgroup>
<thead>
<tr>
<th colspan="2">MCP Tools</th>
</tr>
</thead>
<tbody>
<tr id="toolsSection.create_file">
<td><a href="/workspace/drive/api/reference/mcp/tools_list/create_file">create_file</a></td>
<td><p>Call this tool to create or upload a File to Google Drive.</p>
<p>If uploading a file, the content needs to be base64 encoded into the <code translate="no" dir="ltr">content</code> field regardless of the mimetype of the file being uploaded.</p>
<p>Returns a single File object upon successful creation.</p>
<p>The following Google Drive first-party mime types can be created without providing content:</p>
<ul>
<li><code translate="no" dir="ltr">application/vnd.google-apps.document</code></li>
<li><code translate="no" dir="ltr">application/vnd.google-apps.spreadsheet</code></li>
<li><code translate="no" dir="ltr">application/vnd.google-apps.presentation</code></li>
</ul>
<p>By default, the following conversions will be made for the following mime types:</p>
<ul>
<li><code translate="no" dir="ltr">text/plain</code> to <code translate="no" dir="ltr">application/vnd.google-apps.document</code></li>
<li><code translate="no" dir="ltr">text/csv</code> to <code translate="no" dir="ltr">application/vnd.google-apps.spreadsheet</code></li>
</ul>
<p>To disable conversions for first-party mime types, set <code translate="no" dir="ltr">disable_conversion_to_google_type</code> to true.</p>
<p>Folders can be created by setting the mime type to <code translate="no" dir="ltr">application/vnd.google-apps.folder</code>.</p></td>
</tr>
<tr id="toolsSection.download_file_content">
<td><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content">download_file_content</a></td>
<td><p>Call this tool to download the content of a Drive file as raw binary data (bytes).</p>
<p>If the file is a Google Drive first-party mime type, the <code translate="no" dir="ltr">exportMimeType</code> field is required and will determine the format of the downloaded file.</p>
<p>If the file is not found, try using other tools like <code translate="no" dir="ltr">search_files</code> to find the file the user is requesting.</p>
<p>If the user wants a natural language representation of their Drive content, use the <code translate="no" dir="ltr">read_file_content</code> tool (<code translate="no" dir="ltr">read_file_content</code> should be smaller and easier to parse).</p></td>
</tr>
<tr id="toolsSection.get_file_metadata">
<td><a href="/workspace/drive/api/reference/mcp/tools_list/get_file_metadata">get_file_metadata</a></td>
<td><p>Call this tool to find general metadata about a user's Drive file.</p>
<p>If the file is not found, try using other tools like <code translate="no" dir="ltr">search_files</code> to find the file the user is requesting.</p></td>
</tr>
<tr id="toolsSection.get_file_permissions">
<td><a href="/workspace/drive/api/reference/mcp/tools_list/get_file_permissions">get_file_permissions</a></td>
<td>Call this tool to list the permissions of a Drive File.</td>
</tr>
<tr id="toolsSection.list_recent_files">
<td><a href="/workspace/drive/api/reference/mcp/tools_list/list_recent_files">list_recent_files</a></td>
<td><p>Call this tool to find recent files for a user specified a sort order. Default sort order is <code translate="no" dir="ltr">recency</code>.</p>
<p>Supported sort orders are:</p>
<ul>
<li><code translate="no" dir="ltr">recency</code>: The most recent timestamp from the file's date-time fields.</li>
<li><code translate="no" dir="ltr">lastModified</code>: The last time the file was modified by anyone.</li>
<li><code translate="no" dir="ltr">lastModifiedByMe</code>: The last time the file was modified by the user.</li>
</ul>
<p>The default page size is 10. Utilize <code translate="no" dir="ltr">next_page_token</code> to paginate through the results.</p></td>
</tr>
<tr id="toolsSection.read_file_content">
<td><a href="/workspace/drive/api/reference/mcp/tools_list/read_file_content">read_file_content</a></td>
<td><p>Call this tool to fetch a natural language representation of a Drive file.</p>
<p>The file content may be incomplete for very large files. The text representation will change over time, so don't make assumptions about the particular format of the text returned by this tool.</p>
<p>Supported Mime Types:</p>
<ul>
<li><code translate="no" dir="ltr">application/vnd.google-apps.document</code></li>
<li><code translate="no" dir="ltr">application/vnd.google-apps.presentation</code></li>
<li><code translate="no" dir="ltr">application/vnd.google-apps.spreadsheet</code></li>
<li><code translate="no" dir="ltr">application/pdf</code></li>
<li><code translate="no" dir="ltr">application/msword</code></li>
<li><code translate="no" dir="ltr">application/vnd.openxmlformats-officedocument.wordprocessingml.document</code></li>
<li><code translate="no" dir="ltr">application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</code></li>
<li><code translate="no" dir="ltr">application/vnd.openxmlformats-officedocument.presentationml.presentation</code></li>
<li><code translate="no" dir="ltr">application/vnd.oasis.opendocument.spreadsheet</code></li>
<li><code translate="no" dir="ltr">application/vnd.oasis.opendocument.presentation</code></li>
<li><code translate="no" dir="ltr">application/x-vnd.oasis.opendocument.text</code></li>
<li><code translate="no" dir="ltr">image/png</code></li>
<li><code translate="no" dir="ltr">image/jpeg</code></li>
<li><code translate="no" dir="ltr">image/jpg</code></li>
</ul>
<p>If the file is not found, try using other tools like <code translate="no" dir="ltr">search_files</code> to find the file the user is requesting using keywords.</p></td>
</tr>
<tr id="toolsSection.search_files">
<td><a href="/workspace/drive/api/reference/mcp/tools_list/search_files">search_files</a></td>
<td><p>Call this tool to search for Drive files given a structured query.</p>
<p>The <code translate="no" dir="ltr">query</code> field requires the use of query search operators.</p>
<p>A query string contains the following three parts: <code translate="no" dir="ltr">query_term operator values</code> where:</p>
<ul>
<li><code translate="no" dir="ltr">query_term</code> is the query term or field to search upon.</li>
<li><code translate="no" dir="ltr">operator</code> specifies the condition for the query term.</li>
<li><code translate="no" dir="ltr">values</code> are the specific values to use to filter your search results.</li>
</ul>
<h2 id="query-terms" data-text="Query Terms" tabindex="-1">Query Terms</h2>
<p>The following table lists valid query terms with their descriptions:</p>
<table>
<thead>
<tr>
<th>Query Term</th>
<th>Valid operators</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><code translate="no" dir="ltr">title</code></td>
<td><code translate="no" dir="ltr">contains</code>, <code translate="no" dir="ltr">=</code>, <code translate="no" dir="ltr">!=</code></td>
<td>Title of the file. Surround with single quotes (<code translate="no" dir="ltr">'</code>). Escape single quotes in queries with <code translate="no" dir="ltr">\'</code>, such as <code translate="no" dir="ltr">'Valentine\'s Day'</code>.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">fullText</code></td>
<td><code translate="no" dir="ltr">contains</code></td>
<td>Whether the <code translate="no" dir="ltr">title</code> or text in the file's content matches. Surround with single quotes (<code translate="no" dir="ltr">'</code>). Escape single quotes in queries with <code translate="no" dir="ltr">\'</code>, such as <code translate="no" dir="ltr">'Valentine\'s Day'</code>.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">mimeType</code></td>
<td><code translate="no" dir="ltr">contains</code>, <code translate="no" dir="ltr">=</code>, <code translate="no" dir="ltr">!=</code></td>
<td>MIME type of the file. Surround with single quotes (<code translate="no" dir="ltr">'</code>). Escape single quotes in queries with <code translate="no" dir="ltr">\'</code>, such as <code translate="no" dir="ltr">'Valentine\'s Day'</code>.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">modifiedTime</code></td>
<td><code translate="no" dir="ltr">&lt;=</code>, <code translate="no" dir="ltr">&lt;</code>, <code translate="no" dir="ltr">=</code>, <code translate="no" dir="ltr">!=</code>, <code translate="no" dir="ltr">&gt;</code>, <code translate="no" dir="ltr">&gt;=</code></td>
<td>Date of the last file modification. RFC 3339 format, default time zone is UTC, such as <code translate="no" dir="ltr">2012-06-04T12:00:00-08:00</code>. Fields of type <code translate="no" dir="ltr">date</code> are not comparable.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">viewedByMeTime</code></td>
<td><code translate="no" dir="ltr">&lt;=</code>, <code translate="no" dir="ltr">&lt;</code>, <code translate="no" dir="ltr">=</code>, <code translate="no" dir="ltr">!=</code>, <code translate="no" dir="ltr">&gt;</code>, <code translate="no" dir="ltr">&gt;=</code></td>
<td>Date that the user last viewed a file. RFC 3339 format, default time zone is UTC, such as <code translate="no" dir="ltr">2012-06-04T12:00:00-08:00</code>. Fields of type <code translate="no" dir="ltr">date</code> are not comparable.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">parentId</code></td>
<td><code translate="no" dir="ltr">=</code>, <code translate="no" dir="ltr">!=</code></td>
<td>Whether the parent equals the specified ID. <code translate="no" dir="ltr">root</code> can be used to specify the user's "My Drive" that functions as their primary hierarchy.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">owner</code></td>
<td><code translate="no" dir="ltr">=</code>, <code translate="no" dir="ltr">!=</code></td>
<td>User who owns the file. <code translate="no" dir="ltr">me</code> can be used to specify the user that is making the request.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">sharedWithMe</code></td>
<td><code translate="no" dir="ltr">=</code>, <code translate="no" dir="ltr">!=</code></td>
<td>Files that are in the user's "Shared with me" collection. All file users are in the file's Access Control List (ACL). Can be either <code translate="no" dir="ltr">true</code> or <code translate="no" dir="ltr">false</code>.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">createdTime</code></td>
<td><code translate="no" dir="ltr">&lt;=</code>, <code translate="no" dir="ltr">&lt;</code>, <code translate="no" dir="ltr">=</code>, <code translate="no" dir="ltr">!=</code>, <code translate="no" dir="ltr">&gt;</code>, <code translate="no" dir="ltr">&gt;=</code></td>
<td>Date when the file was created. Use RFC 3339 format, default time zone is UTC, such as <code translate="no" dir="ltr">2012-06-04T12:00:00-08:00</code>.</td>
</tr>
</tbody>
</table>
<h2 id="query-operators" data-text="Query Operators" tabindex="-1">Query Operators</h2>
<p>The following table lists valid query operators:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><code translate="no" dir="ltr">contains</code></td>
<td>The content of one string is present in the other.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">=</code></td>
<td>The content of a string or boolean is equal to the other.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">!=</code></td>
<td>The content of a string or boolean is not equal to the other.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">&lt;</code></td>
<td>A value is less than another.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">&lt;=</code></td>
<td>A value is less than or equal to another.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">&gt;</code></td>
<td>A value is greater than another.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">&gt;=</code></td>
<td>A value is greater than or equal to another.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">in</code></td>
<td>An element is contained within a collection.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">and</code></td>
<td>Return items that match both queries.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">or</code></td>
<td>Return items that match either query.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">not</code></td>
<td>Negates a search query.</td>
</tr>
<tr>
<td><code translate="no" dir="ltr">has</code></td>
<td>A collection contains an element matching the parameters.</td>
</tr>
</tbody>
</table>
<p>Some examples of queries include:</p>
<ul>
<li><code translate="no" dir="ltr">title contains 'hello' and title contains 'goodbye'</code></li>
<li><code translate="no" dir="ltr">modifiedTime &gt; '2024-01-01T00:00:00Z' and (mimeType contains 'image/' or mimeType contains 'video/')</code></li>
<li><code translate="no" dir="ltr">parentId = '1234567'</code></li>
<li><code translate="no" dir="ltr">fullText contains 'hello'</code></li>
<li><code translate="no" dir="ltr">owner = 'test@example.org'</code></li>
<li><code translate="no" dir="ltr">sharedWithMe = true</code></li>
<li><code translate="no" dir="ltr">owner = 'me'</code> (for files owned by the user)</li>
</ul>
<p>Utilize <code translate="no" dir="ltr">next_page_token</code> to paginate through the results. An empty response indicates that there are either no results or no more results to return.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="tools_overview" class="section">

<div id="tools_overview.GENERIC" class="section">

### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server.

<div id="tools_overview.GENERIC.MCP_CURL_REQUEST" class="section">

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
<pre class="devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded="" data-syntax="Bash"><code>curl --location &#39;https://drivemcp.googleapis.com/mcp/v1&#39; \
--header &#39;content-type: application/json&#39; \
--header &#39;accept: application/json, text/event-stream&#39; \
--data &#39;{
    &quot;method&quot;: &quot;tools/list&quot;,
    &quot;jsonrpc&quot;: &quot;2.0&quot;,
    &quot;id&quot;: 1
}&#39;
                    </code></pre></td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

</div>

</div>

Send feedback

<div class="devsite-floating-action-buttons">

</div>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-04-23 UTC."\],\[\],\[\]\]

</div>

</div>
