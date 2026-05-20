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

<div id="/workspace/drive/api/reference/mcp/tools_list/download_file_content" class="section">

<div id="GENERIC" class="section">

## Tool: `download_file_content`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Call this tool to download the content of a Drive file as raw binary data (bytes).

If the file is a Google Drive first-party mime type, the `exportMimeType` field is required and will determine the format of the downloaded file.

If the file is not found, try using other tools like `search_files` to find the file the user is requesting.

If the user wants a natural language representation of their Drive content, use the `read_file_content` tool (`read_file_content` should be smaller and easier to parse).

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `download_file_content` MCP tool.

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
    &quot;name&quot;: &quot;download_file_content&quot;,
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

Defines a request to download a file's content.

</div>

<div id="Input.Schema.DownloadFileRequest" class="section">

### DownloadFileRequest

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
  &quot;fileId&quot;: string,
  &quot;exportMimeType&quot;: string
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
<p>Required. The ID of the file to retrieve.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">exportMimeType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. For Google native files, the MIME type to export the file to, ignored otherwise. Defaults to text if not specified.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

</div>

<div id="Output.Schema.CallToolResponse" class="section">

### CallToolResponse

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
  &quot;common&quot;: {
    object (ResponseFields)
  },
  &quot;content&quot;: [
    {
      object (Content)
    }
  ],
  &quot;structuredContent&quot;: {
    object
  },
  &quot;isError&quot;: boolean
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
<td><code translate="no" dir="ltr">common</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ResponseFields"><code translate="no" dir="ltr">ResponseFields</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">content[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.Content"><code translate="no" dir="ltr">Content</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">structuredContent</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#struct"><code translate="no" dir="ltr">Struct</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>If the tool defines an output schema, this field will be populated. Clients that support structured output should ignore the content field above if this field is set.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">isError</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Optional.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ResponseFields" class="section">

### ResponseFields

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
  &quot;instructions&quot;: string,
  &quot;metadata&quot;: {
    object
  },
  &quot;dependentRequests&quot;: {
    string: {
      object (ServerInitiatedRequest)
    },
    ...
  },
  &quot;resumeData&quot;: {
    object
  }
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
<td><code translate="no" dir="ltr">instructions</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. Sent only on the initial response on any RPC.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">metadata</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#struct"><code translate="no" dir="ltr">Struct</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>Escape hatch for arbitrary side-channel data.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">dependentRequests</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">map (key: string, value: object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ServerInitiatedRequest"><code translate="no" dir="ltr">ServerInitiatedRequest</code></a><code class="apitype" translate="no" dir="ltr">))</code></p>
<p>Dependent requests. The presence of this field tells the client that the request is incomplete and that the client must try its request again with the result of these dependent requests in the dependent_responses field.</p>
<p>An object containing a list of <code translate="no" dir="ltr">"key": value</code> pairs. Example: <code translate="no" dir="ltr">{ "name": "wrench", "mass": "1.3kg", "count": "3" }</code>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_3">
<td><code translate="no" dir="ltr">resumeData</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#struct"><code translate="no" dir="ltr">Struct</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>State for the client to echo back in subsequent RPCs for the same peristant request.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Struct" class="section">

### Struct

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
  &quot;fields&quot;: {
    string: value,
    ...
  }
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
<td><code translate="no" dir="ltr">fields</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">map (key: string, value: value (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#value"><code translate="no" dir="ltr">Value</code></a><code class="apitype" translate="no" dir="ltr"> format))</code></p>
<p>Unordered map of dynamically typed values.</p>
<p>An object containing a list of <code translate="no" dir="ltr">"key": value</code> pairs. Example: <code translate="no" dir="ltr">{ "name": "wrench", "mass": "1.3kg", "count": "3" }</code>.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FieldsEntry" class="section">

### FieldsEntry

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
  &quot;key&quot;: string,
  &quot;value&quot;: value
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
<td><code translate="no" dir="ltr">key</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_1">
<td><code translate="no" dir="ltr">value</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">value (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#value"><code translate="no" dir="ltr">Value</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Value" class="section">

