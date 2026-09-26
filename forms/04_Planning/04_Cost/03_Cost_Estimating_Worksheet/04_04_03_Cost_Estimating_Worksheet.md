---
lang: en
Form: Cost Estimating Worksheet (Instructions)
---

# COST ESTIMATING WORKSHEET - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `Cost Estimating Worksheet`. When asked to populate this form, use the guidance provided for each section below to accurately generate the required content. Reference `parameters.md` for global project variables.

---

### ID
**Instruction:** Unique identifier, such as the WBS ID or activity ID

---

### Parametric estimates
**Instruction:** Cost variable Enter the cost estimating driver, such as hours, square feet, gallons, or some other quantifiable measure. Example: Square feet

---

### Cost per unit
**Instruction:** Record the cost per unit. Example: $9.50

---

### Number of units
**Instruction:** Enter the number of units. Example: 36

---

### Cost estimate
**Instruction:** Multiply the number of units times the cost per unit to calculate the estimate. Example: $9.50 x 36 = $342

---

### Analogous estimates
**Instruction:** Previous activity Enter a description of the previous activity. Example: Build a 160 square foot deck.

---

### Previous cost
**Instruction:** Document the cost of the previous activity. Example: $5,000

---

### Current activity
**Instruction:** Describe how the current activity is different. Example: Build a 200 square foot deck.

---

### Multiplier
**Instruction:** Divide the current activity by the previous activity to get a multiplier. Example: 200/160 = 1.25

---

### Most likely cost
**Instruction:** Determine a most likely cost estimate. Most likely estimates assume that there will be some cost fluctuations but nothing out of the ordinary. Example: $5,000

---

### Pessimistic cost
**Instruction:** Determine a pessimistic cost estimate. Pessimistic estimates assume there are significant risks that will materialize and cause cost overruns. Example: $7,500

---

### Weighting equation
**Instruction:** Weight the three estimates and divide. The most common method of weighting is the beta distribution, where c = cost: cE = ( cO + c4M + cP ) /6

---

### (
**Instruction:** 

---

### )
**Instruction:** 

---

### Example: 4,000 + 4 ( 5,000 ) /6
**Instruction:** Expected cost Enter the expected cost based on the beta distribution. Example: $5,250

