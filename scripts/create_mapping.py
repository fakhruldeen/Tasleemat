import os

pdf_structure = {
    "1 Initiating Forms": [
        "1.1 Project Charter",
        "1.2 Assumption Log",
        "1.3 Stakeholder Register",
        "1.4 Stakeholder Analysis"
    ],
    "2 Planning Forms": [
        "2.1 Project Management Plan",
        "2.2 Change Management Plan",
        "2.3 Project Roadmap",
        "2.4 Scope Management Plan",
        "2.5 Requirements Management Plan",
        "2.6 Requirements Documentation",
        "2.7 Requirements Traceability Matrix",
        "2.8 Project Scope Statement",
        "2.9 Work Breakdown Structure",
        "2.10 WBS Dictionary",
        "2.11 Schedule Management Plan",
        "2.12 Activity List",
        "2.13 Activity Attributes",
        "2.14 Milestone List",
        "2.15 Network Diagram",
        "2.16 Duration Estimates",
        "2.17 Duration Estimating Worksheet",
        "2.18 Project Schedule",
        "2.19 Cost Management Plan",
        "2.20 Cost Estimates",
        "2.21 Cost Estimating Worksheet",
        "2.22 Cost Baseline",
        "2.23 Quality Management Plan",
        "2.24 Quality Metrics",
        "2.25 Responsibility Assignment Matrix",
        "2.26 Resource Management Plan",
        "2.27 Team Charter",
        "2.28 Resource Requirements",
        "2.29 Resource Breakdown Structure",
        "2.30 Communications Management Plan",
        "2.31 Risk Management Plan",
        "2.32 Risk Register",
        "2.33 Risk Report",
        "2.34 Probability and Impact Assessment",
        "2.35 Probability and Impact Matrix",
        "2.36 Risk Data Sheet",
        "2.37 Procurement Management Plan",
        "2.38 Procurement Strategy",
        "2.39 Source Selection Criteria",
        "2.40 Stakeholder Engagement Plan"
    ],
    "3 Executing Forms": [
        "3.1 Issue Log",
        "3.2 Decision Log",
        "3.3 Change Request",
        "3.4 Change Log",
        "3.5 Lessons Learned Register",
        "3.6 Quality Audit",
        "3.7 Team Performance Assessment"
    ],
    "4 Monitoring and Controlling Forms": [
        "4.1 Team Member Status Report",
        "4.2 Project Status Report",
        "4.3 Variance Analysis",
        "4.4 Earned Value Analysis",
        "4.5 Risk Audit",
        "4.6 Contractor Status Report",
        "4.7 Procurement Audit",
        "4.8 Contract Closeout Report",
        "4.9 Product Acceptance Form"
    ],
    "5 Closing": [
        "5.1 Lessons Learned Summary",
        "5.2 Project or Phase Closeout"
    ],
    "6 Agile": [
        "6.1 Product Vision",
        "6.2 Product Backlog",
        "6.3 Release Plan",
        "6.4 Retrospective"
    ]
}

