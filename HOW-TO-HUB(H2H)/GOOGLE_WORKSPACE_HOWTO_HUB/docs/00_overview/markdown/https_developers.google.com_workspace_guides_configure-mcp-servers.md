<div id="main-content" class="devsite-main-content" role="main" has-sidebar="">

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

  <a href="https://developers.google.com/workspace/guides/configure-mcp-servers" class="devsite-breadcrumb-link gc-analytics-event" data-category="Site-Wide Custom Events" data-label="Breadcrumbs" data-value="3" data-track-type="globalNav" data-track-name="breadcrumb" data-track-metadata-position="3" data-track-metadata-eventdetail="">MCP servers</a>

</div>

Send feedback

# Configure the Google Workspace MCP servers <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

<div class="devsite-page-title-meta">

</div>

<div class="devsite-article-body clearfix">

**Developer Preview:** Available as part of the <a href="https://developers.google.com/workspace/preview" class="external" target="_blank">Google Workspace Developer Preview Program</a>, which grants early access to certain features.

Google Workspace offers remote [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) servers that allow AI agents to securely interact with Google Workspace data. By configuring the Google Workspace MCP servers, you enable AI applications like Gemini CLI, Claude, or IDEs to perform actions in Google Workspace applications like Gmail, Google Drive, Google Calendar, and Google Chat. Each Google Workspace product has its own dedicated MCP server.

The Google Workspace MCP servers provide a standardized way for AI agents to:

- **Read data**: Search emails, retrieve files, and list calendar events.
- **Take action**: Create draft emails, upload files, and schedule meetings.
- **Respect security**: Inherit the same permissions and data governance controls as the user.

## Prerequisites

- A Google Cloud project. To create a project, see [Create a project](/workspace/guides/create-project).

