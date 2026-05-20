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

  <a href="https://developers.google.com/workspace/guides/get-started" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="3" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="3" data-track-metadata-eventdetail="">Guides</a>

</div>

Send feedback

# Enable Google Workspace APIs <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

<div class="devsite-key-takeaways-panel-header" aria-labelledby="key-takeaways-panel-title" aria-expanded="false" role="button" tabindex="0">

![Spark icon](/_static/images/icons/spark.svg)

<div class="devsite-key-takeaways-panel-title">

## Page Summary

</div>

<span class="material-icons devsite-key-takeaways-panel-toggle-button" aria-hidden="true"></span>

</div>

<div class="devsite-key-takeaways-panel-content">

<span class="material-icons" aria-label="Report Key Takeaways!">outlined_flag</span>

- Before using Google APIs, you must enable them within a Google Cloud project, which can be created if you don't have one.

- You can enable Google APIs through the Google Cloud console by navigating to the Product Library, selecting the desired API, and clicking "Enable".

- Alternatively, use the Google Cloud CLI by running the `gcloud services enable API_SERVICE_ID` command, replacing `API_SERVICE_ID` with the specific API's identifier.

- A comprehensive table lists various Google Workspace APIs along with their corresponding console links and CLI commands for enabling them within your project.

- After enabling the necessary APIs, you should understand the authentication and authorization processes for using Google Workspace APIs.

</div>

Before using Google APIs, you need to turn them on in a Google Cloud project. You can turn on one or more APIs in a single Google Cloud project. If you don't already have a Google Cloud project, see [Create a Cloud project](/workspace/guides/create-project).

To enable an API in your Cloud project:

<div class="section">

### Google Cloud console

1.  In the Google Cloud console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **APIs & Services** <span aria-label="and then">\></span> **Library** <span aria-label="and then">\></span> **Google Workspace**.

    <a href="https://console.cloud.google.com/apis/library/browse?filter=category:gsuite" class="button button-primary" target="console">Go to API Library</a>

2.  Click the API that you want to turn on.

3.  Click **Enable**.

4.  To enable more APIs, repeat these steps.

</div>

<div class="section">

### Google Cloud CLI

1.  Install or open the <a href="https://cloud.google.com/cli" class="external" target="_blank">Google Cloud Command Line Interface (CLI)</a>.

2.  Run the <a href="https://cloud.google.com/sdk/gcloud/reference/services" class="external" target="_blank"><code translate="no" dir="ltr">services enable</code></a> command, specifying which API service to enable.

    <div>

    </div>

    ``` devsite-terminal
    gcloud services enable API_SERVICE_ID
    ```

</div>

## (Optional) Try Google Workspace APIs in experimental apps

If you're experimenting with Google Workspace, use the following shortcut, which enables popular Google Workspace APIs, and creates OAuth credentials that you can use.

If you're developing an app that accesses user information, you must [configure the OAuth consent screen](/workspace/guides/configure-oauth-consent) before releasing your app.

Click this button to select or create a Google Cloud project, and automatically enable the Workspace APIs:

<span class="devsite-api-getstarted-widget button button-primary" henhouse-header-text="Enable the Workspace APIs" henhouse-product-name="Quickstart experiment" henhouse-credential-type="OAUTH" henhouse-client-type="DESKTOP" api-id="admin.googleapis.com" henhouse-extra-api-ids="script.googleapis.com, calendar-json.googleapis.com, chat.googleapis.com, classroom.googleapis.com, docs.googleapis.com, drive.googleapis.com,forms.googleapis.com, gmail.googleapis.com, gsuiteaddons.googleapis.com, keep.googleapis.com, meet.googleapis.com, sheets.googleapis.com, slides.googleapis.com">Enable the Workspace APIs</span>

In resulting dialog, click **Download client configuration** and save `credentials.json` to your working directory.

[See the Google Workspace APIs explorer](/workspace/explore) for a comprehensive list of all the available APIs, and to try specific methods from your browser.

<div>

#### Enabled APIs (click to expand)

The button enables the following APIs:

- Admin SDK API
- Apps Script API
- Calendar API
- Chat API
- Classroom API
- Docs API
- Drive API
- Forms API
- Gmail API
- Google Workspace add-ons API
- Google Keep API
- Meet REST API
- Sheets API
- Slides API

