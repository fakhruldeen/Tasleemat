<!-- LLM INSTRUCTIONS: Modify the Mermaid Gantt chart to visually represent the project schedule. Ensure valid Mermaid syntax. -->

<h3 align="right">{{Company_Name}}</h3>
<h2 align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 align="center">PROJECT SCHEDULE</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |  

---

```mermaid
gantt
    title Project Schedule
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    
    %% [ Add your project schedule activities here. Below is an example: ]
    section Design Phase
    WBS 1.1 Requirements    :a1, 2026-01-01, 7d
    WBS 1.2 Architecture    :a2, after a1, 10d
    
    section Build Phase
    WBS 2.1 Backend         :b1, after a2, 14d
    WBS 2.2 Frontend        :b2, after a2, 14d
    
    section Testing
    WBS 3.1 QA Testing      :c1, after b1 b2, 7d
```

---

### Signatures

| Prepared By: | Reviewed By: | Approved By: |
| :--- | :--- | :--- |
| **Name:** {{Prepared_By}} | **Name:** {{Reviewed_By}} | **Name:** {{Approved_By}} |
| **Signature:** _____________________ | **Signature:** _____________________ | **Signature:** _____________________ |
| **Date:** _________________ | **Date:** _________________ | **Date:** _________________ |

---

<div align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> PROJECT SCHEDULE | <strong>Ref:</strong> PMO-04.03.08 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
