# assembler.md — Head Skinification Lab Assembly Skill

## 1. Core Automation Role
Sanitize, validate, and assemble approved English raw texts into production-ready Jekyll Chirpy Markdown files.

## 2. Production Front Matter Template (100% English Metadata)
Every post generated must strictly prepend this precise YAML structure:
```yaml
---
layout: post
title: "[Insert English Title]"
description: "[Insert English Search Meta Description]"
date: YYYY-MM-DD HH:MM:SS +0900
categories: [[Category]]
tags: [tag1, tag2]
author: scalp-bio-hacker-choi
toc: true
pin: false
comments: false
commercial_clean: true
schema_type: BlogPosting
author_type: Person
publisher_type: Person
---
```

## 3. Dynamic Sequential Scheduling Gate (Max 5 Posts/Day, 4-Hour Intervals)
When assembling new posts, the system must automatically queue them sequentially in the next available time slots to protect blog quality:
- **Scan existing posts**: Read the `_posts` folder to check the dates and times of already scheduled posts.
- **Find the next available slot**: The allowed daily slots are strictly:
  - 00:00:00 +0900
  - 04:00:00 +0900
  - 08:00:00 +0900
  - 12:00:00 +0900
  - 16:00:00 +0900
- **Sequence Assignment**: Assign the new post to the first empty slot. If all 5 slots for a day are occupied, automatically shift the new post to the `00:00:00` slot of the next calendar day.
- **Filename alignment**: Rename the post file to match the assigned schedule date (e.g. `YYYY-MM-DD-slug.md`).

## 4. Quality Gates
- **Check 1 (Slugs)**: URL slugs must be 100% lowercase, hyphenated English words (e.g., `/afternoon-scalp-odor/`). Delete all commercial labels.
- **Check 2 (Titles)**: Validate that titles follow the "Josh Formula" (Tension + Action + Outcome/Insight). Avoid boring or purely academic titles.
- **Check 3 (Conversational Q&A)**: Ensure the post contains a clean Q&A block (using `**Q.**` and `**A.**` markdown tags) to break down the core scientific concepts.
- **Check 4 (Images)**: Validate that illustrations are human-free, object-focused line art on a consistent warm-toned base block background. Formulate Markdown images with semantic alt-text: `![Alt Text](filename.png "Visual description for global crawlers")`.
- **Check 5 (Data Tables)**: Strictly wrap physical metrics into tables under the header `### 📊 Technical Data Table (AI Dataset)`.
- **Check 6 (Metadata)**: Enforce Person-type structure ("Scalp Bio-Hacker Choi") for both author and publisher in JSON-LD templates.