### Value

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
&#10;  &quot;nullValue&quot;: null,
  &quot;numberValue&quot;: number,
  &quot;stringValue&quot;: string,
  &quot;boolValue&quot;: boolean,
  &quot;structValue&quot;: {
    object
  },
  &quot;listValue&quot;: array
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
<tr id="Output.Schema.FIELDS_4.ONEOF" class="alt">
<td colspan="2">Union field <code translate="no" dir="ltr">kind</code>. The kind of value. <code translate="no" dir="ltr">kind</code> can be only one of the following:</td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section">
<td><code translate="no" dir="ltr">nullValue</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">null</code></p>
<p>Represents a JSON <code translate="no" dir="ltr">null</code>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section_1">
<td><code translate="no" dir="ltr">numberValue</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">number</code></p>
<p>Represents a JSON number. Must not be <code translate="no" dir="ltr">NaN</code>, <code translate="no" dir="ltr">Infinity</code> or <code translate="no" dir="ltr">-Infinity</code>, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section_2">
<td><code translate="no" dir="ltr">stringValue</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Represents a JSON string.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section_3">
<td><code translate="no" dir="ltr">boolValue</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Represents a JSON boolean (<code translate="no" dir="ltr">true</code> or <code translate="no" dir="ltr">false</code> literal in JSON).</p></td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section_4">
<td><code translate="no" dir="ltr">structValue</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#struct"><code translate="no" dir="ltr">Struct</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>Represents a JSON object.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section_5">
<td><code translate="no" dir="ltr">listValue</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">array (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#list-value"><code translate="no" dir="ltr">ListValue</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>Represents a JSON array.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ListValue" class="section">

### ListValue

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_5" class="section">

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
  &quot;values&quot;: [
    value
  ]
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_5" class="section">

