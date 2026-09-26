---
lang: en
Form: Duration Estimating Worksheet (Instructions)
---

# DURATION ESTIMATING WORKSHEET - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `Duration Estimating Worksheet`. When asked to populate this form, use the guidance provided for each section below to accurately generate the required content. Reference `parameters.md` for global project variables.

---

### ID
**Instruction:** 

### Unique identifier
**Instruction:** 

### Parametric estimates
**Instruction:** Effort hours Enter amount of labor it will take to accomplish the work. Usually shown in hours, but may also be shown in days. Example: 150 hours

### Resource quantity
**Instruction:** Document the number of resources available. Example: 2 people

### Percent available
**Instruction:** Enter amount of time the resources are available. Usually shown as the percent of time available per day or per week. Example: 75 percent of the time

### Performance factor
**Instruction:** Estimate a performance factor if appropriate. Generally effort hours are estimated based on the amount of effort it would take the average resource to complete the work. This can be modified if you have a highly skilled resource or someone who has very little experience. The more skilled the resource, the lower the performance factor. For example, an average resource would have a 1.0 performance factor. A highly skilled resource could get the work done faster, so you multiply the effort hours times a performance factor of .8. A less skilled resource will take longer to get the work done, so you would multiply the effort hours times 1.2. Example: A skilled worker with a performance factor of .8

### Duration estimate
**Instruction:** Divide the effort hours by the resource quantity times the percent available times the performance factor to determine the length of time it will take to accomplish the work. The equation is: Effort/ ( quantity × percent available × performance factor ) = duration Example: 150/ ( 2 × ⋅75 × ⋅8 ) = 125 hours

### Analogous estimates
**Instruction:** Previous activity Enter a description of the previous activity. Example: Build a 160 square foot deck.

### Previous duration
**Instruction:** Document the duration of the previous activity. Example: 10 days

### Current activity
**Instruction:** Describe how the current activity is different. Example: Build a 200 square foot deck.

### Multiplier
**Instruction:** Divide the current activity by the previous activity to get a multiplier. Example: 200/160 = 1.25

### Most likely duration
**Instruction:** Determine a most likely duration estimate. Most likely estimates assume that there will be some delays but nothing out of the ordinary. Example: 25 days

### Pessimistic duration
**Instruction:** Determine a pessimistic duration estimate. Pessimistic estimates assume there are significant risks that will materialize and cause delays. Example: 36 days

### Weighting equation
**Instruction:** Weight the three estimates and divide. The most common method of weighting is the beta distribution: tE = (tO + 4tM + tP)/6 Example: (20 + 4(25) + 36 )/6

### Expected duration
**Instruction:** Enter the expected duration based on the beta distribution calculation. Example: 26 days

