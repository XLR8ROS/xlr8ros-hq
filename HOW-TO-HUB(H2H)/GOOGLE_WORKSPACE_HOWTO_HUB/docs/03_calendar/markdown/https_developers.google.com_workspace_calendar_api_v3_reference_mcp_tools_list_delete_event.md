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

<div id="/workspace/calendar/api/v3/reference/mcp/tools_list/delete_event" class="section">

<div id="GENERIC" class="section">

## Tool: `delete_event`

</div>

<div id="GENERIC_1" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Deletes a calendar event.

Use this tool for queries like:

- Delete the event with id event123 on my calendar.

To cancel or decline an event, use the respond_to_event tool instead.

Example:

<div>

</div>

```
delete_event(
            eventId='event123'
        )
        # Deletes the event with id 'event123' on the user's primary calendar.
        
```

</div>

<div id="GENERIC_2" class="section">

The following sample demonstrate how to use `curl` to invoke the `delete_event` MCP tool.

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
    &quot;name&quot;: &quot;delete_event&quot;,
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

Request message for DeleteEvent.

</div>

<div id="Input.Schema.DeleteEventRequest" class="section">

### DeleteEventRequest

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
  &quot;eventId&quot;: string,
&#10;  &quot;calendarId&quot;: string
&#10;  &quot;notificationLevel&quot;: enum (NotificationLevel)
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
<td><code translate="no" dir="ltr">eventId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. The ID of the event to delete.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_calendar_id</code>.</p>
<p><code translate="no" dir="ltr">_calendar_id</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">calendarId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Optional. The calendar ID of the event to delete. The default is the user's primary calendar.</p></td>
</tr>
<tr id="Input.Schema.FIELDS.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_notification_level</code>.</p>
<p><code translate="no" dir="ltr">_notification_level</code> can be only one of the following:</p></td>
</tr>
<tr id="Input.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">notificationLevel</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">enum (</code><code translate="no" dir="ltr">NotificationLevel</code><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Optional. Which email notification should be sent for this event update. Possible values are:</p>
<ul>
<li><code translate="no" dir="ltr">NONE</code> - No email notifications are sent (default).</li>
<li><code translate="no" dir="ltr">EXTERNAL_ONLY</code> - Only external (non-Calendar) attendees receive email notifications.</li>
<li><code translate="no" dir="ltr">ALL</code> - All event attendees receive email notifications.</li>
</ul></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="Output.Schema" class="section">

## Output Schema

<div id="Output.Schema.description" class="section">

</div>

<div id="Output.Schema.Event" class="section">

