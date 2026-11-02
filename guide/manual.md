# 📗 degenOS Full Manual

The complete reference: the system, every command, when and why to use it, how it works under the hood, and how to fix things. For the one-page version, see the [Quickstart](quickstart.md).

**The hierarchy:** 🧠 **degenOS** (the OS / knowledge core + orchestrator) → 📱 **Grace** (interface) → 🌙 **LifeBot** (life) → 💼 **BizBot** (business).

---

## Contents
1. [How it's built](#how-its-built)
2. [degenOS — the OS & knowledge core](#degenos)
3. [Grace — the interface agent](#grace)
4. [LifeBot & BizBot — the domain agents](#the-domain-agents)
5. [Command reference](#command-reference)
6. [The learning loops](#the-learning-loops)
7. [Delivery: how things reach you](#delivery)
8. [The automation schedule](#the-automation-schedule)
9. [Privacy & safety model](#privacy--safety)
10. [Troubleshooting](#troubleshooting)

---

## How it's built

degenOS is **plain scripts + scheduled jobs + an LLM**, deliberately boring infrastructure:

- **Project folders**, one per component, each with a `CLAUDE.md` (its standing instructions), command prompts, and helper scripts.
- **A schema-constants file** in each project is the single source of truth for data layout — nothing hardcodes column letters or IDs elsewhere.
- **Scheduled jobs** (macOS `launchd`) fire the routines at set times. A deterministic Python layer handles anything that must be reliable (scheduling, calendar, reminders); the LLM handles judgment (drafting, triage, synthesis).
- **Telegram** is the I/O surface — a user session for silent delivery, a bot (Grace) for interactive notifications.
- **Google Sheets** hold CRM state; an **Obsidian vault** is the degenOS knowledge core; **Gmail/Calendar/iMessage/Contacts** are read-only inputs (except drafts, which are written but never sent).

No servers, no monthly fees. The trade-off: it runs while your Mac is on.

---

## degenOS

The OS and the knowledge core. It turns raw input into usable thinking: you drop a note, link, or voice memo; degenOS sharpens it, files it, finds non-obvious connections to past notes, and when a theme has enough support, drafts content in your voice. It runs daily research pulses on topics you care about — and, crucially, it hosts the **daily orchestrator** (`morning`) that pulls the whole system together into one ranked dashboard. **Use it when:** you have an idea to capture, a topic to research, content to produce — or just let its morning routine run. Home: an Obsidian vault.

---

## Grace

Grace is a Telegram bot — the one part of the system that **notifies** you and **listens** in real time.

**Two channels, on purpose:**
- **Saved Messages** (silent): briefs, digests, voice notes, scheduled reminders. No buzz.
- **Grace** (notifies): questions that need your input, urgent alerts, and your commands.

**The feedback loop** is the heart of it. When any component hits something only you can answer — an empty CRM field, an unclear status, a fact a draft needs — it asks Grace **one discrete question**. You reply to that message. Deterministic answers (yes/no, a date, a status) get written straight into the right place; open-ended answers route to the next run to apply with full context. Capped so you're never spammed (currently 15 questions/day).

This is how the system fills its own gaps: instead of hoarding questions for a weekly sit-down, it asks in the moment and learns continuously.

---

## The domain agents

### 🌙 LifeBot — life
Protects your time and relationships. It triages multiple email inboxes, drafts replies into your Drafts folder, manages calendar time-blocks (including wellness), maintains a **personal CRM** of friends and contacts with gentle "you haven't talked to X in a while, here's an opener" nudges, and scrapes newsletters/messages for things worth keeping. **Use it when:** ...you don't. It mostly runs itself and reports each evening.

### 💼 BizBot — business
Your outreach operator. It reads your CRM, ranks who needs attention today, and writes personalized drafts — never generic, always grounded in real context about the person. It tracks which message styles actually get replies and shifts future drafts toward what works. **Use it when:** you're doing outreach, following up, prepping for a call, or want a pipeline read.

---

## Command reference

### Daily / automatic (you rarely type these)
| Command | Owner | What it does | When it runs |
|---|---|---|---|
| `morning` | degenOS | Inbox + research + CRM scan → one ranked dashboard | 7:45 AM auto |
| `evening-brief` | LifeBot | Inbox triage, reply drafts, calendar prep, people nudges | 8:00 PM auto |
| `day-schedule` | LifeBot | Time-blocks + smart phone reminders | 7:30 AM auto |

### Weekly
| Command | Owner | What it does | When |
|---|---|---|---|
| `network-weave` | LifeBot | Intros (double-opt-in), gap-bridges, idea→action | Sunday |
| `weekly-debrief` | BizBot | ~10 quick questions → updates the playbooks | Monday |
| `life-debrief` | LifeBot | Silent: learns your voice from sent/edited drafts | Monday |
| CEO Report | all | One cross-system picture of the week | Friday |

### On-demand (type when you want them)
| Command | Owner | Use it when |
|---|---|---|
| `meeting-prep [name]` | BizBot | You have a call and want a full brief on them |
| `enrich-contact [name]` | BizBot | You want deep research on one person |
| `reply-to [name]` | BizBot | A reply needs a thoughtful drafted response |
| `grant-draft [name]` | BizBot | Drafting a grant/application |
| `unsubscribe-audit` | LifeBot | An inbox has gotten noisy |
| `telegram-scan` | LifeBot | Pull news/alpha from your channels |
| `social-checkin` | LifeBot | Refresh contacts from LinkedIn/Facebook |
| `wellness` | LifeBot | See your habit & time-block adherence |
| `crm-seed` | LifeBot | First-run: build the personal CRM from your history |
| `auto-research [topic]` | degenOS | Deep-dive a question |
| `think-deep [question]` | degenOS | Structured reasoning for a hard decision |
| `generate-brief` / `write` / `expand` / `optimize` | degenOS | The content pipeline, stage by stage |

### Grace text commands (natural language)
`remind me [when] to [thing]` · `capture: [note]` · `skip [block] today` · `discrete [Nh/on/off]` · `status` — plus just replying to her questions.

---

## The learning loops

Three loops make the system improve instead of just repeat:

1. **Outreach playbook** (BizBot) — every draft is tagged; replies are tracked; the win-rate by message style feeds back so the best-performing angle leads next time. Cold patterns get retired.
2. **Content patterns** (degenOS) — published pieces' engagement updates a "what works" file that shapes future writing. Reply-winning outreach angles also flow here as validated demand signals.
3. **Voice adaptation** (LifeBot) — the system compares the drafts it wrote against what you actually sent. Your edits teach it your real voice, per audience (crisp for business, warm for friends).

Plus the **block ledger** (LifeBot): it watches which calendar blocks you keep, move, or delete, and adjusts — delete the gym block enough times and it stops scheduling it; consistently move it to 6pm and it adopts 6pm.

---

## Delivery

Every brief reaches you three ways so nothing is missed:
1. **A file** saved to the degenOS vault (searchable archive).
2. **Email** (full content).
3. **Telegram** — as an **expandable digest** (each section taps open; drafts are full text, ready to copy) plus the file attached.

Daily briefs also get a **voice note** (free, generated on-device) so you can listen while making coffee. Visual reports (wellness, CEO report, meeting prep) arrive as **image cards** that display inline.

---

## The automation schedule

```
7:25 AM   Mac wakes (so nothing is missed)
7:30 AM   Day scheduler (LifeBot) — audit yesterday's blocks, place today's, schedule reminders
7:45 AM   Morning dashboard (degenOS) — top actions + pipeline delta
all day   Reminders fire · Grace listens (15-min command checks + instant replies)
8:00 PM   Evening brief (LifeBot) — triage, drafts, prep, people
Sunday    Network weave
Monday    Weekly debrief (you) + life debrief (silent)
Friday    CEO report
```

Headless runs have a hard timeout so a network blip can never leave one hanging.

---

## Privacy & safety

- **Nothing sends without you.** All messages are drafts; you hit send. (The only exception is standard one-click email unsubscribes.)
- **A hard do-not-contact list** is enforced in code — certain people never appear in any draft, reminder, or report, period.
- **Discretion mode** strips personal content from voice briefs on command (for when you're not alone), auto-reverting after a set window.
- **Personal vs. business firewall** — friends are never treated as sales leads; the two CRMs don't cross without your say-so.
- **Voice notes assume they're overheard** — sensitive relationship content stays in text, which you read privately.
- **Data stays yours** — on your machine and in your own Google/Telegram accounts. The public repo carries none of it.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| No morning dashboard | Mac was asleep at 7:45 | Runs on next wake; or trigger manually |
| Grace not responding | Bot token/session lapsed | Re-check the bot connection |
| Reminders not firing | Telegram session expired | Re-auth the user session |
| Email actions failing | OAuth token expired | Re-run the account auth (a pre-flight check prints the exact command) |
| A brief used the wrong voice | Voice not installed where the engine can see it | Install it under Accessibility → Spoken Content (not Siri) |
| Pipeline numbers look wrong | Stage labels differ per CRM tab | The counter is tab-aware; verify the tab's stage set |

A **pre-flight check** runs before the main routines and reports every integration's status with the exact fix command, so failures surface early rather than mid-run.

---

*This manual describes the system generically. Operational specifics and personal data live in private repos.*
