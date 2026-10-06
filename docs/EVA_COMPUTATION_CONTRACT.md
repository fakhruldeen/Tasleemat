---
type: Guide
---
# Attested Computation Contract: Earned Value Analysis (PMO-06.05)

## 1. Concept Definition
- **Metric**: Earned Value Analysis (EVA)
- **OKF Template ID**: `PMO-06.05`
- **Purpose**: Objectively measure project performance and progress in an integrated manner.

## 2. Computation Contract
The calculation of EVA indices and variances is strictly deterministic and must not be hallucinated by LLM agents.
- **Inputs**: `BAC`, `PV`, `EV`, `AC` (Decimal values > 0)
- **Outputs**: `SV`, `CV`, `SPI`, `CPI`, `Percent_Planned`, `Percent_Earned`, `Percent_Spent`, `EAC_CPI`, `EAC_CPI_SPI`, `TCPI`
- **Rounding Rule**: Half-up to 2 decimal places.
- **Tolerance**: Exact match (± 0.01 tolerance due to float/decimal quantization).

## 3. Operational Boundaries & Assurances
- **Executor**: `tools/attested_computations/eva_calculator.py` securely computes the exact metrics.
- **Attester**: `tools/attested_computations/eva_attester.py` verifies that a generated markdown table matches the mathematical truth.
- **Evidence Storage**: Production systems executing these templates must store the attestation signatures outside the OKF Knowledge Bundle. Agents generating PMO-06.05 must rely on external math tools or the provided calculator to fill the form.

## 4. Edge Cases Handled
- Divide-by-zero on Day 1 (where `PV` or `AC` is 0) yields `0.0`.
- Missing or malformed inputs trigger an immediate attestation failure rather than generating corrupt metrics.
