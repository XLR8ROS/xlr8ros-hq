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

<div id="/workspace/drive/api/reference/mcp/tools_list/get_file_permissions" class="section">

<div id="GENERIC" class="section">

## Tool: `get_file_permissions`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Call this tool to list the permissions of a Drive File.

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `get_file_permissions` MCP tool.

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
    &quot;name&quot;: &quot;get_file_permissions&quot;,
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

Request to get file permissions.

</div>

<div id="Input.Schema.GetFilePermissionsRequest" class="section">

### GetFilePermissionsRequest

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
  &quot;fileId&quot;: string
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
<td><code translate="no" dir="ltr">fileId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The ID of the file to get permissions for.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Response to get file permissions.

</div>

<div id="Output.Schema.GetFilePermissionsResponse" class="section">

### GetFilePermissionsResponse

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
  &quot;permissions&quot;: [
    {
      object (Permission)
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
<td><code translate="no" dir="ltr">permissions[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/get_file_permissions#Output.Schema.Permission"><code translate="no" dir="ltr">Permission</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The list of permissions.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Permission" class="section">

### Permission

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
&#10;  &quot;role&quot;: string
&#10;  &quot;displayName&quot;: string
&#10;  &quot;type&quot;: string
&#10;  &quot;emailAddress&quot;: string
&#10;  &quot;view&quot;: string
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
<tr id="Output.Schema.FIELDS_1.ONEOF" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_role</code>.</p>
<p><code translate="no" dir="ltr">_role</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section">
<td><code translate="no" dir="ltr">role</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The role of the grantee for the file. The possible roles include: * <code translate="no" dir="ltr">owner</code> * <code translate="no" dir="ltr">organizer</code> * <code translate="no" dir="ltr">fileOrganizer</code> * <code translate="no" dir="ltr">writer</code> * <code translate="no" dir="ltr">commenter</code> * <code translate="no" dir="ltr">reader</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_display_name</code>.</p>
<p><code translate="no" dir="ltr">_display_name</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">displayName</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Output only. The "pretty" name of the value of the permission. The following is a list of examples for each type of permission: * <code translate="no" dir="ltr">user</code> - User's full name, as defined for their Google Account, such as "Dana A." * <code translate="no" dir="ltr">group</code> - Name of the Google Group, such as "The Company Administrators." * <code translate="no" dir="ltr">domain</code> - String domain name, such as "cymbalgroup.com." * <code translate="no" dir="ltr">anyone</code> - No <code translate="no" dir="ltr">displayName</code> is present.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.ONEOF_2" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_type</code>.</p>
<p><code translate="no" dir="ltr">_type</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">type</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The type of the grantee. Supported values include: * <code translate="no" dir="ltr">user</code> * <code translate="no" dir="ltr">group</code> * <code translate="no" dir="ltr">domain</code> * <code translate="no" dir="ltr">anyone</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.ONEOF_3" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_email_address</code>.</p>
<p><code translate="no" dir="ltr">_email_address</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_3">
<td><code translate="no" dir="ltr">emailAddress</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The email address of the user or group to which this permission refers.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.ONEOF_4" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_view</code>.</p>
<p><code translate="no" dir="ltr">_view</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_4">
<td><code translate="no" dir="ltr">view</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Specifies the view to which this permission applies, if any. Supported values include: * <code translate="no" dir="ltr">published</code> * <code translate="no" dir="ltr">metadata</code></p></td>
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

Last updated 2026-04-14 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-04-14 UTC."\],\[\],\[\]\]

</div>

</div>
