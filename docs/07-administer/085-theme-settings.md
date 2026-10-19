---
layout: cluedin
title: Theme settings
parent: Administer
nav_order: 85
permalink: /administer/theme-settings
content_type: reference
tags: ["administration", "settings", "theme", "branding", "celebrations"]
last_modified: 2026-10-19
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

**Theme** is a page under **Organization Settings** (available from the administration menu) where you choose how CluedIn's interface looks for your organization.

{: .important }
The sign-in page's illustration cycles through a different animated color scheme each day of the week. This is automatic and not configurable from this page.

![Theme settings page, showing the Color Scheme list of presets and the Accent Color and Sidebar Background Color pickers]({{ "/assets/images/administration/theme-settings/theme-settings-page.png" | relative_url }})

## Color Scheme

The **Color Scheme** section lists the preset themes you can apply to your organization:

| Preset | Description |
|---|---|
| CluedIn | The default CluedIn color scheme. |
| CluedIn Radiant | A brighter, blue-to-violet variation of the default scheme. |
| Azure | A scheme that matches Microsoft Azure's color palette. |
| Midnight | A dark indigo scheme. |
| Forest | A green scheme. |
| Sunset | A warm orange and red scheme. |
| Grape | A purple scheme. |
| Custom | Lets you pick your own primary color instead of using a preset. |

Selecting a preset immediately updates the interface so you can preview it before saving. If you select **Custom**, a color picker appears so you can choose the primary color CluedIn uses throughout the interface.

![The Theme settings page with the Forest preset selected, showing the sidebar and header updated to the Forest color scheme]({{ "/assets/images/administration/theme-settings/theme-settings-forest-preview.png" | relative_url }})

## Accent Color and Sidebar Background Color

Below the color scheme list, two additional settings let you fine-tune the sidebar independently of the preset you selected:

- **Accent Color** overrides the sidebar's accent color — the color used for the active menu item.
- **Sidebar Background Color** overrides the sidebar's background color.

Both settings are optional and apply on top of whichever preset is selected, so you can, for example, keep the **Sunset** preset but use your own brand color for the sidebar accent. Each picker starts out showing the current preset's own color. Select **Use theme default** next to a picker to clear your override and go back to the color the selected preset uses by default.

## Save and apply your changes

Select **Save** to apply your changes. CluedIn validates that every color is a valid hex color; if a value is invalid, CluedIn shows an error and does not save your changes.

Once saved, the selected color scheme — including a **Custom** primary color — applies everywhere, including the sign-in page, before anyone in your organization signs in. **Accent Color** and **Sidebar Background Color** apply throughout the interface once someone is signed in. In all cases, anyone with an open session sees the change after refreshing the page.

## Scheduled theme

Below the color settings, the **Scheduled theme** section lets CluedIn switch color schemes automatically by time of day instead of always using the single scheme chosen above.

![Scheduled theme section, enabled, with Day theme and Night theme dropdowns and Day/Night starts at time pickers configured]({{ "/assets/images/administration/theme-settings/theme-settings-scheduled-theme-dropdowns.png" | relative_url }})

Turn on **Enable scheduled theme**, then set:

| Setting | Description |
|---|---|
| Day theme | The preset (from the same list as **Color Scheme**, excluding **Custom**) applied during the day. Choose it from the dropdown. |
| Night theme | The preset applied during the night. Choose it from the dropdown. |
| Day starts at | The local time of day the day theme is applied. Pick a time from the list, or type one directly in 24-hour `HH:mm` format. |
| Night starts at | The local time of day the night theme is applied. Pick a time from the list, or type one directly in 24-hour `HH:mm` format. |

Each time a signed-in user loads CluedIn, it compares their device's local time against these settings and applies whichever theme is currently active. It's checked again on every page load or refresh, but not continuously while a page stays open, so a session that's been open across a day/night boundary picks up the new theme the next time it loads a page rather than switching automatically mid-session.

Select **Save** at the bottom of this section to apply it — this is a separate save action from the **Color Scheme** settings above. The scheduled theme does not apply to the sign-in page, since nobody is signed in there yet to resolve a local time against.

## Celebrations

Below the schedule, the **Celebrations** section lets you choose whether completing actions in CluedIn plays a small celebratory effect.

![Celebrations section, with the Celebration mood dropdown set to Calm]({{ "/assets/images/administration/theme-settings/theme-settings-celebrations.png" | relative_url }})

Choose a **Celebration mood** from the dropdown:

| Mood | Effect |
|---|---|
| Off | No effect — the default. |
| Excited | A confetti burst. |
| Happy | A few balloons rising up the screen. |
| Calm | A brief, subtle glow — no particles. |

The effect plays for every signed-in user in your organization whenever they complete an action that shows a success message, such as saving a setting or creating a record. Select **Save** to apply your choice — this is a separate save action from the sections above it. If your device has a reduced-motion preference turned on, CluedIn skips the effect regardless of the mood selected.
