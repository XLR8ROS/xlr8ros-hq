# Apps in ChatGPT Help Center

Source: https://help.openai.com/en/articles/11487775-apps-in-chatgpt
Fetched URL: https://help.openai.com/en/articles/11487775-apps-in-chatgpt
Fetched at: 2026-05-22T09:29:02.054302+00:00

---

Apps in ChatGPT | OpenAI Help Center

- [All Collections](https://developers.openai.com/en)

- [ChatGPT](https://developers.openai.com/en/collections/3742473-chatgpt)

- [Connected apps](https://developers.openai.com/en/collections/12923329-connected-apps)

- Apps in ChatGPT

# Apps in ChatGPT

Bring your tools and data into ChatGPT so you can search, reference, and work faster without leaving the conversation.

Updated: yesterday

As of December 17, 2025, we are renaming connectors to apps to present a more unified experience. The term now includes both apps that feature interactive UI and connectors that help you search and reference your information in ChatGPT. We are not removing any existing functionality; previously enabled connectors and company knowledge will continue to work as before.

# Overview

Apps let you work with external tools and information to help you get more done in a ChatGPT conversation. Some apps provide in-chat interactive experiences, while others securely connect to your services and data so ChatGPT can pull relevant context into your responses.

You can use select apps to take actions on your behalf, search and reference information from your data sources, run deep research across multiple sources with citations, or sync content in advance so you have up-to-date information on demand in your workspace’s knowledge base. Available apps are listed in the [ChatGPT app directory](https://chatgpt.com/apps). Browse, discover, and install a wide variety of apps to address your use cases.

Apps are available to all logged-in ChatGPT users, with some exceptions. See the note below.

Note: some apps may not be available in EEA, GB or Switzerland depending on whether the app partner offers service in the region. Some apps and app functionalities may be only available to Plus/Pro/Business and Enterprise/Edu plans.

# Connectors are now apps

To present a single unified experience of connected applications in ChatGPT, we have renamed connectors to apps. See the table below for the new terminology. Functionality has not been affected, and you do not need to reconnect any previously enabled connections.

Previous terminologyCurrent terminology

Chat connectorsApps with file search

Deep research connectorsApps with deep research

Synced connectorsApps with sync

# App capabilities

Certain app capabilities might be limited to certain ChatGPT plans. For example, an app may have File Search (Chat) capabilities for ChatGPT Enterprise, but only have deep research capability for Plus and Pro.

Apps may have several features to help you accomplish your tasks within ChatGPT.

### Interactive apps

Some apps [include rich, in-chat experiences](https://openai.com/index/introducing-apps-in-chatgpt/) (for example, interactive cards, maps, or playlists).

### Search

Apps can help you search and reference information from connected third-party services, pulling relevant context into your conversation.

### Deep research

Some apps can be used with deep research for complex, multi-source analysis, with citations back to the originals.

### Sync

Some apps support syncing to index content in advance for faster responses and improved quality.

### Write actions

Some apps may be able to take actions (for example, create or update information in a connected service). Availability depends on the app and how it is configured, and our policies require that apps request confirmation from you before proceeding with external actions.

Workspace admins (including Enterprise/Edu admins) can configure which actions an app is allowed to take for their workspace.

# Apps quickstart

-

Browse apps from the [ChatGPT app directory](https://chatgpt.com/apps), from Settings > Apps, or from the Apps entry in the sidebar.

-

Select the app you are interested in.

-

Select Connect if available.

-

Complete OAuth and enable sync if required.

-

After the app is connected, invoke it in chat by using @ mentions in your prompt or by selecting + and then More to select the app you want to add.

Read on for more details on setup, including workspace setup options for Business and Enterprise/Edu admins.

# Building your own app

In addition to apps available from the [app directory](https://chatgpt.com/apps), you can build your own custom app (formerly “custom connectors”), including to connect ChatGPT to your own tools and internal data.

-

Build apps using the Model Context Protocol (MCP) to let ChatGPT call approved tools and retrieve information from services.

-

If you are on a workspace plan, admins can control whether [custom apps are allowed](https://help.openai.com/articles/12584461) and how they are rolled out.

-

If you are a developer building an app, the Apps SDK is the recommended way to package and publish app experiences, including apps that use MCP-backed tools. You can get started with building apps by referring to the [Apps SDK documentation](https://developers.openai.com/apps-sdk?utm_source=chatgpt.com).

You can also submit apps for publication to the ChatGPT app directory. If your app is approved, inclusion in the app directory may make your app experience available to eligible ChatGPT users. See [submitting apps to the ChatGPT app directory](https://help.openai.com/articles/20001040) for more information.

# App directory

The [app directory](https://chatgpt.com/apps) helps you browse and discover apps in one place. Browse the app directory from Settings > Apps.

Your app directory view depends on your plan type. If you are on a Business or Enterprise/Edu plan, you can see the apps available for your workspace by selecting the workspace-specific tab. You can use other tabs to browse through app categories such as Lifestyle and Productivity.

Select each app entry to bring up the app page, which includes information about the app, such as the app’s capabilities. Select Connect to enable the app for use on your account.

Note: the Connect button for a given app may be greyed out based on geo restrictions, workspace settings, or your plan type. If the button or tooltip says Disabled by admin, ask your workspace admin to enable the app before trying again.

### Connect a new app

You can add apps from Settings > Apps.

-

Go to Settings > Apps.

-

Browse the app directory, find the app you are interested in, and select Connect.

-

Complete the app’s login and authorization flow, if applicable.

-

The app is now available for use in ChatGPT conversations.

### Business and Enterprise/Edu workspace setup

Admins and owners can control app availability from Workspace settings > Apps.

-

Apps are enabled by default for Business plans.

-

Apps are disabled by default for Enterprise/Edu plans.

You can view all available apps from the Directory tab. The Enabled tab shows apps currently enabled for your workspace, and the Drafts tab includes [custom apps being developed](https://help.openai.com/articles/12584461) for your organization.

The Enabled tab allows you to search and filter for apps and apply actions to a group of apps by selecting them. For example, you can filter for all apps with write actions and disable them as a group.

Workspace users can browse all available apps in the app directory, but they can only connect to apps that have been enabled by their workspace admin.

### Business workspace setup for admins and owners

Apps are enabled by default for Business plans, including apps with sync. You can manage apps from the Enabled tab.

-

Select the more options menu (•••) for the app you want to manage.

-

Select App details to review the app.

-

Select Action control to review which actions are available for the app.

-

Select Disable to make the app unavailable for your workspace.

-

Select Manage domains if you want to limit which accounts workspace members can use to connect the app.

You can also use the search and filtering functionality to select and configure multiple apps, so long as the configuration is common to all selected apps.

### Enterprise/Edu workspace setup for admins and owners

Apps are disabled by default for Enterprise/Edu workspaces. You can enable desired apps for your workspace by accessing the Directory tab and selecting Enable in the app listing. Depending on the app, you can configure several app features during the enablement process and select Publish for the changes to take effect.

### Configure access

Choose this option to configure [RBAC](https://help.openai.com/articles/11750701). By default, the app is available to all users in the workspace, but you can restrict access to specific groups.

### Configure actions

Choose this option to configure the actions an app can perform. Select Action control to review which actions the app can use in your workspace. Admins can choose how the app's current actions are handled by allowing all actions, allowing only read actions, or selecting a custom set of actions. If admins select Custom, they can also choose how actions added later are handled by selecting Enable all new actions, Only enable new read actions, or Disable new actions.

For non-sync apps, you can also add parameter constraints to actions. Parameter constraints help control what arguments the model is allowed to send to an app when the action is called. You can apply constraints to all non-object fields in an action, such as strings, numbers, booleans, arrays, and objects with nested properties. When a constraint blocks an action, end users will see a message explaining that the action was blocked due to a workspace configuration and which constraint prevented it.

To add a constraint:

-

Select Parameter Constraints for the action you want to constrain.

-

Locate the parameter you want to constrain and set the required constraint or filter.

-

Select the save button, such as Save regex for string constraints or Save range for numeric constraints.

If you want to remove the constraint, select Parameter Constraints for the action you want to revert, find the parameter, and then either delete the constraints you imposed or select Reset to default.

### Manage domains

If available, choose this option to limit which accounts workspace members can connect to ChatGPT by restricting connected accounts to an approved set of domains. The list of approved domains is configurable per app.

### Enable sync

Some apps may allow [sync](https://help.openai.com/articles/10847137). By default, users have to opt into sync from user settings when they connect the app. Some apps may allow you to enable sync for your entire team.

To enable sync for the app, select the checkbox, then select Publish. If the app supports it, you may see additional options to deploy team-wide or enable self-service.

-

Select Deploy to your team if available to enable sync for your entire team. Your team members will not need to do any additional setup.

-

Select Self-service setup to allow each team member to set up the app or connector individually from Settings > Apps.

After choosing options and publishing the app, it appears in the Enabled tab. You can further configure it by using the more options menu (•••) next to the app listing.

-

Select App details for more information about the app.

-

Select User access to control RBAC.

-

Select Action control if available to configure app actions.

-

Select Disable to make the app unavailable for your workspace.

You can also use the search and filtering functionality to select and configure multiple apps, so long as the configuration is common to all selected apps.

### Manage apps

After app setup, you can manage app settings from Workspace settings > Apps. Select the Enabled tab, locate the app you want to manage, and then select the more options menu (•••) for the app you want to manage. Review the section above for various configuration options.

# Apps capabilities by plan

PlanInteractiveSearchDeep researchSyncWriteCustom (MCP)

Free✔︎LimitedLimited✔︎

Go✔︎LimitedLimited✔︎

Plus✔︎✔︎✔︎✔︎✔︎

Pro✔︎✔︎✔︎✔︎✔︎✔︎

Business✔︎✔︎✔︎✔︎✔︎✔︎

Enterprise/Edu✔︎✔︎✔︎✔︎✔︎✔︎

Note: Some apps with search and deep research capabilities may not be available to Free/Go users; the Connect button on the listing for these apps will be greyed out.

# Supported apps and capabilities

Note: information about apps is now available in the app directory, which is the source of information for any new apps added. Refer to the [app directory listing](https://chatgpt.com/apps) for the most current information on supported apps.

# Admin controls, security, and compliance

-

Workspace owners and admins manage app availability from settings. Enterprise/Edu workspaces can configure [RBAC](https://help.openai.com/articles/11750701) for apps.

-

User conversations, including conversations using any app, are already available in the Compliance API.

-

All app calls are logged as part of the [OpenAI Compliance Logs platform](https://chatgpt.com/admin/api-reference#tag/Logs:-Apps).

-

Read more: [Compliance API for Enterprise Customers](https://help.openai.com/articles/9261474-compliance-api-for-enterprise-customers).

# FAQ

### Which models can I use with apps?

Apps are available with all models with the exception of the Pro models.

### In Enterprise, Edu, and Business workspaces, who can enable or disable apps?

Workspace owners and admins manage availability in settings. For Enterprise and Edu, owners can configure role-based access controls (RBAC).

### Are there special rate limits for apps?

No. Apps follow normal ChatGPT rate limits for your plan (external apps may impose their own caps).

### Can I remove an app from my workspace or account?

Admins and owners can disable an app from [Workspace settings](https://chatgpt.com/admin/ca). Users can disconnect apps from Settings > Apps.

Your connected third-party application may also have its own options for unlinking.

### What does ChatGPT share with apps?

After you enable an app, the app may be able to access information from ChatGPT in order to help provide context for your requests. For example, if the Canva app is enabled and you ask, “Canva, can you turn these ideas into a presentation?”, then the app may access and use relevant context from your ChatGPT conversations (such as names or taglines you have been brainstorming) in order to help generate a design based on what you have discussed.

If you have Memory turned on, when an app is responding to your requests, it may also leverage relevant information from memories to provide more customized and useful interactions for you. For example, if you have Memory turned on and you ask, “Canva, can you design a flyer for my business?”, then the app may access and use relevant context from your memories (such as the fact that you have a dog-walking business) to better customize the requested flyer. You can learn more about [Memory](https://help.openai.com/articles/8590148), including how to disable it or control individual memories.

Apps you enable may also see basic information typically shared when you visit a website, such as your IP address, device or browser type, language and region settings, and approximate location, and can use that information to improve the accuracy of your results. Approximate location is based on your IP address and reflects a general area like your city or region, not your exact street address or GPS coordinates. For example, if you have enabled the Zillow app and ask to find houses nearby, the app can use your approximate location to show listings in your area without you needing to type in a city or ZIP code.

Data shared with apps is handled according to each app’s terms of service and privacy policies, which you will see before enabling the app.

### How does ChatGPT use information from apps?

After you enable an app, ChatGPT can use information in the app as context to help provide responses. If you have [Memory](https://help.openai.com/articles/8590148) enabled in your settings, ChatGPT may remember relevant information accessed from the app. ChatGPT can also use relevant information accessed from apps to inform web search queries when ChatGPT [searches the web](https://help.openai.com/articles/9237897) to provide you with information.

### Does Voice mode support apps?

Voice mode currently does not support apps.

### Does OpenAI use information from apps to train its models?

-

For ChatGPT Business, Enterprise, and Edu customers: OpenAI does not use information accessed from connectors to train models by default.

For ChatGPT Free, Plus, Go, and Pro users: OpenAI may use information accessed from apps to train our models if your “Improve the model for everyone” setting is on. You can read more about how your data is stored and used in [this article](https://help.openai.com/articles/7730893) in our help center.

## Was this article helpful?

Submit

[ChatGPT](https://chatgpt.com)[API](https://platform.openai.com/docs/)[Service Status](https://status.openai.com)Cookie Preferences