### Event

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
  &quot;status&quot;: string,
  &quot;htmlLink&quot;: string,
  &quot;created&quot;: string,
  &quot;updated&quot;: string,
  &quot;summary&quot;: string,
  &quot;description&quot;: string,
  &quot;location&quot;: string,
  &quot;creator&quot;: {
    object (Principal)
  },
  &quot;organizer&quot;: {
    object (Principal)
  },
  &quot;start&quot;: {
    object (DateOrDateTime)
  },
  &quot;end&quot;: {
    object (DateOrDateTime)
  },
  &quot;recurrence&quot;: [
    string
  ],
  &quot;recurringEventId&quot;: string,
  &quot;originalStartTime&quot;: {
    object (DateOrDateTime)
  },
  &quot;transparency&quot;: string,
  &quot;visibility&quot;: string,
  &quot;attendees&quot;: [
    {
      object (Attendee)
    }
  ],
  &quot;eventType&quot;: string,
  &quot;conferenceUrl&quot;: string,
  &quot;colorId&quot;: string,
  &quot;overrideReminders&quot;: [
    {
      object (Reminder)
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
<p>Opaque identifier of the event. When creating new single or recurring events, you can specify their IDs. Provided IDs must follow these rules:</p>
<ul>
<li>characters allowed in the ID are those used in base32hex encoding, i.e. lowercase letters a-v and digits 0-9, see section 3.1.2 in RFC2938</li>
<li>the length of the ID must be between 5 and 1024 characters</li>
<li>the ID must be unique per calendar</li>
</ul>
<p>Due to the globally distributed nature of the system, we cannot guarantee that ID collisions will be detected at event creation time. To minimize the risk of collisions we recommend using an established UUID algorithm such as one described in RFC4122.</p>
<p>If you do not specify an ID, it will be automatically generated by the server.</p>
<p>Note that the icalUID and the id are not identical and only one of them should be supplied at event creation time. One difference in their semantics is that in recurring events, all occurrences of one event have different ids while they all share the same icalUIDs.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_1">
<td><code translate="no" dir="ltr">status</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Status of the event. Optional. Possible values are:</p>
<ul>
<li><code translate="no" dir="ltr">confirmed</code> - The event is confirmed. This is the default status.</li>
<li><code translate="no" dir="ltr">tentative</code> - The event is tentatively confirmed.</li>
<li><code translate="no" dir="ltr">cancelled</code> - The event is cancelled (deleted). The list method returns cancelled events only on incremental sync (when syncToken or updatedMin are specified) or if the showDeleted flag is set to true. The get method always returns them.</li>
</ul>
<p>A cancelled status represents two different states depending on the event type:</p>
<ol>
<li>Cancelled exceptions of an uncancelled recurring event indicate that this instance should no longer be presented to the user. Clients should store these events for the lifetime of the parent recurring event.Cancelled exceptions are only guaranteed to have values for the id, recurringEventId and originalStartTime fields populated. The other fields might be empty.</li>
<li>All other cancelled events represent deleted events. Clients should remove their locally synced copies. Such cancelled events will eventually disappear, so do not rely on them being available indefinitely. Deleted events are only guaranteed to have the id field populated.</li>
</ol>
<p>On the organizer's calendar, cancelled events continue to expose event details (summary, location, etc.) so that they can be restored (undeleted). Similarly, the events to which the user was invited and that they manually removed continue to provide details. However, incremental sync requests with showDeleted set to false will not return these details.</p>
<p>If an event changes its organizer (for example via the move operation) and the original organizer is not on the attendee list, it will leave behind a cancelled event where only the id field is guaranteed to be populated.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_2">
<td><code translate="no" dir="ltr">htmlLink</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>An absolute link to this event in the Google Calendar Web UI. Read-only.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_3">
<td><code translate="no" dir="ltr">created</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Creation time of the event (as a ISO 8601 formatted timestamp). Read-only.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_4">
<td><code translate="no" dir="ltr">updated</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Last modification time of the main event data (as a ISO 8601 formatted timestamp). Updating event reminders will not cause this to change. Read-only.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_5">
<td><code translate="no" dir="ltr">summary</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Title of the event.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_6">
<td><code translate="no" dir="ltr">description</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Description of the event. Can contain HTML. Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_7">
<td><code translate="no" dir="ltr">location</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Geographic location of the event as free-form text. Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_8">
<td><code translate="no" dir="ltr">creator</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_events#Output.Schema.Principal"><code translate="no" dir="ltr">Principal</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The creator of the event. Read-only.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_9">
<td><code translate="no" dir="ltr">organizer</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_events#Output.Schema.Principal"><code translate="no" dir="ltr">Principal</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The organizer of the event. If the organizer is also an attendee, this is indicated with a separate entry in attendees with the organizer field set to True. Read-only.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_10">
<td><code translate="no" dir="ltr">start</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_events#Output.Schema.DateOrDateTime"><code translate="no" dir="ltr">DateOrDateTime</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The (inclusive) start time of the event. For a recurring event, this is the start time of the first instance.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_11">
<td><code translate="no" dir="ltr">end</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_events#Output.Schema.DateOrDateTime"><code translate="no" dir="ltr">DateOrDateTime</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The (exclusive) end time of the event. For a recurring event, this is the end time of the first instance.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_12">
<td><code translate="no" dir="ltr">recurrence[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>List of RRULE, EXRULE, RDATE and EXDATE lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_13">
<td><code translate="no" dir="ltr">recurringEventId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>For an instance of a recurring event, this is the id of the recurring event to which this instance belongs. Immutable.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_14">
<td><code translate="no" dir="ltr">originalStartTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_events#Output.Schema.DateOrDateTime"><code translate="no" dir="ltr">DateOrDateTime</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>For an instance of a recurring event, this is the time at which this event would start according to the recurrence data in the recurring event identified by recurringEventId. It uniquely identifies the instance within the recurring event series even if the instance was moved to a different time. Immutable.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_15">
<td><code translate="no" dir="ltr">transparency</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Whether the event blocks time on the calendar. Optional. Possible values are:</p>
<ul>
<li><code translate="no" dir="ltr">opaque</code> - Default value. The event does block time on the calendar. This is equivalent to setting Show me as to Busy in the Calendar UI.</li>
<li><code translate="no" dir="ltr">transparent</code> - The event does not block time on the calendar. This is equivalent to setting Show me as to Available in the Calendar UI.</li>
</ul></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_16">
<td><code translate="no" dir="ltr">visibility</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Visibility of the event. Optional. Possible values are:</p>
<ul>
<li><code translate="no" dir="ltr">default</code> - Uses the default visibility for events on the calendar. This is the default value.</li>
<li><code translate="no" dir="ltr">public</code> - The event is public and event details are visible to all readers of the calendar.</li>
<li><code translate="no" dir="ltr">private</code> - The event is private and only event attendees may view event details.</li>
<li><code translate="no" dir="ltr">confidential</code> - The event is private. This value is provided for compatibility reasons.</li>
</ul></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_17">
<td><code translate="no" dir="ltr">attendees[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_events#Output.Schema.Attendee"><code translate="no" dir="ltr">Attendee</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>The attendees of the event.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_18">
<td><code translate="no" dir="ltr">eventType</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Specific type of the event. This cannot be modified after the event is created. Possible values are:</p>
<ul>
<li><code translate="no" dir="ltr">birthday</code> - A special all-day event with an annual recurrence.</li>
<li><code translate="no" dir="ltr">default</code> - A regular event or not further specified.</li>
<li><code translate="no" dir="ltr">focusTime</code> - A focus-time event.</li>
<li><code translate="no" dir="ltr">fromGmail</code> - An event from Gmail. This type of event cannot be created.</li>
<li><code translate="no" dir="ltr">outOfOffice</code> - An out-of-office event.</li>
<li><code translate="no" dir="ltr">workingLocation</code> - A working location event.</li>
</ul></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_19">
<td><code translate="no" dir="ltr">conferenceUrl</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The Google Meet link for the event.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_20">
<td><code translate="no" dir="ltr">colorId</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Event color ID (string <code translate="no" dir="ltr">1</code>-<code translate="no" dir="ltr">11</code>):</p>
<ul>
<li>1: Lavender</li>
<li>2: Sage</li>
<li>3: Grape</li>
<li>4: Flamingo</li>
<li>5: Banana</li>
<li>6: Tangerine</li>
<li>7: Peacock</li>
<li>8: Graphite</li>
<li>9: Blueberry</li>
<li>10: Basil</li>
<li>11: Tomato.</li>
</ul>
<p>In Google Calendar, event colors function as categories — settable per-event or per-series. Users may assign custom labels to colors in the web UI (e.g., <code translate="no" dir="ltr">1:1s</code>, <code translate="no" dir="ltr">Break</code>), but the API only exposes numeric IDs, not those labels. Only affects your own calendar view — each attendee controls their own event color.</p></td>
</tr>
<tr id="Output.Schema.FIELDS.field_section_21">
<td><code translate="no" dir="ltr">overrideReminders[]</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">object (</code><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_events#Output.Schema.Reminder"><code translate="no" dir="ltr">Reminder</code></a><code class="apitype" translate="no" dir="ltr">)</code></p>
<p>Reminders defined for this event, overriding the default reminders for the calendar. If not set, the default reminders on the calendar are used.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Principal" class="section">

### Principal

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
  &quot;email&quot;: string,
  &quot;displayName&quot;: string,
  &quot;self&quot;: boolean
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
<td><code translate="no" dir="ltr">email</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Email address of the principal (calendar).</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_1">
<td><code translate="no" dir="ltr">displayName</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The principal's name, if available.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_1.field_section_2">
<td><code translate="no" dir="ltr">self</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Whether this principal corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.DateOrDateTime" class="section">

### DateOrDateTime

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
  &quot;date&quot;: string,
  &quot;dateTime&quot;: string,
  &quot;timeZone&quot;: string
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
<td><code translate="no" dir="ltr">date</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>An ISO 8601 formatted date at midnight UTC such as <code translate="no" dir="ltr">2019-11-20T00:00:00Z</code>. If this field is set, <code translate="no" dir="ltr">date_time</code> must not be set.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_1">
<td><code translate="no" dir="ltr">dateTime</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>An ISO 8601 formatted timestamp such as <code translate="no" dir="ltr">2019-11-20T08:19:06-07:00</code> or <code translate="no" dir="ltr">2019-11-20T08:19:06Z</code>. If this field is set, <code translate="no" dir="ltr">date</code> must not be set.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_2.field_section_2">
<td><code translate="no" dir="ltr">timeZone</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>TZDB timezone name if available.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Attendee" class="section">

### Attendee

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
  &quot;id&quot;: string,
  &quot;email&quot;: string,
  &quot;displayName&quot;: string,
  &quot;organizer&quot;: boolean,
  &quot;self&quot;: boolean,
  &quot;resource&quot;: boolean,
  &quot;optionalAttendee&quot;: boolean,
  &quot;responseStatus&quot;: string,
  &quot;comment&quot;: string,
  &quot;additionalGuests&quot;: integer
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
<td><code translate="no" dir="ltr">id</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The attendee's Profile ID, if available.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_1">
<td><code translate="no" dir="ltr">email</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The attendee's email address, if available. This field must be present when adding an attendee. It must be a valid email address as per RFC5322. Required when adding an attendee.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_2">
<td><code translate="no" dir="ltr">displayName</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The attendee's name, if available. Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_3">
<td><code translate="no" dir="ltr">organizer</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Whether the attendee is the organizer of the event. Read-only. The default is False.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_4">
<td><code translate="no" dir="ltr">self</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Whether this entry represents the calendar on which this copy of the event appears. Read-only. The default is False.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_5">
<td><code translate="no" dir="ltr">resource</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Whether the attendee is a resource. Can only be set when the attendee is added to the event for the first time. Subsequent modifications are ignored. Optional. The default is False.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_6">
<td><code translate="no" dir="ltr">optionalAttendee</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">boolean</code></p>
<p>Whether this is an optional attendee. Optional. The default is False.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_7">
<td><code translate="no" dir="ltr">responseStatus</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The attendee's response status. Possible values are:</p>
<ul>
<li><code translate="no" dir="ltr">needsAction</code> - The attendee has not responded to the invitation (recommended for new events).</li>
<li><code translate="no" dir="ltr">declined</code> - The attendee has declined the invitation.</li>
<li><code translate="no" dir="ltr">tentative</code> - The attendee has tentatively accepted the invitation.</li>
<li><code translate="no" dir="ltr">accepted</code> - The attendee has accepted the invitation.</li>
</ul></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_8">
<td><code translate="no" dir="ltr">comment</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>The attendee's response comment. Optional.</p></td>
</tr>
<tr id="Output.Schema.FIELDS_3.field_section_9">
<td><code translate="no" dir="ltr">additionalGuests</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Number of additional guests. Optional. The default is 0.</p></td>
</tr>
</tbody>
</table>

</div>

<div id="Output.Schema.Reminder" class="section">

### Reminder

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
&#10;  &quot;method&quot;: string
&#10;  &quot;minutes&quot;: integer
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
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_method</code>.</p>
<p><code translate="no" dir="ltr">_method</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section">
<td><code translate="no" dir="ltr">method</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">string</code></p>
<p>Required. How the reminder is delivered to the user. Possible values are:</p>
<ul>
<li><code translate="no" dir="ltr">email</code> - Reminders are sent via email.</li>
<li><code translate="no" dir="ltr">popup</code> - Reminders are sent via a UI popup.</li>
</ul></td>
</tr>
<tr id="Output.Schema.FIELDS_4.ONEOF_1" class="alt">
<td colspan="2"><p>Union field <code translate="no" dir="ltr">_minutes</code>.</p>
<p><code translate="no" dir="ltr">_minutes</code> can be only one of the following:</p></td>
</tr>
<tr id="Output.Schema.FIELDS_4.field_section_1">
<td><code translate="no" dir="ltr">minutes</code></td>
<td><p><code class="apitype" translate="no" dir="ltr">integer</code></p>
<p>Required. Number of minutes in advance that the reminder should be delivered.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

<div id="GENERIC_3" class="section">

### Tool Annotations

Destructive Hint: ✅ \| Idempotent Hint: ✅ \| Read Only Hint: ❌ \| Open World Hint: ❌

</div>

</div>

</div>

Send feedback

<div class="devsite-floating-action-buttons">

</div>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-06 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-06 UTC."\],\[\],\[\]\]

</div>

</div>
