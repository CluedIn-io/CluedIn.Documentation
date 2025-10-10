---
layout: cluedin
nav_order: 5
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/purview/data-factory-pipeline-run-schedule
title: Data Factory Pipeline Run Schedule
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Use this setting to automate when your pipeline runs by entering a single **schedule string** in the textbox beside the toggle. The feature supports both **Azure Data Factory** and **Microsoft Fabric** compatible ranges. You define _what_ cadence to run (minutely, hourly, daily, weekly, monthly) and _when_ within that cadence (specific days/times), plus optional start/end bounds and time zone. If a parameter is omitted, sensible defaults are applied (see tables below).

> **UI note:** You’ll paste one of the strings below into the textbox next to your toggle.

  ![pipeline-run-schedule-settings.png]({{ "/assets/images/microsoft-integration/purview/adf-cluedin-settings.png" | relative_url }})

---

## TL;DR — Quick Examples

```
Minutely:Interval=15
Hourly:Interval=2
Daily:Interval=1&Hours=[0,12,18]&Minutes=[0,30]
Weekly:Interval=1&WeekDays=[1,3,5]&Hours=[8,16]&Minutes=[0,45]
Monthly:Interval=1&MonthDays=[1,15,-1]&Hours=[9,21]&Minutes=[15,45]
```

**What these do:**
- **Minutely:Interval=15** → every 15 minutes  
- **Hourly:Interval=2** → every 2 hours  
- **Daily:Interval=1&Hours=[0,12,18]&Minutes=[0,30]** → daily at 00:00, 00:30, 12:00, 12:30, 18:00, 18:30  
- **Weekly:Interval=1&WeekDays=[1,3,5]&Hours=[8,16]&Minutes=[0,45]** → weekly on Mon/Wed/Fri at 08:00, 08:45, 16:00, 16:45  
- **Monthly:Interval=1&MonthDays=[1,15,-1]&Hours=[9,21]&Minutes=[15,45]** → monthly on 1st, 15th, and end-of-month at 09:15, 09:45, 21:15, 21:45  

> **Cross-platform tip:** `MonthDays=[-1]` (end-of-month) is **Azure-only**. If you also target Fabric, prefer explicit day values (e.g., compute EOM externally and pass `1–31` only).

---

## Syntax

```
<Frequency>:<Key>=<Value>[&<Key>=<Value>...]
```

- **Frequency**: one of `Minutely | Hourly | Daily | Weekly | Monthly`
- **Key/Value pairs**: separated by `&`
- **Arrays**: bracketed, comma-separated (e.g., `[1,3,5]`)
- **Times**: specified via `Hours` and `Minutes` arrays
- **Optional bounds**: `StartDateTime`, `EndDateTime`
- **Optional**: `TimeZone`

### Formal-ish Grammar (EBNF)

```
schedule     = frequency ":" params ;
frequency    = "Minutely" | "Hourly" | "Daily" | "Weekly" | "Monthly" ;
params       = pair | pair "&" params ;
pair         = key "=" value ;
key          = "Interval" | "WeekDays" | "MonthDays" | "Hours" | "Minutes"
             | "StartDateTime" | "EndDateTime" | "TimeZone" ;
value        = integer | array | datetime | string ;
array        = "[" elements "]" ;
elements     = integer | integer "," elements ;
integer      = "-"? DIGITS ;
datetime     = DATE | DATE "T" TIME ;      // e.g., 10-08-2025 or 10-08-2025T14:30
DATE         = "MM-DD-YYYY" ;              // DateFormat = MM-dd-yyyy
TIME         = "HH:MM" ;                   // TimeFormat = HH:mm (24-hour clock)
```

---

## Frequencies & Allowed Parameters

### Minutely
- **Keys**: `Interval`, `StartDateTime`, `EndDateTime`, `TimeZone`
- **Limits**:
  - **Azure**: `Interval` = `1–720000`
  - **Fabric**: `Interval` = `1–720`

### Hourly
- **Keys**: `Interval`, `StartDateTime`, `EndDateTime`, `TimeZone`
- **Limits**:
  - **Azure**: `Interval` = `1–12000`
  - **Fabric**: `Interval` = `1–72`

