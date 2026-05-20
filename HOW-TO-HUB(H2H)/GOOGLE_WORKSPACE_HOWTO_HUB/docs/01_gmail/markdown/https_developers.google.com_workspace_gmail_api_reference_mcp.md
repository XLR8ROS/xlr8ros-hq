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

# MCP Reference: gmailmcp.googleapis.com <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

<div id="/workspace/gmail/api/reference/mcp/index" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

This is an MCP server provided by Gmail API. The server provides tools for developers to build LLM applications on top of Gmail.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [configure the Gmail MCP server](https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

<div id="rest_endpoints">

</div>

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Gmail MCP API MCP server has the following global MCP endpoints:

- https://gmailmcp.googleapis.com/mcp/v1

The Gmail MCP API MCP server offers the following MCP toolset endpoints:

- https://gmailmcp.googleapis.com/mcp/v1

## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world. Toolsets are a group of tools that are useful for a specific task. Using toolsets can help your agent perform better because it decreases the number of tools available to your agent.

### Toolsets

The gmailmcp.googleapis.com MCP server has the following toolsets:

<div id="toolsetsSection" class="section">

<table id="toolsetsSection-table" class="properties fixed">
<colgroup>
<col style="width: 30%" />
<col style="width: 40%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr>
<th colspan="3">MCP Toolsets</th>
</tr>
<tr>
<th>Endpoint</th>
<th>Description</th>
<th>Tools</th>
</tr>
</thead>
<tbody>
<tr id="toolsetsSection.mcp.v1">
<td>/mcp/v1</td>
<td>Toolset for the Gmail MCP Server.</td>
<td><code translate="no" dir="ltr"> </code>
<ul>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/create_draft">create_draft</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/create_label">create_label</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/get_thread">get_thread</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/label_message">label_message</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/label_thread">label_thread</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/list_drafts">list_drafts</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/list_labels">list_labels</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/search_threads">search_threads</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/unlabel_message">unlabel_message</a></li>
<li><a href="/workspace/gmail/api/reference/mcp/tools_list/unlabel_thread">unlabel_thread</a></li>
</ul></td>
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
<pre class="devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded="" data-syntax="Bash"><code>curl --location &#39;https://gmailmcp.googleapis.com/mcp/v1&#39; \
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

Last updated 2026-05-13 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-13 UTC."\],\[\],\[\]\]

</div>

</div>
