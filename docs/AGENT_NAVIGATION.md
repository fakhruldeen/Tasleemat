---
type: Guide
---
# Tasleemat AI Agent Navigation Guidance

## Overview
This document specifies how LLMs, RAG systems, and autonomous agents should navigate the Tasleemat Open Knowledge Format (OKF) v0.2 bundle. The `forms/` directory operates as a bilingual, machine-readable Knowledge Graph.

## 1. Concept Identification & Retrieval
- **Form ID (`form_id`)**: The definitive primary key for any PMO artifact (e.g., `PMO-03.01`). Use this to resolve relationships, regardless of directory structure or language.
- **Tokens (`token_pointer`)**: Every markdown concept contains a `token_pointer` (e.g., `_tokens/...npy`). If your agent architecture supports pre-computed arrays (like Qwen2.5/tiktoken), load the `.npy` file directly to bypass tokenization and reduce Time-To-First-Token (TTFT) by roughly 30%.

## 2. Bilingual Traversal
Do not assume English and Arabic templates share the exact same filepath structure. To locate a translation:
1. Extract the `form_id` from the current document.
2. Query the bundle for the document matching `form_id == target` AND `language == 'ar'` (or `'en'`).
*Never fabricate translation paths.*

## 3. Form Completion
- Search for HTML comments starting with `<!-- LLM INSTRUCTIONS:`.
- These comments dictate how to map user notes into the flat markdown form.
- Explicitly mark unknown fields as `[ Requires Human Input ]`. Never hallucinate project data.

## 4. Currency and Trust
- **Status (`status`)**: Only generate documents based on `status: approved` templates. Warn users if they request generation against a `draft` or `deprecated` template.
- **Evidence (`sources`)**: If a form references a framework (e.g., PMBOK), the `sources` array in the frontmatter contains the definitive citation keys.