### Daily
- **Keys**: `Interval`, `Hours`, `Minutes`, `StartDateTime`, `EndDateTime`, `TimeZone`
- **Limits**:
  - **Azure**: `Interval` = `1–500`
  - **Fabric**: `Interval` is not supported
  - `Hours` = `0–23`, `Minutes` = `0–59`

### Weekly
- **Keys**: `Interval`, `WeekDays`, `Hours`, `Minutes`, `StartDateTime`, `EndDateTime`, `TimeZone`
- **Limits**:
  - **Azure**: `Interval` = `1–71`
  - **Fabric**: `Interval` is not supported
  - `WeekDays` = `[1–7]` where `1=Mon … 7=Sun`
  - `Hours` = `0–23`, `Minutes` = `0–59`

### Monthly
- **Keys**: `Interval`, `MonthDays`, `Hours`, `Minutes`, `StartDateTime`, `EndDateTime`, `TimeZone`
- **Limits**:
  - **Azure**: `Interval` = `1–16`
  - **Fabric**: `Interval` = `1–12`
  - **Azure MonthDays**: `1–31` and `-1` for **End of Month**
  - **Fabric MonthDays**: `1–31` (no `-1`)
  - `Hours` = `0–23`, `Minutes` = `0–59`

---

## Parameter Keys & Defaults

| Key             | Type      | Meaning                                                                 | Default if Omitted                                                                 |
|-----------------|-----------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `Interval`      | Integer   | Frequency step (e.g., every _n_ minutes/hours/days/weeks/months)        | `1`                                                                                |
| `WeekDays`      | Int[]     | Days of week (`1=Mon … 7=Sun`) for `Weekly`                              | Current day of week (1–7)                                                          |
| `MonthDays`     | Int[]     | Days of month (`1–31`, **Azure** also `-1` for EOM) for `Monthly`        | Today’s day of month                                                               |
| `Hours`         | Int[]     | Hours in 24-hr clock (`0–23`)                                            | Current hour                                                                       |
| `Minutes`       | Int[]     | Minutes (`0–59`)                                                         | Current minute                                                                     |
| `StartDateTime` | Date/Time | `MM-dd-yyyy` or `MM-dd-yyyyTHH:mm`                                       | Current date/time                                                                  |
| `EndDateTime`   | Date/Time | Upper bound for firing                                                   | Minutely/Hourly: end of **day**; Daily/Weekly: end of **month**; Monthly: end of **year** |
| `TimeZone`      | String    | IANA/Windows time zone ID (e.g., `Asia/Manila`, `Pacific Standard Time`) | Current system time zone                                                           |

> **Tip:** If you provide `Hours` without `Minutes`, the current minute is used; likewise for `Minutes` without `Hours`.

---

## Date/Time & Time Zone Notes

- **DateFormat** = `MM-dd-yyyy` (e.g., `10-08-2025`)  
- **TimeFormat** = `HH:mm` (e.g., `14:30`)  
- `StartDateTime`/`EndDateTime` accept `MM-dd-yyyy` or `MM-dd-yyyyTHH:mm`.  
- **Time Zone**: If omitted, your server/app’s current time zone is assumed.  
- **Bounds behavior**: Triggers occur **on or after** `StartDateTime` and **before or on** `EndDateTime` (inclusive end varies by implementation; see defaults above).

**Examples**
```
Daily:Interval=1&Hours=[6,18]&Minutes=[0]&StartDateTime=10-01-2025T06:00&TimeZone=Asia/Manila
Weekly:Interval=2&WeekDays=[2]&Hours=[9]&Minutes=[30]&EndDateTime=12-31-2025
Monthly:Interval=1&MonthDays=[-1]&Hours=[23]&Minutes=[59]&TimeZone=UTC
```

---

## Platform Differences (Azure vs Fabric)

Some ranges differ by platform:

- **Interval (Minutely)**: Azure `1–720000`, Fabric `1–720`  
- **Interval (Hourly)**: Azure `1–12000`, Fabric `1–72`  
- **Interval (Monthly)**: Azure `1–16`, Fabric `1–12`  
- **End-of-Month (`-1`)**: **Azure only** for `MonthDays`

> If you target **both** platforms, avoid `MonthDays=-1` and pick explicit end-of-month dates where possible (e.g., compute 28–31 externally).

---

## How Combinations Work