</div>

## Google Workspace APIs

Use the following Google Cloud console links or the [Google Cloud Command Line Interface (CLI)](https://cloud.google.com/cli) to enable specific Google Workspace APIs in your Cloud project.

<div>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody class="list">
<tr>
<td><h3 id="admin-sdk-api" class="add-link" data-text="             Admin SDK API" tabindex="-1"><a href="/workspace/admin">Admin SDK API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=admin.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="admin.googleapis.com">Enable Admin SDK API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable admin.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="alert-center-api" class="add-link" data-text="             Alert Center API" tabindex="-1"><a href="/workspace/admin/alertcenter">Alert Center API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=alertcenter.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="alertcenter.googleapis.com">Enable Alert Center API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable alertcenter.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="apps-script-api" class="add-link" data-text="             Apps Script API" tabindex="-1"><a href="/apps-script">Apps Script API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=script.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="script.googleapis.com">Enable Apps Script API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable script.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="caldav-api" class="add-link" data-text="             CalDAV API" tabindex="-1"><a href="/workspace/calendar/caldav">CalDAV API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=caldav.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="caldav.googleapis.com">Enable CalDAV API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable caldav.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="calendar-api" class="add-link" data-text="             Calendar API" tabindex="-1"><a href="/workspace/calendar">Calendar API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=calendar-json.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="calendar-json.googleapis.com">Enable Calendar API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable calendar-json.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="chat-api" class="add-link" data-text="             Chat API" tabindex="-1"><a href="/chat">Chat API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="chat.googleapis.com">Enable Chat API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable chat.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="classroom-api" class="add-link" data-text="             Classroom API" tabindex="-1"><a href="/workspace/classroom">Classroom API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=classroom.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="classroom.googleapis.com">Enable Classroom API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable classroom.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="cloud-identity-api" class="add-link" data-text="             Cloud Identity API" tabindex="-1"><a href="https://cloud.google.com/identity/docs">Cloud Identity API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=cloudidentity.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="cloudidentity.googleapis.com">Enable Cloud Identity API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable cloudidentity.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="cloud-search-api" class="add-link" data-text="             Cloud Search API" tabindex="-1"><a href="/workspace/cloud-search">Cloud Search API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=cloudsearch.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="cloudsearch.googleapis.com">Enable Cloud Search API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable cloudsearch.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="docs-api" class="add-link" data-text="             Docs API" tabindex="-1"><a href="/workspace/docs">Docs API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=docs.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="docs.googleapis.com">Enable Docs API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable docs.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="drive-api" class="add-link" data-text="             Drive API" tabindex="-1"><a href="/drive">Drive API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="drive.googleapis.com">Enable Drive API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable drive.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="drive-activity-api" class="add-link" data-text="             Drive Activity API" tabindex="-1"><a href="/drive/activity">Drive Activity API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=driveactivity.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="driveactivity.googleapis.com">Enable Drive Activity API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable driveactivity.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="drive-labels-api" class="add-link" data-text="             Drive Labels API" tabindex="-1"><a href="/drive/labels">Drive Labels API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=drivelabels.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="drivelabels.googleapis.com">Enable Drive Labels API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable drivelabels.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="forms-api" class="add-link" data-text="             Forms API" tabindex="-1"><a href="/workspace/forms/api">Forms API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=forms.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="forms.googleapis.com">Enable Forms API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable forms.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="gmail-api" class="add-link" data-text="             Gmail API" tabindex="-1"><a href="/workspace/gmail">Gmail API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=gmail.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="gmail.googleapis.com">Enable Gmail API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable gmail.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="groups-migration-api" class="add-link" data-text="             Groups Migration API" tabindex="-1"><a href="/workspace/admin/groups-migration">Groups Migration API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=groupsmigration.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="groupsmigration.googleapis.com">Enable Groups Migration API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable groupsmigration.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="groups-settings-api" class="add-link" data-text="             Groups Settings API" tabindex="-1"><a href="/workspace/admin/groups-settings">Groups Settings API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=groupssettings.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="groupssettings.googleapis.com">Enable Groups Settings API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable groupssettings.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="google-workspace-add-ons-api" class="add-link" data-text="             Google Workspace add-ons API" tabindex="-1"><a href="/workspace/add-ons">Google Workspace add-ons API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=gsuiteaddons.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="gsuiteaddons.googleapis.com">Enable Google Workspace add-ons API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable gsuiteaddons.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="google-keep-api" class="add-link" data-text="             Google Keep API" tabindex="-1"><a href="/workspace/keep/api">Google Keep API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=keep.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="keep.googleapis.com">Enable Google Keep API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable keep.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="enterprise-license-manager-api" class="add-link" data-text="             Enterprise License Manager API" tabindex="-1"><a href="/workspace/admin/licensing">Enterprise License Manager API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=licensing.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="licensing.googleapis.com">Enable Enterprise License Manager API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable licensing.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="marketplace-api" class="add-link" data-text="             Marketplace API" tabindex="-1"><a href="/workspace/marketplace/reference/rest">Marketplace API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=appsmarket.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="appsmarket.googleapis.com">Enable Marketplace API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable appsmarket.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="marketplace-sdk" class="add-link" data-text="             Marketplace SDK" tabindex="-1"><a href="/workspace/marketplace">Marketplace SDK</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=appsmarket-component.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="appsmarket-component.googleapis.com">Enable Marketplace SDK</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable appsmarket-component.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="meet-rest-api" class="add-link" data-text="             Meet REST API" tabindex="-1"><a href="/meet">Meet REST API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=meet.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="meet.googleapis.com">Enable Meet REST API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable meet.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="people-api" class="add-link" data-text="             People API" tabindex="-1"><a href="/people">People API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=people.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="people.googleapis.com">Enable People API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable people.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="postmaster-tools-api" class="add-link" data-text="             Postmaster Tools API" tabindex="-1"><a href="/workspace/gmail/postmaster">Postmaster Tools API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=gmailpostmastertools.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="gmailpostmastertools.googleapis.com">Enable Postmaster Tools API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable gmailpostmastertools.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="reseller-api" class="add-link" data-text="             Reseller API" tabindex="-1"><a href="/workspace/admin/reseller">Reseller API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=reseller.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="reseller.googleapis.com">Enable Reseller API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable reseller.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="sheets-api" class="add-link" data-text="             Sheets API" tabindex="-1"><a href="/workspace/sheets">Sheets API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=sheets.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="sheets.googleapis.com">Enable Sheets API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable sheets.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="slides-api" class="add-link" data-text="             Slides API" tabindex="-1"><a href="/workspace/slides">Slides API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=slides.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="slides.googleapis.com">Enable Slides API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable slides.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="tasks-api" class="add-link" data-text="             Tasks API" tabindex="-1"><a href="/workspace/tasks">Tasks API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=tasks.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="tasks.googleapis.com">Enable Tasks API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable tasks.googleapis.com</code></pre></td>
</tr>
<tr>
<td><h3 id="vault-api" class="add-link" data-text="             Vault API" tabindex="-1"><a href="/workspace/vault">Vault API</a></h3></td>
<td style="flex-direction: column"><a href="https://console.cloud.google.com/flows/enableapi?apiid=vault.googleapis.com" class="button button-primary" target="console" data-category="Workspace:EnableAPI" data-label="vault.googleapis.com">Enable Vault API</a>
<div>
&#10;</div>
<pre class="devsite-terminal devsite-click-to-copy" translate="no" dir="ltr" data-is-upgraded=""><code>gcloud services enable vault.googleapis.com</code></pre></td>
</tr>
</tbody>
</table>

</div>

## Next step

[Learn how authentication and authorization works](/workspace/guides/auth-overview) for Google Workspace APIs.

</div>

Send feedback

<div class="devsite-floating-action-buttons">

</div>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-20 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-04-20 UTC."\],\[\],\["To use Google APIs, they must be enabled in a Google Cloud project. This can be done via the Google Cloud console by navigating to the Product Library, selecting the API, and clicking \\Enable,\\ repeating for multiple APIs. Alternatively, using the Google Cloud CLI, run \`gcloud services enable API_SERVICE_ID\` to enable specific API. A list of google workspace APIs is provided along with their corresponding links and \`gcloud\` commands.\n"\]\]

</div>

</div>