new_mapping = {
    # 01 Business and Value Delivery
    "Business Case": "01_Business_and_Value_Delivery/01_Business_Case",
    "Benefits Management Plan": "01_Business_and_Value_Delivery/02_Benefits_Management_Plan",
    "Value Realization Register": "01_Business_and_Value_Delivery/03_Value_Realization_Register",

    # 02 Project Approach and Tailoring
    "Tailoring Plan": "02_Project_Approach_and_Tailoring/01_Tailoring_Plan",
    "AI Governance Plan": "02_Project_Approach_and_Tailoring/02_AI_Governance_Plan",
    "AI Readiness Assessment": "02_Project_Approach_and_Tailoring/03_AI_Readiness_Assessment",
    "AI Use Case Canvas": "02_Project_Approach_and_Tailoring/04_AI_Use_Case_Canvas",

    # 03 Initiating
    "Project Charter": "03_Initiating/01_Project_Charter",
    "Product Vision": "03_Initiating/02_Product_Vision",
    "Assumption Log": "03_Initiating/03_Assumption_Log",
    "Stakeholder Register": "03_Initiating/04_Stakeholder_Register",
    "Stakeholder Analysis": "03_Initiating/05_Stakeholder_Analysis",

    # 04 Planning
    "Project Management Plan": "04_Planning/01_Integration/01_Project_Management_Plan",
    "Change Management Plan": "04_Planning/01_Integration/02_Change_Management_Plan",
    "Project Roadmap": "04_Planning/01_Integration/03_Project_Roadmap",

    "Scope Management Plan": "04_Planning/02_Scope/01_Scope_Management_Plan",
    "Requirements Management Plan": "04_Planning/02_Scope/02_Requirements_Management_Plan",
    "Requirements Documentation": "04_Planning/02_Scope/03_Requirements_Documentation",
    "Requirements Traceability Matrix": "04_Planning/02_Scope/04_Requirements_Traceability_Matrix",
    "Project Scope Statement": "04_Planning/02_Scope/05_Project_Scope_Statement",
    "Work Breakdown Structure": "04_Planning/02_Scope/06_Work_Breakdown_Structure",
    "WBS Dictionary": "04_Planning/02_Scope/07_WBS_Dictionary",
    "Product Backlog": "04_Planning/02_Scope/08_Product_Backlog",

    "Schedule Management Plan": "04_Planning/03_Schedule/01_Schedule_Management_Plan",
    "Activity List": "04_Planning/03_Schedule/02_Activity_List",
    "Activity Attributes": "04_Planning/03_Schedule/03_Activity_Attributes",
    "Milestone List": "04_Planning/03_Schedule/04_Milestone_List",
    "Network Diagram": "04_Planning/03_Schedule/05_Network_Diagram",
    "Duration Estimates": "04_Planning/03_Schedule/06_Duration_Estimates",
    "Duration Estimating Worksheet": "04_Planning/03_Schedule/07_Duration_Estimating_Worksheet",
    "Project Schedule": "04_Planning/03_Schedule/08_Project_Schedule",
    "Release Plan": "04_Planning/03_Schedule/09_Release_Plan",

    "Cost Management Plan": "04_Planning/04_Cost/01_Cost_Management_Plan",
    "Cost Estimates": "04_Planning/04_Cost/02_Cost_Estimates",
    "Cost Estimating Worksheet": "04_Planning/04_Cost/03_Cost_Estimating_Worksheet",
    "Cost Baseline": "04_Planning/04_Cost/04_Cost_Baseline",

    "Quality Management Plan": "04_Planning/05_Quality/01_Quality_Management_Plan",
    "Quality Metrics": "04_Planning/05_Quality/02_Quality_Metrics",

    "Resource Management Plan": "04_Planning/06_Resource/01_Resource_Management_Plan",
    "Resource Requirements": "04_Planning/06_Resource/02_Resource_Requirements",
    "Resource Breakdown Structure": "04_Planning/06_Resource/03_Resource_Breakdown_Structure",
    "Responsibility Assignment Matrix": "04_Planning/06_Resource/04_Responsibility_Assignment_Matrix",
    "Team Charter": "04_Planning/06_Resource/05_Team_Charter",

    "Communications Management Plan": "04_Planning/07_Communications/01_Communications_Management_Plan",

    "Risk Management Plan": "04_Planning/08_Risk/01_Risk_Management_Plan",
    "Risk Register": "04_Planning/08_Risk/02_Risk_Register",
    "Probability and Impact Assessment": "04_Planning/08_Risk/03_Probability_and_Impact_Assessment",
    "Probability and Impact Matrix": "04_Planning/08_Risk/04_Probability_and_Impact_Matrix",
    "Risk Data Sheet": "04_Planning/08_Risk/05_Risk_Data_Sheet",
    "Risk Report": "04_Planning/08_Risk/06_Risk_Report",

    "Procurement Management Plan": "04_Planning/09_Procurement/01_Procurement_Management_Plan",
    "Procurement Strategy": "04_Planning/09_Procurement/02_Procurement_Strategy",
    "Source Selection Criteria": "04_Planning/09_Procurement/03_Source_Selection_Criteria",

    "Stakeholder Engagement Plan": "04_Planning/10_Stakeholder/01_Stakeholder_Engagement_Plan",

    # 05 Executing
    "Issue Log": "05_Executing/01_Issue_Log",
    "Decision Log": "05_Executing/02_Decision_Log",
    "Change Request": "05_Executing/03_Change_Request",
    "Change Log": "05_Executing/04_Change_Log",
    "Quality Audit": "05_Executing/05_Quality_Audit",
    "Team Performance Assessment": "05_Executing/06_Team_Performance_Assessment",
    "Lessons Learned Register": "05_Executing/07_Lessons_Learned_Register",
    "Retrospective": "05_Executing/08_Retrospective",
    "Prompt Library Log": "05_Executing/09_Prompt_Library_Log",

    # 06 Monitoring and Controlling
    "Project Status Report": "06_Monitoring_and_Controlling/01_Project_Status_Report",
    "Team Member Status Report": "06_Monitoring_and_Controlling/02_Team_Member_Status_Report",
    "Contractor Status Report": "06_Monitoring_and_Controlling/03_Contractor_Status_Report",
    "Variance Analysis": "06_Monitoring_and_Controlling/04_Variance_Analysis",
    "Earned Value Analysis": "06_Monitoring_and_Controlling/05_Earned_Value_Analysis",
    "Risk Audit": "06_Monitoring_and_Controlling/06_Risk_Audit",
    "Procurement Audit": "06_Monitoring_and_Controlling/07_Procurement_Audit",
    "Product Acceptance Form": "06_Monitoring_and_Controlling/08_Product_Acceptance_Form",

    # 07 Closing
    "Lessons Learned Summary": "07_Closing/01_Lessons_Learned_Summary",
    "Contract Closeout Report": "07_Closing/02_Contract_Closeout_Report",
    "Project or Phase Closeout": "07_Closing/03_Project_or_Phase_Closeout"
}

