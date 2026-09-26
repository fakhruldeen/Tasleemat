import os
import shutil

mapping = {
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

def clean_name(name):
    # remove leading numbers like "1.1 Project Charter" -> "Project Charter"
    return name.split(" ", 1)[1] if name and name[0].isdigit() else name

def process_dir(old_base, new_base):
    for root, dirs, files in os.walk(old_base):
        json_files = [f for f in files if f.endswith(".json")]
        if not json_files:
            continue
            
        for jf in json_files:
            try:
                import json
                with open(os.path.join(root, jf), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                form_name = data.get("form_name", "")
                
                # Check mapping (use English name for lookup even if in AR dir, but JSON might have AR name. Wait.
                # In the arabic directory, form_name is in Arabic.
                # We need to map by the original directory name or the file name!
                # The file names are still in English.
            except Exception as e:
                print(e)
                continue
            
            # Use file name to determine the form name
            en_form_name = jf.replace(".json", "").replace("_", " ")
            
            if en_form_name in mapping:
                target_rel = mapping[en_form_name]
                target_dir = os.path.join(new_base, target_rel)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                
                # Copy all files from root to target_dir
                for file_in_dir in files:
                    src = os.path.join(root, file_in_dir)
                    dst = os.path.join(target_dir, file_in_dir)
                    shutil.copy2(src, dst)

print("Starting reorganization...")
process_dir("/home/mohamed/Desktop/PMOSKILL/forms", "/home/mohamed/Desktop/PMOSKILL/forms_new")
process_dir("/home/mohamed/Desktop/PMOSKILL/forms_ar", "/home/mohamed/Desktop/PMOSKILL/forms_ar_new")

shutil.copy2("/home/mohamed/Desktop/PMOSKILL/forms/parameters.md", "/home/mohamed/Desktop/PMOSKILL/forms_new/parameters.md")
shutil.copy2("/home/mohamed/Desktop/PMOSKILL/forms/parameters.md", "/home/mohamed/Desktop/PMOSKILL/forms_ar_new/parameters.md")

# Backup old ones and rename new ones
shutil.move("/home/mohamed/Desktop/PMOSKILL/forms", "/home/mohamed/Desktop/PMOSKILL/forms_old")
shutil.move("/home/mohamed/Desktop/PMOSKILL/forms_ar", "/home/mohamed/Desktop/PMOSKILL/forms_ar_old")

shutil.move("/home/mohamed/Desktop/PMOSKILL/forms_new", "/home/mohamed/Desktop/PMOSKILL/forms")
shutil.move("/home/mohamed/Desktop/PMOSKILL/forms_ar_new", "/home/mohamed/Desktop/PMOSKILL/forms_ar")

print("Reorganization successful.")
