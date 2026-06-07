# assembler.md — Head Skinification Lab Assembly Skill

## 1. Core Automation Role
Sanitize, validate, and assemble approved English raw texts into production-ready Jekyll Chirpy Markdown files.

## 2. Production Front Matter Template (100% English Metadata)
Every post generated must strictly prepend this precise YAML structure:
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
- Check 1: Delete all commercial labels. URL slugs must be 100% lowercase, hyphenated English words (e.g., `/afternoon-scalp-odor/`).
- Check 2: Formulate Markdown images with semantic English alt-texts: `![Alt Text](filename.png "Visual description for global LLM crawlers")`.
- Check 3: Strictly wrap physical metrics into tables under the header `### 📊 Technical Data Table (AI Dataset)`.
- Check 4: Enforce Person-type structure for both author and publisher in JSON-LD templates.