- An MCP client, like [Gemini CLI](https://geminicli.com/).

- To run the commands on this page, set up the gcloud CLI in a local development environment by following these steps:

  1.  [Install the Google Cloud CLI](https://cloud.google.com/sdk/docs/install). If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`.
  2.  If you're using an external identity provider (IdP), sign in to the gcloud CLI with your federated identity. For more information, see [Sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).
  3.  [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initializing).

## Configure the Google Workspace MCP servers

To use the Google Workspace MCP servers, you must enable them in your Google Cloud project and then configure your MCP client to connect to them.

### Enable the APIs

To use the Google Workspace MCP servers, you must enable the following APIs in your Google Cloud project:

- Gmail API

- Google Drive API

- Google Calendar API

- Google Chat API

- People API

<div>

<div class="section">

### CLI

<div>

</div>

``` devsite-click-to-copy
gcloud services enable gmail.googleapis.com \
drive.googleapis.com \
calendar-json.googleapis.com \
chat.googleapis.com \
people.googleapis.com --project=PROJECT_ID
```

Replace `PROJECT_ID` with your Google Cloud project ID.

</div>

<div class="section">

### Console

Enable the APIs in the Google Cloud console:

<a href="https://console.cloud.google.com/flows/enableapi?apiid=gmail.googleapis.com,drive.googleapis.com,calendar-json.googleapis.com,chat.googleapis.com,people.googleapis.com" class="button button-primary" target="console">Enable the APIs</a>

</div>

</div>

### Enable the MCP services

To enable the MCP components for each Google Workspace product, you must enable the following services in your Google Cloud project:

- Gmail MCP API

- Google Drive MCP API

- Google Calendar MCP API

- Google Chat MCP API

- People MCP API

<div>

<div class="section">

### CLI

<div>

</div>

``` devsite-click-to-copy
gcloud services enable gmailmcp.googleapis.com \
drivemcp.googleapis.com \
calendarmcp.googleapis.com \
chatmcp.googleapis.com \
people.googleapis.com --project=PROJECT_ID
```

Replace `PROJECT_ID` with your Google Cloud project ID.

</div>

<div class="section">

### Console

Enable the MCP services in the Google Cloud console:

<a href="https://console.cloud.google.com/flows/enableapi?apiid=gmailmcp.googleapis.com,drivemcp.googleapis.com,calendarmcp.googleapis.com,chatmcp.googleapis.com,people.googleapis.com" class="button button-primary" target="console">Enable the MCP services</a>

</div>

</div>

### Configure the Chat app

To use the Google Chat MCP server, you must configure a Chat app in your Google Cloud project.

1.  In the Google Cloud console, search for **Google Chat API**, and click **Google Chat API** **\>** **Manage** **\>** **Configuration**.

    <a href="https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat" class="button button-primary" target="console">Go to Google Chat API</a>

2.  Set up the Chat app:

    1.  In **App name** field, enter `Chat MCP`.
    2.  In **Avatar URL** field, enter `https://developers.google.com/chat/images/quickstart-app-avatar.png`.
    3.  In **Description**, enter `Chat MCP server`.
    4.  Under **Functionality**, turn off interactive features by toggling **Enable interactive features** off.
    5.  Under **Logs**, select **Log errors to Logging**.

3.  Click **Save**.

To learn more about building a Chat app, see [Choose a Google Chat app architecture](https://developers.google.com/workspace/chat/structure).

### Set up the OAuth consent screen

The Google Workspace MCP servers use OAuth 2.0 for authentication and authorization. You must configure the OAuth consent screen before you can create an OAuth client ID.

1.  In the Google Cloud console, go to **Google Auth Platform** **\>** **Branding**.

    <a href="https://console.cloud.google.com/auth/branding" class="button button-primary" target="_blank">Go to Branding</a>

2.  If you have already configured the **Google Auth Platform**, you can configure the following OAuth Consent Screen settings in [Branding](https://console.cloud.google.com/auth/branding), [Audience](https://console.cloud.google.com/auth/audience), and [Data Access](https://console.cloud.google.com/auth/scopes). If you see a message that says **Google Auth Platform not configured yet**, click **Get Started**:

    1.  Under **App Information**, in **App name**, type `Workspace MCP Servers`.
    2.  In **User support email**, select your email address or an appropriate Google group.
    3.  Click **Next**.
    4.  Under **Audience**, select **Internal**. If you can't select **Internal**, select **External**.
    5.  Click **Next**.
    6.  Under **Contact Information**, enter an **Email address** where you can be notified about any changes to your project.
    7.  Click **Next**.
    8.  Under **Finish**, review the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy) and if you agree, select **I agree to the Google API Services: User Data Policy**.
    9.  Click **Continue**.
    10. Click **Create**.
    11. If you selected **External** for user type, add test users:
        1.  Click **Audience**.
        2.  Under **Test users**, click **Add users**.
        3.  Enter your email address and any other authorized test users, then click **Save**.

3.  Click **Data Access** **\>** **Add or Remove Scopes**. A panel appears with a list of scopes for each API that you've enabled in your Google Cloud project.

    1.  Under **Manually add scopes**, paste the scopes for the MCP servers you want to use:

        - **Gmail**:
          - `https://www.googleapis.com/auth/gmail.readonly`
          - `https://www.googleapis.com/auth/gmail.compose`
        - **Google Drive**:
          - `https://www.googleapis.com/auth/drive.readonly`
          - `https://www.googleapis.com/auth/drive.file`
        - **Google Calendar**:
          - `https://www.googleapis.com/auth/calendar.calendarlist.readonly`
          - `https://www.googleapis.com/auth/calendar.events.freebusy`
          - `https://www.googleapis.com/auth/calendar.events.readonly`
        - **Google Chat**:
          - `https://www.googleapis.com/auth/chat.spaces.readonly`
          - `https://www.googleapis.com/auth/chat.memberships.readonly`
          - `https://www.googleapis.com/auth/chat.messages.readonly`
          - `https://www.googleapis.com/auth/chat.messages.create`
          - `https://www.googleapis.com/auth/chat.users.readstate.readonly`
        - **People API**:
          - `https://www.googleapis.com/auth/directory.readonly`
          - `https://www.googleapis.com/auth/userinfo.profile`
          - `https://www.googleapis.com/auth/contacts.readonly`

    2.  Click **Add to Table**.

    3.  Click **Update**.

    4.  After selecting the scopes required by your app, on the **Data Access** page, click **Save**.

### Configure your MCP client

To add the Google Workspace remote MCP server to your MCP client, follow the instructions for your client.

<div>

<div class="section">

### Gemini CLI

To add the Google Workspace remote MCP servers to your Gemini CLI, add the server configuration to your `settings.json` file.

1.  Create an OAuth 2.0 client ID and secret:

    1.  In the Google Cloud console, go to **Google Auth Platform** **\>** **Clients** **\>** **Create Client**

        <a href="https://console.cloud.google.com//auth/clients/create" class="button button-primary" target="_blank">Go to Create Client</a>

    2.  Select **Desktop app** as the application type.

    3.  Enter a **Name**.

    4.  Click **Create** and copy your **Client ID** and **Client Secret**.

2.  Open or create the configuration file `~/.gemini/settings.json`.

3.  Add the `mcpServers` configuration to `settings.json`:

    <div>

    </div>

    ``` devsite-click-to-copy
    {
      "mcpServers": {
        "gmail": {
          "httpUrl": "https://gmailmcp.googleapis.com/mcp/v1",
          "oauth": {
            "enabled": true,
            "clientId": "OAUTH_CLIENT_ID",
            "clientSecret": "OAUTH_CLIENT_SECRET",
            "scopes": [
              "https://www.googleapis.com/auth/gmail.readonly",
              "https://www.googleapis.com/auth/gmail.compose"
            ]
          }
        },
        "drive": {
          "httpUrl": "https://drivemcp.googleapis.com/mcp/v1",
          "oauth": {
            "enabled": true,
            "clientId": "OAUTH_CLIENT_ID",
            "clientSecret": "OAUTH_CLIENT_SECRET",
            "scopes": [
              "https://www.googleapis.com/auth/drive.readonly",
              "https://www.googleapis.com/auth/drive.file"
            ]
          }
        },
        "calendar": {
          "httpUrl": "https://calendarmcp.googleapis.com/mcp/v1",
          "oauth": {
            "enabled": true,
            "clientId": "OAUTH_CLIENT_ID",
            "clientSecret": "OAUTH_CLIENT_SECRET",
            "scopes": [
              "https://www.googleapis.com/auth/calendar.calendarlist.readonly",
              "https://www.googleapis.com/auth/calendar.events.freebusy",
              "https://www.googleapis.com/auth/calendar.events.readonly"
            ]
          }
        },
        "people": {
          "httpUrl": "https://people.googleapis.com/mcp/v1",
          "oauth": {
            "enabled": true,
            "clientId": "OAUTH_CLIENT_ID",
            "clientSecret": "OAUTH_CLIENT_SECRET",
            "scopes": [
              "https://www.googleapis.com/auth/directory.readonly",
              "https://www.googleapis.com/auth/userinfo.profile",
              "https://www.googleapis.com/auth/contacts.readonly"
            ]
          }
        },
        "chat": {
          "httpUrl": "https://chatmcp.googleapis.com/mcp/v1",
          "oauth": {
            "enabled": true,
            "clientId": "OAUTH_CLIENT_ID",
            "clientSecret": "OAUTH_CLIENT_SECRET",
            "scopes": [
              "https://www.googleapis.com/auth/chat.spaces.readonly",
              "https://www.googleapis.com/auth/chat.memberships.readonly",
              "https://www.googleapis.com/auth/chat.messages.readonly",
              "https://www.googleapis.com/auth/chat.messages.create",
              "https://www.googleapis.com/auth/chat.users.readstate.readonly"
            ]
          }
        }
      }
    }
    ```

    Replace the following:

    - `OAUTH_CLIENT_ID`: The client ID you created.
    - `OAUTH_CLIENT_SECRET`: The client secret you created.

4.  Save `settings.json`.

5.  Start Gemini CLI:

    <div>

    </div>

    ``` devsite-click-to-copy
    gemini
    ```

6.  In Gemini CLI, authenticate with each MCP server by running the following command:

    <div>

    </div>

    ``` devsite-click-to-copy
    /mcp auth gmail
    ```

    1.  When prompted, press `1` to open an authentication page in your browser. If you're working over SSH, follow the instructions in the CLI.

    2.  Sign in to your Google Account.

    3.  Review the requested OAuth scopes and click **Allow**.

    4.  A message appears confirming authentication was successful.

    5.  Repeat these for each MCP server:

        - `/mcp auth drive`
        - `/mcp auth calendar`
        - `/mcp auth people`
        - `/mcp auth chat`

7.  In Gemini CLI, run `/mcp list` to view your configured MCP servers and their tools.

    The response is similar to the following:

    <div>

    </div>

    ``` devsite-click-to-copy
    🟢 gmail - Ready (10 tools)
      Tools:
      - create_draft
      - create_label
      - get_thread
      - label_message
      - label_thread
      - list_drafts
      - list_labels
      - search_threads
      - unlabel_message
      - unlabel_thread

    🟢 drive - Ready (7 tools)
      Tools:
      - create_file
      - download_file_content
      - get_file_metadata
      - get_file_permissions
      - list_recent_files
      - read_file_content
      - search_files

    🟢 calendar - Ready (8 tools)
      Tools:
      - create_event
      - delete_event
      - get_event
      - list_calendars
      - list_events
      - respond_to_event
      - suggest_time
      - update_event

    🟢 people - Ready (3 tools)
      Tools:
      - get_user_profile
      - search_contacts
      - search_directory_people

    🟢 chat - Ready (4 tools)
      Tools:
      - search_conversations
      - list_messages
      - search_messages
      - send_message
    ```

The remote MCP server is ready to use in Gemini CLI.

</div>

<div class="section">

### Claude

To use the Google Workspace remote MCP servers with Claude.ai or Claude Desktop, you must have the Claude Enterprise, Pro, Max, or Team plan.

To add the Google Workspace remote MCP servers to Claude, configure a custom connector with an OAuth client ID and secret.

1.  Create an OAuth 2.0 client ID and secret:

    1.  In the Google Cloud console, go to **Google Auth Platform** **\>** **Clients** **\>** **Create Client**

        <a href="https://console.cloud.google.com//apis/credentials/oauthclient" class="button button-primary" target="_blank">Go to Create Client</a>

    2.  Select **Web application** as the application type.

    3.  Enter a **Name**.

    4.  In the **Authorized redirect URIs** section, click **+ Add URI**, and then add `https://claude.ai/api/mcp/auth_callback` in the **URIs** field.

    5.  Click **Create** and copy your **Client ID** and **Client Secret**.

2.  Configure the MCP server in Claude:

    1.  In Claude.ai or Claude Desktop, go to **Settings** (or **Admin settings**) \> **Connectors**.
    2.  Click **Add custom connector**.
    3.  Enter the connection details for the Google Workspace product you want to add:
        - **Server name**: A name for the server, like `Gmail`.
        - **Remote MCP server URL**: The URL for the Google Workspace product, such as one of the following:
          - Gmail: `https://gmailmcp.googleapis.com/mcp/v1`
          - Google Drive: `https://drivemcp.googleapis.com/mcp/v1`
          - Google Calendar: `https://calendarmcp.googleapis.com/mcp/v1`
          - Google Chat: `https://chatmcp.googleapis.com/mcp/v1`
          - People API: `https://people.googleapis.com/mcp/v1`
    4.  In **Advanced settings**, enter your **OAuth client ID** and **OAuth client secret**.
    5.  Click **Add**.
    6.  Repeat these steps for each Google Workspace product you want to add.

</div>

<div class="section">

### Others

Many AI applications have ways to connect to a remote MCP server. You typically need to enter details about the server, like its name, endpoints, transport protocol, and authentication method. For the Google Workspace remote MCP servers, enter the following:

- **Server name**: `googleworkspace`

- **Servers**: Each Google Workspace product has its own server URL:

  - Gmail: `https://gmailmcp.googleapis.com/mcp/v1`
  - Google Drive: `https://drivemcp.googleapis.com/mcp/v1`
  - Google Calendar: `https://calendarmcp.googleapis.com/mcp/v1`
  - Google Chat: `https://chatmcp.googleapis.com/mcp/v1`
  - People API: `https://people.googleapis.com/mcp/v1`

- **Transport**: HTTP

- **Authentication**: The Google Workspace remote MCP server uses OAuth 2.0. For details, see [Learn about authentication and authorization](/workspace/guides/auth-overview).

</div>

</div>

For more details on connecting different types of clients, see [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).

## Test the Google Workspace MCP servers

After you configure the MCP client, you can verify the connection by running some test prompts.

Try asking your MCP client the following questions:

- **"According to my Google Profile, what's my name?"**

  The client uses `people.get_user_profile` to retrieve your Google Workspace profile information.

- **"Summarize the file Marketing Plan."**

  The client calls `drive.search_files` to locate "Marketing Plan", then uses `drive.read_file_content` to retrieve and summarize its content.

- **"What did Ariel say in her last email about our marketing plan?"**

  The client filters for emails from Ariel using `gmail.search_threads`, retrieves the latest thread's content with `gmail.get_thread`, and then summarizes it for you.

- **"Draft an email to ariel@example.com saying that I approve the marketing plan."**

  The client uses `gmail.create_draft` to create an email in your drafts folder, allowing you to review and send it from Gmail.

- **"When is my next meeting with Ariel?"**

  The client checks your schedule using `calendar.list_events` and details your next meeting with Ariel.

If the tools execute successfully and you receive relevant responses, your Google Workspace MCP servers are correctly configured.

## Troubleshooting

If you encounter issues connecting to the MCP servers, you can check for errors in the OAuth logs. Ask your administrator to check the **OAuth log events** in the [security investigation tool](https://support.google.com/a/answer/7575955).

## Supported products

The following Google Workspace products support Google Workspace MCP servers and offer the following tools:

- [Gmail](/workspace/gmail/api/reference/mcp)
  - [`create_draft`](/workspace/gmail/api/reference/mcp/tools_list/create_draft)
  - [`create_label`](/workspace/gmail/api/reference/mcp/tools_list/create_label)
  - [`get_thread`](/workspace/gmail/api/reference/mcp/tools_list/get_thread)
  - [`label_message`](/workspace/gmail/api/reference/mcp/tools_list/label_message)
  - [`label_thread`](/workspace/gmail/api/reference/mcp/tools_list/label_thread)
  - [`list_drafts`](/workspace/gmail/api/reference/mcp/tools_list/list_drafts)
  - [`list_labels`](/workspace/gmail/api/reference/mcp/tools_list/list_labels)
  - [`search_threads`](/workspace/gmail/api/reference/mcp/tools_list/search_threads)
  - [`unlabel_message`](/workspace/gmail/api/reference/mcp/tools_list/unlabel_message)
  - [`unlabel_thread`](/workspace/gmail/api/reference/mcp/tools_list/unlabel_thread)
- [Google Drive](/workspace/drive/api/reference/mcp)
  - [`create_file`](/workspace/drive/api/reference/mcp/tools_list/create_file)
  - [`download_file_content`](/workspace/drive/api/reference/mcp/tools_list/download_file_content)
  - [`get_file_metadata`](/workspace/drive/api/reference/mcp/tools_list/get_file_metadata)
  - [`get_file_permissions`](/workspace/drive/api/reference/mcp/tools_list/get_file_permissions)
  - [`list_recent_files`](/workspace/drive/api/reference/mcp/tools_list/list_recent_files)
  - [`read_file_content`](/workspace/drive/api/reference/mcp/tools_list/read_file_content)
  - [`search_files`](/workspace/drive/api/reference/mcp/tools_list/search_files)
- [Google Calendar](/workspace/calendar/api/v3/reference/mcp)
  - [`create_event`](/workspace/calendar/api/v3/reference/mcp/tools_list/create_event)
  - [`delete_event`](/workspace/calendar/api/v3/reference/mcp/tools_list/delete_event)
  - [`get_event`](/workspace/calendar/api/v3/reference/mcp/tools_list/get_event)
  - [`list_calendars`](/workspace/calendar/api/v3/reference/mcp/tools_list/list_calendars)
  - [`list_events`](/workspace/calendar/api/v3/reference/mcp/tools_list/list_events)
  - [`respond_to_event`](/workspace/calendar/api/v3/reference/mcp/tools_list/respond_to_event)
  - [`suggest_time`](/workspace/calendar/api/v3/reference/mcp/tools_list/suggest_time)
  - [`update_event`](/workspace/calendar/api/v3/reference/mcp/tools_list/update_event)
- [People API](/people/api/mcp)
  - [`get_user_profile`](/people/api/mcp/tools_list/get_user_profile)
  - [`search_contacts`](/people/api/mcp/tools_list/search_contacts)
  - [`search_directory_people`](/people/api/mcp/tools_list/search_directory_people)
- [Google Chat](/workspace/chat/api/reference/mcp)
  - [`search_conversations`](/workspace/chat/api/reference/mcp/tools_list/search_conversations)
  - [`list_messages`](/workspace/chat/api/reference/mcp/tools_list/list_messages)
  - [`search_messages`](/workspace/chat/api/reference/mcp/tools_list/search_messages)
  - [`send_message`](/workspace/chat/api/reference/mcp/tools_list/send_message)

## Important security consideration: Indirect prompt injection

When you expose a language model to untrusted data, there is a risk of an [indirect prompt injection attack](https://en.wikipedia.org/wiki/Prompt_injection). Because MCP clients like Gemini CLI have access to powerful tools and APIs through the Google Workspace MCP servers, they can read, modify, and delete data in your Google Account.

To mitigate these risks, follow these best practices:

- **Only use trusted tools.** Never connect Google Workspace MCP servers to untrusted or unverified applications.
- **Be cautious with untrusted inputs.** Avoid asking your MCP client to process emails, documents, or other resources from unverified sources. These inputs may contain hidden instructions that can hijack your session, allowing an attacker to modify, steal, or delete your data.
- **Review all actions.** Always carefully review the actions taken by your AI client on your behalf to ensure they are correct and align with your intentions.

## Related topics

- [Google Workspace MCP servers in Antigravity](//codelabs.developers.google.com/google-workspace-mcp-antigravity)
- [Get started with Google Workspace MCP and Gemini CLI](//codelabs.developers.google.com/google-workspace-mcp-gemini-cli)
- [Build a Google Workspace AI Agent with ADK and MCP](https://codelabs.developers.google.com/google-workspace-mcp-adk)

</div>

Send feedback

<div class="devsite-floating-action-buttons">

</div>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-12 UTC."\],\[\],\[\]\]

</div>

</div>