with open('/home/mohamed/Desktop/PMOSKILL/forms/mapping.md', 'w', encoding='utf-8') as f:
    f.write("# PMBOK Forms Mapping\n\n")
    f.write("This document maps the original forms listed in `forms.pdf` to their new logical locations in the project lifecycle directory structure.\n\n")
    
    f.write("## Original PDF Forms\n\n")
    f.write("| Original PDF Reference | Form Name | New Directory Path |\n")
    f.write("| --- | --- | --- |\n")
    
    for chapter, forms in pdf_structure.items():
        f.write(f"| **{chapter}** | | |\n")
        for form in forms:
            parts = form.split(" ", 1)
            pdf_id = parts[0]
            name = parts[1]
            new_path = new_mapping.get(name, "Not Mapped")
            f.write(f"| {pdf_id} | {name} | `{new_path}` |\n")
            
    f.write("\n## Newly Added Forms (PMBOK 8th Ed. & AI Essentials)\n\n")
    f.write("These forms were not present in the original `forms.pdf` but have been added to modernize the repository for PMBOK 8th Edition and PMI's AI Project Management standards.\n\n")
    f.write("| Form Name | New Directory Path |\n")
    f.write("| --- | --- |\n")
    
    added_forms = [
        "Business Case", "Benefits Management Plan", "Value Realization Register",
        "Tailoring Plan", "AI Governance Plan", "AI Readiness Assessment",
        "AI Use Case Canvas", "Prompt Library Log"
    ]
    
    for form in added_forms:
        new_path = new_mapping.get(form, "Not Mapped")
        f.write(f"| {form} | `{new_path}` |\n")

print("mapping.md created successfully.")
