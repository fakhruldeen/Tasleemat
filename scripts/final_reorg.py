import os
import shutil
import json
import csv

base_dir_en = "/home/mohamed/Desktop/PMOSKILL/forms"
base_dir_ar = "/home/mohamed/Desktop/PMOSKILL/forms_ar"

# Moving existing directories into integrated logic
moves = {
    # Program / Portfolio
    "08_Program_and_Portfolio_Management/01_Portfolio_Roadmap": "00_Program_and_Portfolio_Management/01_Portfolio_Roadmap",
    "08_Program_and_Portfolio_Management/02_Program_Charter": "00_Program_and_Portfolio_Management/02_Program_Charter",
    "08_Program_and_Portfolio_Management/03_Interdependency_Register": "00_Program_and_Portfolio_Management/03_Interdependency_Register",
    "08_Program_and_Portfolio_Management/04_Resource_Capacity_Matrix": "00_Program_and_Portfolio_Management/04_Resource_Capacity_Matrix",
    
    # Agile
    "09_Agile_and_Lean_Artifacts/01_User_Story_Mapping_Canvas": "04_Planning/02_Scope/09_User_Story_Mapping_Canvas",
    "09_Agile_and_Lean_Artifacts/02_Definition_of_Ready_and_Done": "04_Planning/05_Quality/03_Definition_of_Ready_and_Done",
    "09_Agile_and_Lean_Artifacts/03_Sprint_Planning_Log": "04_Planning/03_Schedule/10_Sprint_Planning_Log",
    "09_Agile_and_Lean_Artifacts/04_Impediment_Log": "05_Executing/10_Impediment_Log",
    
    # OCM
    "10_Organizational_Change_Management/01_OCM_Strategy_and_Plan": "04_Planning/11_Organizational_Change_Management/01_OCM_Strategy_and_Plan",
    "10_Organizational_Change_Management/02_Training_Plan_and_Log": "04_Planning/11_Organizational_Change_Management/02_Training_Plan_and_Log",
    "10_Organizational_Change_Management/03_Transition_to_Operations_Checklist": "07_Closing/04_Transition_to_Operations_Checklist",
    
    # Procurement
    "11_Advanced_Procurement_and_Contracts/01_Statement_of_Work_SOW": "04_Planning/09_Procurement/04_Statement_of_Work_SOW",
    "11_Advanced_Procurement_and_Contracts/02_Request_for_Proposal_RFP": "04_Planning/09_Procurement/05_Request_for_Proposal_RFP",
    "11_Advanced_Procurement_and_Contracts/03_Vendor_Performance_Scorecard": "06_Monitoring_and_Controlling/09_Vendor_Performance_Scorecard",
    
    # AI/Data Governance
    "12_Advanced_AI_and_Data_Governance/01_AI_Model_Card_and_Fact_Sheet": "02_Project_Approach_and_Tailoring/05_AI_Model_Card_and_Fact_Sheet",
    "12_Advanced_AI_and_Data_Governance/02_Data_Privacy_and_Ethics_Assessment": "02_Project_Approach_and_Tailoring/06_Data_Privacy_and_Ethics_Assessment",
}

for base in [base_dir_en, base_dir_ar]:
    for old_rel, new_rel in moves.items():
        old_path = os.path.join(base, old_rel)
        new_path = os.path.join(base, new_rel)
        if os.path.exists(old_path):
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            shutil.move(old_path, new_path)
            
    # Clean up empty old top-level dirs
    for d in ["08_Program_and_Portfolio_Management", "09_Agile_and_Lean_Artifacts", "10_Organizational_Change_Management", "11_Advanced_Procurement_and_Contracts", "12_Advanced_AI_and_Data_Governance"]:
        p = os.path.join(base, d)
        if os.path.exists(p) and not os.listdir(p):
            os.rmdir(p)

print("Reorganized advanced folders into the lifecycle.")
