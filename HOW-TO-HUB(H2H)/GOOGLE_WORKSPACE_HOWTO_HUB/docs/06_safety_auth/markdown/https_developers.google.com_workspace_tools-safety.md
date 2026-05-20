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

</div>

Send feedback

# Google Workspace standardized model for agent tools and APIs <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

Following the launch of new agent tools like the Google Workspace MCP server, we are introducing a standardized tiering model for Google Workspace APIs, including MCP, to safeguard the ecosystem while fostering innovation. This model provides a predictable path to scale for high-impact applications and protects against unique risks such as API abuse and unintended large-scale data egress. We expect that less than 1% of active developers will need to move beyond the standard usage tier, ensuring the vast majority of our community can continue to build without friction.

- As of May 1, 2026, we are adjusting usage quotas across several Google Workspace product APIs, starting with Gmail API, Google Calendar API, and Google Drive API. These adjustments are designed to more closely align with typical usage patterns for common use cases, ensuring that the platform helps support safety, and privacy that Google Workspace users and customers expect.

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th style="border: 1px solid black">Existing projects using affected APIs between November 2025 and April 2026</th>
  <th style="border: 1px solid black">New projects (without prior use of APIs) from May 1, 2026</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td style="border: 1px solid black">API usage quotas already in place will remain unchanged for at least 60 days.</td>
  <td style="border: 1px solid black">New API usage quotas documented for <a href="/workspace/gmail/api/reference/quota">Gmail API</a>, <a href="/workspace/calendar/api/guides/quota">Calendar API</a>, and <a href="/workspace/drive/api/guides/limits">Drive API</a> will be rolled out over several weeks, applying to any project created from May 1, 2026.</td>
  </tr>
  <tr>
  <td colspan="2" style="border: 1px solid black">Requests to increase quotas can be submitted for approval as per the details for each API.</td>
  </tr>
  <tr>
  <td colspan="2" style="border: 1px solid black">Later in 2026, following 90 days of notice:
  <ul>
  <li>Quota increase requests will require Google Cloud billing to be enabled.</li>
  <li>API usage <em>over</em> standard daily thresholds will generate charges on your Google Cloud bill.</li>
  <li>New standard API quotas will apply unless an increased quota has already been approved and billing is enabled.</li>
  </ul></td>
  </tr>
  </tbody>
  </table>

- More details regarding initial changes to API usage quotas are available for [Gmail API](/workspace/gmail/api/reference/quota), [Calendar API](/workspace/calendar/api/guides/quota), or [Drive API](/workspace/drive/api/guides/limits).

## Coming soon: Faster access for scaled usage to our tools

For developers who will require faster, scaled access we plan to introduce an option for projects to increase their standard usage quotas through a paid option. Projects implementing the Google Workspace APIs will have the ability to increase their project quotas by agreeing to pay for API usage above the standard daily limit. We expect to provide this billable usage quota increase option with added details in the coming months, with 90 days notice.

## Google Workspace developer policy and Google terms

Note that working with Google Workspace APIs is still subject to the [Google Workspace API developer policy](/workspace/workspace-api-user-data-developer-policy) and the [Google APIs Terms of Service](https://developers.google.com/terms). As such, Google may require verification, such as in the form of an audit, of adherence to our user data policies.

## Related topics

- [Configure the Google Workspace MCP servers](/workspace/guides/configure-mcp-servers)
- Blog announcement: [Agent tools and security updates for Google Workspace developers](http://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html).

</div>

Send feedback

<div class="devsite-floating-action-buttons">

</div>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-01 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-01 UTC."\],\[\],\[\]\]

</div>

</div>