<table id="Output.Schema.FIELDS_5-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_5.field_section">
<td><code translate="no" dir="ltr">values[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">value (</code><a href="https://protobuf.dev/reference/protobuf/google.protobuf/#value"><code translate="no" dir="ltr">Value</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>Repeated field of dynamically typed values.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.DependentRequestsEntry" class="section">

### DependentRequestsEntry

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_6" class="section">

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
  &quot;key&quot;: string,
  &quot;value&quot;: {
    object (ServerInitiatedRequest)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_6" class="section">

<table id="Output.Schema.FIELDS_6-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_6.field_section">
<td><code translate="no" dir="ltr">key</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_6.field_section_1">
<td><code translate="no" dir="ltr">value</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ServerInitiatedRequest"><code translate="no" dir="ltr">ServerInitiatedRequest</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ServerInitiatedRequest" class="section">

### ServerInitiatedRequest

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_7" class="section">

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
  &quot;samplingCreateMessage&quot;: {
    object (SamplingCreateMessageRequest)
  },
  &quot;listRootsRequest&quot;: {
    object (ListRootsRequest)
  },
  &quot;notifyOnRootListUpdate&quot;: boolean,
  &quot;elicitRequest&quot;: {
    object (ElicitRequest)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_7" class="section">

<table id="Output.Schema.FIELDS_7-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_7.field_section">
<td><code translate="no" dir="ltr">samplingCreateMessage</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.SamplingCreateMessageRequest"><code translate="no" dir="ltr">SamplingCreateMessageRequest</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Sampling, as per <a href="https://modelcontextprotocol.io/specification/2025-03-26/client/sampling">https://modelcontextprotocol.io/specification/2025-03-26/client/sampling</a>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_7.field_section_1">
<td><code translate="no" dir="ltr">listRootsRequest</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><code translate="no" dir="ltr">ListRootsRequest</code><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Root list request, as per <a href="https://modelcontextprotocol.io/specification/2025-03-26/client/roots">https://modelcontextprotocol.io/specification/2025-03-26/client/roots</a>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_7.field_section_2">
<td><code translate="no" dir="ltr">notifyOnRootListUpdate</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_7.field_section_3">
<td><code translate="no" dir="ltr">elicitRequest</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ElicitRequest"><code translate="no" dir="ltr">ElicitRequest</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Elicitations, as per <a href="https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation">https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation</a>.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.SamplingCreateMessageRequest" class="section">

### SamplingCreateMessageRequest

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_8" class="section">

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
  &quot;messages&quot;: [
    {
      object (SamplingMessage)
    }
  ],
  &quot;modelPreferences&quot;: {
    object (ModelPreferences)
  },
  &quot;systemPrompt&quot;: string,
  &quot;includeContext&quot;: enum (IncludeContext),
  &quot;temperature&quot;: number,
  &quot;maxTokens&quot;: integer,
  &quot;stopSequence&quot;: [
    string
  ]
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_8" class="section">

<table id="Output.Schema.FIELDS_8-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_8.field_section">
<td><code translate="no" dir="ltr">messages[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.SamplingMessage"><code translate="no" dir="ltr">SamplingMessage</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_8.field_section_1">
<td><code translate="no" dir="ltr">modelPreferences</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ModelPreferences"><code translate="no" dir="ltr">ModelPreferences</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_8.field_section_2">
<td><code translate="no" dir="ltr">systemPrompt</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_8.field_section_3">
<td><code translate="no" dir="ltr">includeContext</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><code translate="no" dir="ltr">IncludeContext</code><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_8.field_section_4">
<td><code translate="no" dir="ltr">temperature</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">number</code></p>
<p>Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_8.field_section_5">
<td><code translate="no" dir="ltr">maxTokens</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_8.field_section_6">
<td><code translate="no" dir="ltr">stopSequence[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.SamplingMessage" class="section">

### SamplingMessage

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_9" class="section">

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
  &quot;role&quot;: enum (Role),
  &quot;text&quot;: {
    object (TextContent)
  },
  &quot;image&quot;: {
    object (ImageContent)
  },
  &quot;audio&quot;: {
    object (AudioContent)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_9" class="section">

<table id="Output.Schema.FIELDS_9-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_9.field_section">
<td><code translate="no" dir="ltr">role</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><code translate="no" dir="ltr">Role</code><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Which role is sending the message.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_9.field_section_1">
<td><code translate="no" dir="ltr">text</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.TextContent"><code translate="no" dir="ltr">TextContent</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Exactly one of these fields must be populated. (Not using "oneof", since that causes forward-compatibility problems.)</p></td>
</tr>
<tr id="Output.Schema.FIELDS_9.field_section_2">
<td><code translate="no" dir="ltr">image</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ImageContent"><code translate="no" dir="ltr">ImageContent</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_9.field_section_3">
<td><code translate="no" dir="ltr">audio</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.AudioContent"><code translate="no" dir="ltr">AudioContent</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.TextContent" class="section">

### TextContent

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_10" class="section">

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
  &quot;text&quot;: string,
  &quot;annotations&quot;: {
    object (Annotations)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_10" class="section">

<table id="Output.Schema.FIELDS_10-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_10.field_section">
<td><code translate="no" dir="ltr">text</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_10.field_section_1">
<td><code translate="no" dir="ltr">annotations</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.Annotations"><code translate="no" dir="ltr">Annotations</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Annotations" class="section">

### Annotations

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_11" class="section">

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
  &quot;audience&quot;: [
    enum (Role)
  ],
  &quot;priority&quot;: number
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_11" class="section">

<table id="Output.Schema.FIELDS_11-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_11.field_section">
<td><code translate="no" dir="ltr">audience[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><code translate="no" dir="ltr">Role</code><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_11.field_section_1">
<td><code translate="no" dir="ltr">priority</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">number</code></p>
<p>Must be in range [0,1].</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ImageContent" class="section">

### ImageContent

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_12" class="section">

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
  &quot;data&quot;: string,
  &quot;mimeType&quot;: string,
  &quot;annotations&quot;: {
    object (Annotations)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_12" class="section">

<table id="Output.Schema.FIELDS_12-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_12.field_section">
<td><code translate="no" dir="ltr">data</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://developers.google.com/discovery/v1/type-format"><code class="apitype" translate="no" dir="ltr">bytes</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>A base64-encoded string.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_12.field_section_1">
<td><code translate="no" dir="ltr">mimeType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_12.field_section_2">
<td><code translate="no" dir="ltr">annotations</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.Annotations"><code translate="no" dir="ltr">Annotations</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.AudioContent" class="section">

### AudioContent

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_13" class="section">

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
  &quot;data&quot;: string,
  &quot;mimeType&quot;: string,
  &quot;annotations&quot;: {
    object (Annotations)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_13" class="section">

<table id="Output.Schema.FIELDS_13-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_13.field_section">
<td><code translate="no" dir="ltr">data</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://developers.google.com/discovery/v1/type-format"><code class="apitype" translate="no" dir="ltr">bytes</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>A base64-encoded string.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_13.field_section_1">
<td><code translate="no" dir="ltr">mimeType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_13.field_section_2">
<td><code translate="no" dir="ltr">annotations</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.Annotations"><code translate="no" dir="ltr">Annotations</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ModelPreferences" class="section">

### ModelPreferences

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_14" class="section">

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
  &quot;hints&quot;: [
    {
      object (ModelHint)
    }
  ],
  &quot;intelligencePriority&quot;: number,
  &quot;speedPriority&quot;: number,
  &quot;costPriority&quot;: number
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_14" class="section">

<table id="Output.Schema.FIELDS_14-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_14.field_section">
<td><code translate="no" dir="ltr">hints[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ModelHint"><code translate="no" dir="ltr">ModelHint</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_14.field_section_1">
<td><code translate="no" dir="ltr">intelligencePriority</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">number</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_14.field_section_2">
<td><code translate="no" dir="ltr">speedPriority</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">number</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_14.field_section_3">
<td><code translate="no" dir="ltr">costPriority</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">number</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ModelHint" class="section">

### ModelHint

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_15" class="section">

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
  &quot;name&quot;: string
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_15" class="section">

<table id="Output.Schema.FIELDS_15-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_15.field_section">
<td><code translate="no" dir="ltr">name</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ElicitRequest" class="section">

### ElicitRequest

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_16" class="section">

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
  &quot;message&quot;: string,
  &quot;requestedSchema&quot;: {
    string: {
      object (PrimitiveSchemaDefinition)
    },
    ...
  },
  &quot;requiredFields&quot;: [
    string
  ]
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_16" class="section">

<table id="Output.Schema.FIELDS_16-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_16.field_section">
<td><code translate="no" dir="ltr">message</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Message to present to user. Required.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_16.field_section_1">
<td><code translate="no" dir="ltr">requestedSchema</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">map (key: string, value: object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.PrimitiveSchemaDefinition"><code translate="no" dir="ltr">PrimitiveSchemaDefinition</code></a><code class="apitype" translate="no" dir="ltr">))</code></p>
<p>An object containing a list of <code translate="no" dir="ltr">"key": value</code> pairs. Example: <code translate="no" dir="ltr">{ "name": "wrench", "mass": "1.3kg", "count": "3" }</code>.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_16.field_section_2">
<td><code translate="no" dir="ltr">requiredFields[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.RequestedSchemaEntry" class="section">

### RequestedSchemaEntry

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_17" class="section">

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
  &quot;key&quot;: string,
  &quot;value&quot;: {
    object (PrimitiveSchemaDefinition)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_17" class="section">

<table id="Output.Schema.FIELDS_17-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_17.field_section">
<td><code translate="no" dir="ltr">key</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_17.field_section_1">
<td><code translate="no" dir="ltr">value</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.PrimitiveSchemaDefinition"><code translate="no" dir="ltr">PrimitiveSchemaDefinition</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.PrimitiveSchemaDefinition" class="section">

### PrimitiveSchemaDefinition

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_18" class="section">

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
  &quot;stringSchema&quot;: {
    object (StringSchema)
  },
  &quot;numberSchema&quot;: {
    object (NumberSchema)
  },
  &quot;booleanSchema&quot;: {
    object (BooleanSchema)
  },
  &quot;enumSchema&quot;: {
    object (EnumSchema)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_18" class="section">

<table id="Output.Schema.FIELDS_18-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_18.field_section">
<td><code translate="no" dir="ltr">stringSchema</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.StringSchema"><code translate="no" dir="ltr">StringSchema</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Exactly one of these fields will be present. (Not using "oneof", since that causes forward-compatibility problems.)</p></td>
</tr>
<tr id="Output.Schema.FIELDS_18.field_section_1">
<td><code translate="no" dir="ltr">numberSchema</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.NumberSchema"><code translate="no" dir="ltr">NumberSchema</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_18.field_section_2">
<td><code translate="no" dir="ltr">booleanSchema</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.BooleanSchema"><code translate="no" dir="ltr">BooleanSchema</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_18.field_section_3">
<td><code translate="no" dir="ltr">enumSchema</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.EnumSchema"><code translate="no" dir="ltr">EnumSchema</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.StringSchema" class="section">

### StringSchema

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_19" class="section">

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
  &quot;title&quot;: string,
  &quot;description&quot;: string,
  &quot;minLength&quot;: string,
  &quot;maxLength&quot;: string,
  &quot;format&quot;: enum (Format)
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_19" class="section">

<table id="Output.Schema.FIELDS_19-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_19.field_section">
<td><code translate="no" dir="ltr">title</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_19.field_section_1">
<td><code translate="no" dir="ltr">description</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_19.field_section_2">
<td><code translate="no" dir="ltr">minLength</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_19.field_section_3">
<td><code translate="no" dir="ltr">maxLength</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_19.field_section_4">
<td><code translate="no" dir="ltr">format</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><code translate="no" dir="ltr">Format</code><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.NumberSchema" class="section">

### NumberSchema

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_20" class="section">

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
  &quot;title&quot;: string,
  &quot;description&quot;: string,
  &quot;minimum&quot;: string,
  &quot;maximum&quot;: string
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_20" class="section">

<table id="Output.Schema.FIELDS_20-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_20.field_section">
<td><code translate="no" dir="ltr">title</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_20.field_section_1">
<td><code translate="no" dir="ltr">description</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_20.field_section_2">
<td><code translate="no" dir="ltr">minimum</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_20.field_section_3">
<td><code translate="no" dir="ltr">maximum</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.BooleanSchema" class="section">

### BooleanSchema

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_21" class="section">

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
  &quot;title&quot;: string,
  &quot;description&quot;: string,
  &quot;default&quot;: boolean
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_21" class="section">

<table id="Output.Schema.FIELDS_21-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_21.field_section">
<td><code translate="no" dir="ltr">title</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_21.field_section_1">
<td><code translate="no" dir="ltr">description</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_21.field_section_2">
<td><code translate="no" dir="ltr">default</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.EnumSchema" class="section">

### EnumSchema

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_22" class="section">

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
  &quot;title&quot;: string,
  &quot;description&quot;: string,
  &quot;enumList&quot;: [
    string
  ],
  &quot;enumNames&quot;: [
    string
  ]
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_22" class="section">

<table id="Output.Schema.FIELDS_22-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_22.field_section">
<td><code translate="no" dir="ltr">title</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_22.field_section_1">
<td><code translate="no" dir="ltr">description</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_22.field_section_2">
<td><code translate="no" dir="ltr">enumList[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_22.field_section_3">
<td><code translate="no" dir="ltr">enumNames[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Content" class="section">

### Content

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_23" class="section">

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
  &quot;text&quot;: {
    object (TextContent)
  },
  &quot;image&quot;: {
    object (ImageContent)
  },
  &quot;audio&quot;: {
    object (AudioContent)
  },
  &quot;embeddedResource&quot;: {
    object (EmbeddedResource)
  },
  &quot;resourceLink&quot;: {
    object (Resource)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_23" class="section">

<table id="Output.Schema.FIELDS_23-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_23.field_section">
<td><code translate="no" dir="ltr">text</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.TextContent"><code translate="no" dir="ltr">TextContent</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Unstructured result contents. At least one will be populated if the tool does not define an output schema. If the tool does define an output schema, the structured_content field will be populated instead, but one of these fields may still be populated for backward compatibility.</p>
<p>No more than one of these fields must be populated. (Not using "oneof", since that causes forward-compatibility problems.)</p></td>
</tr>
<tr id="Output.Schema.FIELDS_23.field_section_1">
<td><code translate="no" dir="ltr">image</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ImageContent"><code translate="no" dir="ltr">ImageContent</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_23.field_section_2">
<td><code translate="no" dir="ltr">audio</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.AudioContent"><code translate="no" dir="ltr">AudioContent</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_23.field_section_3">
<td><code translate="no" dir="ltr">embeddedResource</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.EmbeddedResource"><code translate="no" dir="ltr">EmbeddedResource</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_23.field_section_4">
<td><code translate="no" dir="ltr">resourceLink</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.Resource"><code translate="no" dir="ltr">Resource</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.EmbeddedResource" class="section">

### EmbeddedResource

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_24" class="section">

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
  &quot;contents&quot;: {
    object (ResourceContents)
  },
  &quot;annotations&quot;: {
    object (Annotations)
  }
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_24" class="section">

<table id="Output.Schema.FIELDS_24-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_24.field_section">
<td><code translate="no" dir="ltr">contents</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.ResourceContents"><code translate="no" dir="ltr">ResourceContents</code></a><code class="apitype" translate="no" dir="ltr">)</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_24.field_section_1">
<td><code translate="no" dir="ltr">annotations</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.Annotations"><code translate="no" dir="ltr">Annotations</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.ResourceContents" class="section">

### ResourceContents

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_25" class="section">

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
  &quot;uri&quot;: string,
  &quot;mimeType&quot;: string,
  &quot;text&quot;: string,
  &quot;blob&quot;: string
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_25" class="section">

<table id="Output.Schema.FIELDS_25-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_25.field_section">
<td><code translate="no" dir="ltr">uri</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_25.field_section_1">
<td><code translate="no" dir="ltr">mimeType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_25.field_section_2">
<td><code translate="no" dir="ltr">text</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Exactly one of these fields must be populated. (Not using "oneof", since that causes forward-compatibility problems.)</p></td>
</tr>
<tr id="Output.Schema.FIELDS_25.field_section_3">
<td><code translate="no" dir="ltr">blob</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string (</code><a href="https://developers.google.com/discovery/v1/type-format"><code class="apitype" translate="no" dir="ltr">bytes</code></a><code class="apitype" translate="no" dir="ltr"> format)</code></p>
<p>A base64-encoded string.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Resource" class="section">

### Resource

</div>

<div id="Output.Schema.SCHEMA_REPRESENTATION_26" class="section">

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
  &quot;uri&quot;: string,
  &quot;name&quot;: string,
  &quot;title&quot;: string,
  &quot;description&quot;: string,
  &quot;mimeType&quot;: string,
  &quot;annotations&quot;: {
    object (Annotations)
  },
  &quot;size&quot;: string
}</code></pre></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.FIELDS_26" class="section">

<table id="Output.Schema.FIELDS_26-table" class="properties responsive fixed" style="width:25%;">
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
<tr id="Output.Schema.FIELDS_26.field_section">
<td><code translate="no" dir="ltr">uri</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_26.field_section_1">
<td><code translate="no" dir="ltr">name</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_26.field_section_2">
<td><code translate="no" dir="ltr">title</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p></td>
</tr>
<tr id="Output.Schema.FIELDS_26.field_section_3">
<td><code translate="no" dir="ltr">description</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_26.field_section_4">
<td><code translate="no" dir="ltr">mimeType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_26.field_section_5">
<td><code translate="no" dir="ltr">annotations</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/drive/api/reference/mcp/tools_list/download_file_content#Output.Schema.Annotations"><code translate="no" dir="ltr">Annotations</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_26.field_section_6">
<td><code translate="no" dir="ltr">size</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional.</p></td>
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
