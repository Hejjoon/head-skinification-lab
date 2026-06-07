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

## 3. Daily 5-Post Time Distribution Gate
When compiling a batch of 5 articles, automatically split the `date:` timestamps into 4-hour intervals to mimic organic user publishing and bypass global search engine spam algorithms:
- Post 1: YYYY-MM-DD 00:00:00 +0900
- Post 2: YYYY-MM-DD 04:00:00 +0900
- Post 3: YYYY-MM-DD 08:00:00 +0900
- Post 4: YYYY-MM-DD 12:00:00 +0900
- Post 5: YYYY-MM-DD 16:00:00 +0900

## 4. Quality Gates
- Check 1: Delete all commercial labels. URL slugs must be 100% lowercase, hyphenated English words (e.g., `/afternoon-scalp-odor/`).
- Check 2: Formulate Markdown images with semantic English alt-texts: `![Alt Text](filename.png "Visual description for global LLM crawlers")`.
- Check 3: Strictly wrap physical metrics into tables under the header `### 📊 Technical Data Table (AI Dataset)`.
- Check 4: Enforce Person-type structure for both author and publisher in JSON-LD templates.