- **Daily/Weekly/Monthly** fire at **cartesian combinations** of `Hours × Minutes`.  
  - `Hours=[8,16]` and `Minutes=[0,45]` → `08:00, 08:45, 16:00, 16:45`.
- **Weekly** uses `WeekDays × Hours × Minutes`.  
- **Monthly** uses `MonthDays × Hours × Minutes`.  
- If a specified day doesn’t exist in a month (e.g., `31` in February), the run **skips** that date.

---

## Validation Checklist

- ✅ `Frequency` is one of the five allowed values  
- ✅ Numeric ranges fit the target platform (Azure/Fabric)  
- ✅ Arrays are bracketed and comma-separated, no spaces needed (`[1,3,5]`)  
- ✅ No unsupported values (e.g., `MonthDays=-1` and `Interval` for `Daily` & `Weekly` on Fabric)  
- ✅ `StartDateTime ≤ EndDateTime` (if both provided)  
- ✅ `TimeZone` is a valid ID (e.g., `Asia/Manila`, `UTC`, `Pacific Standard Time`)

---

## More Examples

**Every 10 minutes from now until end of day**
```
Minutely:Interval=10
```

**Every 4 hours between two dates in UTC**
```
Hourly:Interval=4&StartDateTime=10-08-2025T00:00&EndDateTime=10-15-2025T23:59&TimeZone=UTC
```

**Daily at 07:30 only**
```
Daily:Hours=[7]&Minutes=[30]
```

**Weekly on weekends at the top of the hour**
```
Weekly:WeekDays=[6,7]&Minutes=[0]
```

**Monthly on 1st, 15th, 30th at 09:00 and 18:00**
```
Monthly:MonthDays=[1,15,30]&Hours=[9,18]&Minutes=[0]
```

**Azure only: Monthly on End-of-Month at 23:59**
```
Monthly:MonthDays=[-1]&Hours=[23]&Minutes=[59]
```

---

## FAQ

**Q: What happens if I omit `Hours` and `Minutes` on Daily/Weekly/Monthly?**  
A: They default to the current hour/minute at the time you enable/save the schedule.

**Q: How are `StartDateTime` and `EndDateTime` interpreted?**  
A: They bound execution to that window, using the specified (or default) `TimeZone`.

**Q: Can I specify seconds?**  
A: Seconds are not part of the configured formats. Use `HH:mm` for time and, if needed, schedule more frequent runs instead.

---

## Verification & Screenshots

> Use these images to document and verify end-to-end behavior. Replace the placeholders with actual screenshots from your environment.

### 1) CluedIn: Schedule Created (Success Notification)
- **What to capture:** The in-app notification/toast confirming that the schedule has been created successfully.
- **When to capture:** Immediately after clicking **Save** with a valid schedule string.
- **Expected text (example):** “Pipeline run schedule created for '*pipelineName*'.”

  ![cluedin-schedule-success.png]({{ "/assets/images/microsoft-integration/purview/cluedin-schedule-success.png" | relative_url }})

---

### 2) Fabric / Azure: Schedule Artifact
- **What to capture:** The corresponding schedule/trigger created in **Microsoft Fabric** and/or **Azure Data Factory**.
- **When to capture:** After the CluedIn success message appears, open the target platform and navigate to the trigger/schedule details.
- **Fabric path (example):** _Workspace → Pipelines → (Pipeline Name) → Schedules → (Your Schedule)_  
- **Azure Data Factory path (example):** _Authoring → Triggers → (Trigger Name) → Schedule_
  
**Fabric:**

  ![fabric-schedule-created.png]({{ "/assets/images/microsoft-integration/purview/fabric-schedule-created.png" | relative_url }})

**Azure Data Factory:**

  ![adf-schedule-created.png]({{ "/assets/images/microsoft-integration/purview/adf-schedule-created.png" | relative_url }})

---

### 3) CluedIn: Schedule Disabled Notification (Toggle Off)
- **What to capture:** The in-app notification confirming the schedule has been **disabled** after the settings toggle is turned off (or when the textbox is cleared and saved).
- **When to capture:** Immediately after disabling the setting.
- **Expected text (example):** “Pipeline run schedule disabled.”

  ![cluedin-schedule-disabled.png]({{ "/assets/images/microsoft-integration/purview/cluedin-schedule-disabled.png" | relative_url }})
---