---
type: Skill
name: pmo-governance
description: Bilingual PMO governance, artifact scaffolding, and data validation using Tasleemat.
---

# PMO Governance Skill

This skill equips agents with standard operating procedures for managing deliverables using the Tasleemat PMO Operating System.

## Workflow
1. Identify the required deliverable ID using `tasleemat_list_artifacts` or `tasleemat_get_artifact`.
2. Retrieve the official template and practitioner guide using `tasleemat_get_asset`.
3. Populate the deliverable adhering to Document Control headers and audit trail hashes.
4. Validate structured payloads for supported forms (`PMO-01.01`, `PMO-03.01`, `PMO-04.08.02`, `PMO-06.01`, `PMO-07.03`) using `tasleemat_validate_data`. Unsupported forms return status='unavailable'.
