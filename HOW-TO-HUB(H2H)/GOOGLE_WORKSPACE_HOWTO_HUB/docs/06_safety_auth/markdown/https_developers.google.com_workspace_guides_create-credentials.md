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

# Create access credentials <span slot="popout-heading"> Stay organized with collections </span> <span slot="popout-contents"> Save and categorize content based on your preferences. </span>

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

- Google Workspace APIs require credentials, which can be API keys, OAuth client IDs, or service accounts, depending on the type of access needed.

- API keys provide anonymous access to public data and are created in the Google Cloud console.

- OAuth client IDs are used for accessing user data with consent and require separate IDs for different platforms.

- Service accounts enable applications to access data or act on behalf of users and require role assignment and secure key management.

- Creating a service account involves assigning roles, generating keys, and optionally configuring domain-wide delegation for accessing user data on behalf of the application.

</div>

Credentials are used to obtain an access token from Google's authorization servers so your app can call Google Workspace APIs. This guide describes how to choose and set up the credentials your app needs.

For definitions of terms found on this page, see the [Authentication and authorization overview](/workspace/guides/auth-overview).

## Choose the access credential that is right for you

The required credentials depend on the type of data, platform, and access methodology of your app. There are three types of credentials available:

| Use case | Authentication method | About this authentication method |
|----|----|----|
| Access publicly available data anonymously in your app. | [API keys](#api-key) | Check that the API you want to use supports API keys before using this authentication method. |
| Access user data such as their email address or age. | [OAuth client ID](#oauth-client-id) | Requires your app to request and receive consent from the user. |
| Access data that belongs to your own application or access resources on behalf of Google Workspace or Cloud Identity users through [domain-wide delegation.](#optional_set_up_domain-wide_delegation_for_a_service_account) | [Service account](#service-account) | When an app authenticates as a service account, it has access to all resources that the service account has permission to access. |

**Note:** To be guided on how to choose a credential, see [Choose the right authentication method for your use case](https://cloud.google.com/docs/authentication#auth-decision-tree) in the Google Cloud console or use the [Help me choose option](https://console.cloud.google.com/apis/credentials/wizard) in the Google Cloud console.

### API key credentials

An API key is a long string containing upper and lower case letters, numbers, underscores, and hyphens, such as `AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe`. This authentication method is used to anonymously access publicly available data, such as Google Workspace files shared using the "Anyone on the Internet with this link" sharing setting. For more details, see [Using API keys](https://cloud.google.com/docs/authentication/api-keys).

To create an API key:

1.  In the Google Cloud console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **APIs & Services** <span aria-label="and then">\></span> **Credentials**.

    <a href="https://console.cloud.google.com/apis/credentials" class="button button-primary" target="console">Go to Credentials</a>

2.  Click **Create credentials** <span aria-label="and then">\></span> **API key**.

3.  Your new API key is displayed.
    - Click Copy <span class="material-icons" aria-hidden="true" translate="no">content_copy</span> to copy your API key for use in your app's code. The API key can also be found in the "API Keys" section of your project's credentials.
    - To prevent unauthorized use, we recommend restricting where and for which APIs the API key can be used. For more details, see [Add API restrictions](https://cloud.google.com/docs/authentication/api-keys#adding-api-restrictions).

### OAuth client ID credentials

To authenticate end users and access user data in your app, you need to create one or more OAuth 2.0 Client IDs. A client ID is used to identify a single app to Google's OAuth servers. If your app runs on multiple platforms, you must create a separate client ID for each platform.

Choose your [application type](https://support.google.com/cloud/answer/6158849#service-web-app&zippy=%2Cweb-applications%2Cnative-applications) for specific instructions about how to create an OAuth client ID:

<div class="section">

<div class="section">

### Web application

1.  In the Google API Console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **Google Auth platform** <span aria-label="and then">\></span> **Clients**.

    <a href="https://console.developers.google.com/auth/clients" class="button button-primary" target="console">Go to Clients</a>

2.  Click **Create Client**.

3.  Click **Application type** <span aria-label="and then">\></span> **Web application**.

4.  In the **Name** field, type a name for the credential. This name is only shown in the Google API Console.

5.  Add authorized URIs related to your app:
    - **Client-side apps (JavaScript)**–Under **Authorized JavaScript origins**, click **Add URI**. Then, enter a URI to use for browser requests. This identifies the domains from which your application can send API requests to the OAuth 2.0 server.
    - **Server-side apps (Java, Python, and more)**–Under **Authorized redirect URIs**, click **Add URI**. Then, enter an endpoint URI to which the OAuth 2.0 server can send responses.

6.  Click **Create**.

    The newly created credential appears under **OAuth 2.0 Client IDs**.

    Note the Client ID. Client secrets aren't used for Web applications.

</div>

<div class="section">

### Android

1.  In the Google API Console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **Google Auth platform** <span aria-label="and then">\></span> **Clients**.

    <a href="https://console.developers.google.com/auth/clients" class="button button-primary" target="console">Go to Clients</a>

2.  Click **Create Client**.

3.  Click **Application type** <span aria-label="and then">\></span> **Android**.

4.  In the "Name" field, type a name for the credential. This name is only shown in the Google API Console.

5.  In the "Package name" field, enter the package name from your `AndroidManifest.xml` file.

6.  In the "SHA-1 certificate fingerprint" field, enter your <a href="https://support.google.com/cloud/answer/6158849#installedapplications&amp;android&amp;zippy=%2Cnative-applications%2Candroid" class="external" target="_blank">generated SHA-1 certificate fingerprint</a>.

7.  Click **Create**.

    The newly created credential appears under "OAuth 2.0 Client IDs."

</div>

<div class="section">

### iOS

1.  In the Google API Console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **Google Auth platform** <span aria-label="and then">\></span> **Clients**.

    <a href="https://console.developers.google.com/auth/clients" class="button button-primary" target="console">Go to Clients</a>

2.  Click **Create Client**.

3.  Click **Application type** <span aria-label="and then">\></span> **iOS**.

4.  In the "Name" field, type a name for the credential. This name is only shown in the Google API Console.

5.  In the "Bundle ID" field, enter the bundle identifier as listed in the app's `Info.plist` file.

6.  Optional: If your app appears in the Apple App Store, enter the App Store ID.

7.  Optional: In the "Team ID" field, enter the unique 10-character string that's generated by Apple and assigned to your team.

8.  Click **Create**.

    The newly created credential appears under "OAuth 2.0 Client IDs."

</div>

<div class="section">

### Chrome Extension

1.  In the Google API Console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **Google Auth platform** <span aria-label="and then">\></span> **Clients**.

    <a href="https://console.developers.google.com/auth/clients" class="button button-primary" target="console">Go to Clients</a>

2.  Click **Create Client**.

3.  Click **Application type** <span aria-label="and then">\></span> **Chrome Extension**.

4.  In the "Name" field, type a name for the credential. This name is only shown in the Google API Console.

5.  In the "Item ID" field, enter your app's unique 32-character ID string. You can find this ID value in your app's Chrome Web Store URL and in the <a href="https://chrome.google.com/webstore/developer/dashboard" class="external" target="_blank">Chrome Web Store Developer Dashboard</a>.

6.  Click **Create**.

    The newly created credential appears under "OAuth 2.0 Client IDs."

</div>

<div class="section">

### Desktop app

1.  In the Google API Console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **Google Auth platform** <span aria-label="and then">\></span> **Clients**.

    <a href="https://console.developers.google.com/auth/clients" class="button button-primary" target="console">Go to Clients</a>

2.  Click **Create Client**.

3.  Click **Application type** <span aria-label="and then">\></span> **Desktop app**.

4.  In the **Name** field, type a name for the credential. This name is only shown in the Google API Console.

5.  Click **Create**.

    The newly created credential appears under "OAuth 2.0 Client IDs."

</div>

<div class="section">

### TVs & Limited Input devices

1.  In the Google API Console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **Google Auth platform** <span aria-label="and then">\></span> **Clients**.

    <a href="https://console.developers.google.com/auth/clients" class="button button-primary" target="console">Go to Clients</a>

2.  Click **Create Client**.

3.  Click **Application type** <span aria-label="and then">\></span> **TVs & Limited Input devices**.

4.  In the "Name" field, type a name for the credential. This name is only shown in the Google API Console.

5.  Click **Create**.

    The newly created credential appears under "OAuth 2.0 Client IDs."

</div>

</div>

### Service account credentials

A service account is a special kind of account used by an application, rather than a person. You can use a service account to access data or perform actions by the robot account, or to access data on behalf of Google Workspace or Cloud Identity users. For more information, see <a href="https://cloud.google.com/iam/docs/understanding-service-accounts" class="external" target="_blank">Understanding service accounts</a>.

#### Create a service account

<div class="section">

### Google API Console

1.  In the Google API Console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **IAM & Admin** <span aria-label="and then">\></span> **Service Accounts**.

    <a href="https://console.developers.google.com/iam-admin/serviceaccounts" class="button button-primary" target="console">Go to Service Accounts</a>

2.  Click **Create service account**.

3.  Fill in the service account details, then click **Create and continue**.
    Note: By default, Google creates a unique service account ID. If you would like to change the ID, modify the ID in the service account ID field.

4.  Optional: Assign roles to your service account to grant access to your Google Cloud project's resources. For more details, refer to <a href="https://cloud.google.com/iam/docs/granting-changing-revoking-access" class="external" target="_blank">Granting, changing, and revoking access to resources</a>.

5.  Click **Continue**.

6.  Optional: Enter users or groups that can manage and perform actions with this service account. For more details, refer to <a href="https://cloud.google.com/iam/docs/impersonating-service-accounts" class="external" target="_blank">Managing service account impersonation</a>.

7.  Click **Done**. Make a note of the email address for the service account.

</div>

<div class="section">

### gcloud CLI

1.  Create the service account:

    <div>

    </div>

    ``` devsite-click-to-copy
    gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
      --display-name="SERVICE_ACCOUNT_NAME"
    ```

2.  Optional: Assign roles to your service account to grant access to your Google Cloud project's resources. For more details, refer to <a href="https://cloud.google.com/iam/docs/granting-changing-revoking-access" class="external" target="_blank">Granting, changing, and revoking access to resources</a>.

</div>

#### Assign a role to a service account

You must assign a prebuilt or custom role to a service account by a super administrator account.

1.  In the Google Admin console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span><span aria-label="and then">\></span> **Account** <span aria-label="and then">\></span> **Admin roles**.

    <a href="https://admin.google.com/ac/roles" class="button button-primary" target="admin-console">Go to Admin roles</a>

2.  Point to the role that you want to assign, and then click **Assign admin**.

3.  Click **Assign service accounts**.

4.  Enter the email address of the service account.

5.  Click **Add <span aria-label="and then">\></span> Assign role**.

#### Create credentials for a service account

You need to obtain credentials in the form of a public/private key pair. These credentials are used by your code to authorize service account actions within your app.

To obtain credentials for your service account:

1.  In the Google Cloud console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **IAM & Admin** <span aria-label="and then">\></span> **Service Accounts**.

    <a href="https://console.cloud.google.com/iam-admin/serviceaccounts" class="button button-primary" target="console">Go to Service Accounts</a>

2.  Select your service account.

3.  Click **Keys** <span aria-label="and then">\></span> **Add key** <span aria-label="and then">\></span> **Create new key**.

4.  Select **JSON**, then click **Create**.

    Your new public/private key pair is generated and downloaded to your machine as a new file. Save the downloaded JSON file as `credentials.json` in your working directory. This file is the only copy of this key. For information about how to store your key securely, see <a href="https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys" class="external" target="_blank">Managing service account keys</a>.

5.  Click **Close**.

#### Optional: Set up domain-wide delegation for a service account

To call APIs on behalf of users in a Google Workspace organization, your service account needs to be granted domain-wide delegation of authority in the Google Workspace Admin console by a super administrator account. For more information, see <a href="/identity/protocols/oauth2/service-account#delegatingauthority" class="external" target="_blank">Delegating domain-wide authority to a service account</a>.

To set up domain-wide delegation of authority for a service account:

1.  In the Google Cloud console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **IAM & Admin** <span aria-label="and then">\></span> **Service Accounts**.

    <a href="https://console.cloud.google.com/iam-admin/serviceaccounts" class="button button-primary" target="console">Go to Service Accounts</a>

2.  Select your service account.

3.  Click **Show advanced settings**.

4.  Under "Domain-wide delegation," find your service account's "Client ID." Click Copy <span class="material-icons" aria-hidden="true" translate="no">content_copy</span> to copy the client ID value to your clipboard.

5.  If you have super administrator access to the relevant Google Workspace account, click **View Google Workspace Admin Console**, then sign in using a super administrator user account and continue following these steps.

    If you don't have super administrator access to the relevant Google Workspace account, contact a super administrator for that account and send them your service account's Client ID and list of OAuth Scopes so they can complete the following steps in the Admin console.

    1.  In the Google Admin console, go to Menu <span class="material-icons" aria-hidden="true" translate="no">menu</span> <span aria-label="and then">\></span> **Security** <span aria-label="and then">\></span> **Access and data control** <span aria-label="and then">\></span> **API controls**.

        <a href="https://admin.google.com/ac/owl" class="button button-primary" target="admin-console">Go to API controls</a>

    2.  Click **Manage Domain Wide Delegation**.

    3.  Click **Add new**.

    4.  In the "Client ID" field, paste the client ID that you previously copied.

    5.  In the "OAuth Scopes" field, enter a comma-delimited list of the scopes required by your application. This is the same set of scopes you defined when configuring the OAuth consent screen.

    6.  Click **Authorize**.

## Next step

You're ready to develop on Google Workspace! Review the list of [Google Workspace developer products](/workspace/products) and [how to find help](/workspace/support).

</div>

Send feedback

<div class="devsite-floating-action-buttons">

</div>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-20 UTC.

<div class="devsite-content-data">

Need to tell us more?

\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-04-20 UTC."\],\[\],\["Google uses credentials for apps to access Google Workspace APIs. Three credential types exist: API keys for public data access, OAuth client IDs for user data, and service accounts for application-owned data or delegated access. To create an API key go to the API and Services section in the Google Cloud console. Create an OAuth client ID by choosing the correct app platform and filling the required fields. Service accounts are created through IAM & Admin section of the Google Cloud console, or CLI, and allow role assignments and key generation. Domain-wide delegation can be set up in the Google Admin console to make API calls on behalf of users.\n"\]\]

</div>

</div>
