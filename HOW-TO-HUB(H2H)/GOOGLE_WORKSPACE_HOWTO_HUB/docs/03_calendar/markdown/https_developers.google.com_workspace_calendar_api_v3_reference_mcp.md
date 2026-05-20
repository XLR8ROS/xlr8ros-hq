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

# MCP Reference: calendarmcp.googleapis.com <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

<div id="/workspace/calendar/api/v3/reference/mcp/index" class="section">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

This is an MCP server provided by Google Calendar API. The server provides tools for developers to build LLM applications on top of Calendar.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [configure the Calendar MCP server](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

<div id="rest_endpoints">

</div>

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Calendar MCP API has the following global MCP endpoint:

- https://calendarmcp.googleapis.com/mcp/v1

## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The calendarmcp.googleapis.com MCP server has the following tools:

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
<tr id="toolsSection.list_events">
<td><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_events"><code translate="no" dir="ltr">list_events</code></a></td>
<td><p>Lists calendar events in a given calendar satisfying the given conditions.</p>
<p>Key Features:</p>
<ul>
<li>Any Calendar ID, which can be user's primary calendar or others.</li>
<li>Time range filtering.</li>
<li>Retrieves ALL events matching the time constraints.</li>
</ul>
<p>If available, use search_events tool instead for searches on the user's primary calendar if:</p>
<ul>
<li>You are querying for events matching a specific topic, category, or intent (e.g., 'lunch meetings', 'project syncs').</li>
<li>You need to find the (top K) most relevant events rather than all events satisfying the constraints.</li>
<li>You need keyword or semantic search capabilities.</li>
</ul>
<p>Use this tool for queries like:</p>
<ul>
<li>What's on my calendar tomorrow?</li>
<li>What's on my calendar for July 14th 2025?</li>
<li>What are my meetings next week?</li>
<li>Do I have any conflicts this afternoon?</li>
<li><p>What meetings does John have tomorrow?</p></li>
</ul>
<p>Example:</p>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>list_events(
    startTime=&#39;2024-09-17T06:00:00&#39;,
    endTime=&#39;2024-09-17T12:00:00&#39;,
    pageSize=10
)
# Returns up to 10 calendar events between 6:00 AM and 12:00 PM on September 17, 2024 from the user&#39;s primary calendar.</code></pre></td>
</tr>
<tr id="toolsSection.get_event">
<td><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/get_event"><code translate="no" dir="ltr">get_event</code></a></td>
<td><p>Returns a single event from a given calendar.</p>
<p>Use this tool for queries like:</p>
<ul>
<li>Get details for the team meeting.</li>
<li>Show me the event with id event123 on my calendar.</li>
</ul>
<p>Example:</p>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>get_event(
    eventId=&#39;event123&#39;
)
# Returns the event details for the event with id `event123` on the user&#39;s primary calendar.</code></pre></td>
</tr>
<tr id="toolsSection.list_calendars">
<td><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/list_calendars"><code translate="no" dir="ltr">list_calendars</code></a></td>
<td><p>Returns the calendars on the user's calendar list.</p>
<p>Use this tool for queries like:</p>
<ul>
<li>What are all my calendars?</li>
</ul>
<p>Example:</p>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>list_calendars()
# Returns all calendars the authenticated user has access to.</code></pre></td>
</tr>
<tr id="toolsSection.suggest_time">
<td><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/suggest_time"><code translate="no" dir="ltr">suggest_time</code></a></td>
<td><p>Suggests time periods across one or more calendars. To access the primary calendar, add 'primary' in the attendee_emails field.</p>
<p>Use this tool for queries like:</p>
<ul>
<li>When are all of us free for a meeting?</li>
<li>Find a 30 minute slot where we are both available.</li>
<li>Check if <a href="mailto:jane.doe@google.com">jane.doe@google.com</a> is free on Monday morning.</li>
</ul>
<p>Example:</p>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>suggest_time(
    attendeeEmails=[&#39;joedoe@gmail.com&#39;, &#39;janedoe@gmail.com&#39;],
    startTime=&#39;2024-09-10T00:00:00&#39;,
    endTime=&#39;2024-09-17T00:00:00&#39;,
    durationMinutes=60,
    preferences={
        &#39;startHour&#39;: &#39;09:00&#39;,
        &#39;endHour&#39;: &#39;17:00&#39;,
        &#39;excludeWeekends&#39;: True
    }
)
# Returns up to 5 suggested time slots where both users are available for at least one hour between 9:00 AM and 5:00 PM on weekdays from September 10 through September 16, 2024.</code></pre></td>
</tr>
<tr id="toolsSection.create_event">
<td><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/create_event"><code translate="no" dir="ltr">create_event</code></a></td>
<td><p>Creates a calendar event.</p>
<p>Use this tool for queries like:</p>
<ul>
<li>Create an event on my calendar for tomorrow at 2pm called 'Meeting with Jane'.</li>
<li>Schedule a meeting with <a href="mailto:john.doe@google.com">john.doe@google.com</a> next Monday from 10am to 11am.</li>
</ul>
<p>Example:</p>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>create_event(
    summary=&#39;Meeting with Jane&#39;,
    startTime=&#39;2024-09-17T14:00:00&#39;,
    endTime=&#39;2024-09-17T15:00:00&#39;
)
# Creates an event on the primary calendar for September 17, 2024 from 2pm to 3pm called &#39;Meeting with Jane&#39;.</code></pre></td>
</tr>
<tr id="toolsSection.update_event">
<td><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/update_event"><code translate="no" dir="ltr">update_event</code></a></td>
<td><p>Updates a calendar event.</p>
<p>Use this tool for queries like:</p>
<ul>
<li>Update the event 'Meeting with Jane' to be one hour later.</li>
<li>Add <a href="mailto:john.doe@google.com">john.doe@google.com</a> to the meeting tomorrow.</li>
</ul>
<p>Example:</p>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>update_event(
    eventId=&#39;event123&#39;,
    summary=&#39;Meeting with Jane and John&#39;
)
# Updates the summary of event with id &#39;event123&#39; on the primary calendar to &#39;Meeting with Jane and John&#39;.</code></pre></td>
</tr>
<tr id="toolsSection.delete_event">
<td><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/delete_event"><code translate="no" dir="ltr">delete_event</code></a></td>
<td><p>Deletes a calendar event.</p>
<p>Use this tool for queries like:</p>
<ul>
<li>Delete the event with id event123 on my calendar.</li>
</ul>
<p>To cancel or decline an event, use the respond_to_event tool instead.</p>
<p>Example:</p>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>delete_event(
    eventId=&#39;event123&#39;
)
# Deletes the event with id &#39;event123&#39; on the user&#39;s primary calendar.</code></pre></td>
</tr>
<tr id="toolsSection.respond_to_event">
<td><a href="/workspace/calendar/api/v3/reference/mcp/tools_list/respond_to_event"><code translate="no" dir="ltr">respond_to_event</code></a></td>
<td><p>Responds to an event.</p>
<p>Use this tool for queries like:</p>
<ul>
<li>Accept the event with id event123 on my calendar.</li>
<li>Decline the meeting with Jane.</li>
<li>Cancel my next meeting.</li>
<li>Tentatively accept the planing meeting.</li>
</ul>
<p>Example:</p>
<div>
&#10;</div>
<pre translate="no" dir="ltr" data-is-upgraded=""><code>respond_to_event(
    eventId=&#39;event123&#39;,
    responseStatus=&#39;accepted&#39;
)
# Responds with status &#39;accepted&#39; to the event with id &#39;event123&#39; on the user&#39;s primary calendar.</code></pre></td>
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
<pre class="devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded="" data-syntax="Bash"><code>curl --location &#39;https://calendarmcp.googleapis.com/mcp/v1&#39; \
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

Last updated 2026-05-06 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-06 UTC."\],\[\],\[\]\]

</div>

</div>
