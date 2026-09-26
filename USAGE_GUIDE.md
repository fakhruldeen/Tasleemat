# 📚 Tasleemat Usage Guide

Welcome to the comprehensive usage guide for the Tasleemat PMO Toolkit. 

## Understanding the 4-File System
Inside every artifact directory (e.g., `01_Project_Charter`), you will find four closely related files. Here is how to use each one:

### 1. The Guide (`_Guide.md`)
Start here. This document explains the **What, Why, When, Who, and How** of the artifact based on modern project management standards. It includes a link to download the other files.

### 2. The Printable Template (`_Template.md`)
This is the final, visually appealing document. It contains an HTML-formatted table layout with signature blocks at the bottom and a document reference number at the top. 
* **Use Case:** Export this to PDF for physical signatures, or copy/paste it into a company wiki (like Confluence or Notion).

### 3. The LLM Prompt (`.md`)
This file contains the system instructions for Large Language Models (LLMs). It breaks down exactly what information belongs in each field of the template.
* **Use Case:** Copy the contents of this file and paste it into ChatGPT alongside your project parameters to get a highly accurate draft.

### 4. The Data Schema (`.json` / `.csv`)
For developers and data analysts, these files contain the exact structural requirements of the form in a machine-readable format.
* **Use Case:** Use the CSV to import historical project data into Excel/PowerBI dashboards. Use the JSON to build automated API pipelines that generate forms dynamically.

## 🤖 Step-by-Step AI Generation Workflow
To generate a professional PMO document using AI:
1. Open `/forms/parameters.md` and fill out your project details. Copy the entire file.
2. Go to ChatGPT/Claude and paste the parameters. Tell the AI: *"These are my global project parameters. Keep them in memory."*
3. Open the `.md` prompt file of the document you want to create (e.g., `Project_Charter.md`). Copy the entire text.
4. Paste it into the AI and say: *"Fill out this document based on the global parameters and the following rough notes: [Insert your rough meeting notes here]."*
5. The AI will output a fully populated Markdown document that matches the exact structure of your `_Template.md`!
