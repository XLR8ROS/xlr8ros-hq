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

  <a href="https://developers.google.com/workspace/calendar" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="3" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="3" data-track-metadata-eventdetail="Google Calendar">Google Calendar</a>

- <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true">

  </div>

  <a href="https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="4" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="4" data-track-metadata-eventdetail="">MCP server</a>

</div>

Send feedback

# MCP Tools Reference: calendarmcp.googleapis.com <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

<div id="/workspace/calendar/api/v3/reference/mcp/tools_list/suggest_time" class="section">

<div id="GENERIC" class="section">

## Tool: `suggest_time`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Suggests time periods across one or more calendars. To access the primary calendar, add 'primary' in the attendee_emails field.

Use this tool for queries like:

- When are all of us free for a meeting?
- Find a 30 minute slot where we are both available.
- Check if <jane.doe@google.com> is free on Monday morning.

Example:

<div>

</div>

```
suggest_time(
            attendeeEmails=['joedoe@gmail.com', 'janedoe@gmail.com'],
            startTime='2024-09-10T00:00:00',
            endTime='2024-09-17T00:00:00',
            durationMinutes=60,
            preferences={
                'startHour': '09:00',
                'endHour': '17:00',
                'excludeWeekends': True
            }
        )
        # Returns up to 5 suggested time slots where both users are available for at least one hour between 9:00 AM and 5:00 PM on weekdays from September 10 through September 16, 2024.
        
```

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `suggest_time` MCP tool.

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
<pre class="devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded="" data-syntax="Bash"><code>curl --location &#39;https://calendarmcp.googleapis.com/mcp&#39; \
--header &#39;content-type: application/json&#39; \
--header &#39;accept: application/json, text/event-stream&#39; \
--data &#39;{
  &quot;method&quot;: &quot;tools/call&quot;,
  &quot;params&quot;: {
    &quot;name&quot;: &quot;suggest_time&quot;,
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

Request message for SuggestTime.

</div>

<div id="Input.Schema.SuggestTimeRequest" class="section">

### SuggestTimeRequest

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
  &quot;attendeeEmails&quot;: [
    string
  ],
  &quot;startTime&quot;: string,
  &quot;endTime&quot;: string,
&#10;  &quot;timeZone&quot;: string
&#10;  &quot;durationMinutes&quot;: integer
&#10;  &quot;preferences&quot;: {
    object (Preferences)
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
<td><code translate="no" dir="ltr">attendeeEmails[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The attendee emails to find free time for.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">startTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The start of the interval for the query formatted as per ISO 8601.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">endTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The end of the interval for the query formatted as per ISO 8601.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_time_zone</code>.</p>
<p><code translate="no" dir="ltr">_time_zone</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">timeZone</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. Time zone used for the time values. This field accepts IANA Time Zone database names, e.g., <code translate="no" dir="ltr">America/Los_Angeles</code>. The default is the time zone of the user's primary calendar.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_duration_minutes</code>.</p>
<p><code translate="no" dir="ltr">_duration_minutes</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_4">
<td><code translate="no" dir="ltr">durationMinutes</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Optional. Minimum duration of a free time slot in minutes. The default is 30 minutes.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF_2" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_preferences</code>.</p>
<p><code translate="no" dir="ltr">_preferences</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_5">
<td><code translate="no" dir="ltr">preferences</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/suggest_time#Input.Schema.Preferences"><code translate="no" dir="ltr">Preferences</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The preferences to find suggested time for.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Input.Schema.Preferences" class="section">

### Preferences

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
&#10;  &quot;startHour&quot;: string
&#10;  &quot;endHour&quot;: string
&#10;  &quot;excludeWeekends&quot;: boolean
&#10;  &quot;pageSize&quot;: integer
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
<tr id="Input.Schema.FIELDS_1.ONEOF" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_start_hour</code>.</p>
<p><code translate="no" dir="ltr">_start_hour</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS_1.field_section">
<td><code translate="no" dir="ltr">startHour</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The preferred start hour of day (e.g., <code translate="no" dir="ltr">09:00</code>).</p></td>
</tr>
<tr id="Input.Schema.FIELDS_1.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_end_hour</code>.</p>
<p><code translate="no" dir="ltr">_end_hour</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">endHour</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The preferred end hour of day (e.g., <code translate="no" dir="ltr">17:00</code>).</p></td>
</tr>
<tr id="Input.Schema.FIELDS_1.ONEOF_2" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_exclude_weekends</code>.</p>
<p><code translate="no" dir="ltr">_exclude_weekends</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">excludeWeekends</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Whether to exclude weekends.</p></td>
</tr>
<tr id="Input.Schema.FIELDS_1.ONEOF_3" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_page_size</code>.</p>
<p><code translate="no" dir="ltr">_page_size</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS_1.field_section_3">
<td><code translate="no" dir="ltr">pageSize</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Maximum number of time slots to return. Default is 5.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

Response message for SuggestTime.

</div>

<div id="Output.Schema.SuggestTimeResponse" class="section">

### SuggestTimeResponse

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
  &quot;timeSlots&quot;: [
    {
      object (TimeSlot)
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
<td><code translate="no" dir="ltr">timeSlots[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/suggest_time#Output.Schema.TimeSlot"><code translate="no" dir="ltr">TimeSlot</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>List of suggested time slots.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.TimeSlot" class="section">

### TimeSlot

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
  &quot;startTime&quot;: string,
  &quot;endTime&quot;: string,
  &quot;durationMinutes&quot;: integer
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
<td><code translate="no" dir="ltr">startTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The start time of the free time slot as an ISO 8601 formatted timestamp.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">endTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The end time of the free time slot as an ISO 8601 formatted timestamp.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">durationMinutes</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>The duration of the free time slot in minutes.</p></td>
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

Last updated 2026-04-23 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-04-23 UTC."\],\[\],\[\]\]

</div>

</div>
