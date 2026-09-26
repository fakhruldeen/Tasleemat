import os
import json
import csv

base_dir = "/home/mohamed/Desktop/PMOSKILL/forms"

new_structure = {
    "7 Business and Value Delivery": {
        "7.1 Business Case": {
            "is_table": False,
            "fields": {
                "Business Need": "Identify the problem or opportunity.",
                "Analysis of Situation": "Describe the current state, future state, and root causes.",
                "Recommendation": "The recommended option or approach to address the need.",
                "Evaluation Criteria": "Metrics used to measure success."
            }
        },
        "7.2 Benefits Management Plan": {
            "is_table": False,
            "fields": {
                "Target Benefits": "Expected tangible and intangible value to be gained.",
                "Strategic Alignment": "How the benefits align with the organization's strategic goals.",
                "Timeframe": "When the benefits are expected to be realized.",
                "Metrics": "How the benefits will be measured.",
                "Risks": "Risks associated with realizing the benefits."
            }
        },
        "7.3 Value Realization Register": {
            "is_table": True,
            "fields": {
                "Benefit ID": "Unique identifier for the benefit.",
                "Description": "Description of the benefit.",
                "Owner": "Person accountable for the benefit realization.",
                "Target Value": "The expected value.",
                "Actual Value": "The realized value.",
                "Status": "Status of the benefit realization."
            }
        }
    },
    "8 Tailoring and Adaptation": {
        "8.1 Tailoring Plan": {
            "is_table": True,
            "fields": {
                "Process/Artifact": "The standard process or artifact being considered.",
                "Tailoring Decision": "Added, removed, or modified?",
                "Justification": "Reasoning for the tailoring decision.",
                "Approver": "Person who approved the change."
            }
        }
    },
    "9 AI Project Management": {
        "9.1 AI Governance Plan": {
            "is_table": False,
            "fields": {
                "Ethical Guidelines": "Principles guiding the ethical use of AI on this project.",
                "Data Privacy & Security": "Protocols for protecting sensitive data used by AI models.",
                "Bias Mitigation": "Strategies to identify and reduce bias in AI outcomes.",
                "Compliance Requirements": "Legal or organizational regulations the AI must adhere to.",
                "Accountability": "Who is responsible for the AI's actions and outputs."
            }
        },
        "9.2 AI Readiness Assessment": {
            "is_table": False,
            "fields": {
                "Data Maturity": "Assessment of data quality, availability, and architecture.",
                "Technical Infrastructure": "Evaluation of compute, storage, and software capabilities.",
                "Skills & Expertise": "Availability of required AI and domain expertise.",
                "Organizational Culture": "Readiness for change and adoption of AI tools.",
                "Overall Readiness Score": "Summary score or recommendation."
            }
        },
        "9.3 AI Use Case Canvas": {
            "is_table": False,
            "fields": {
                "Problem Statement": "The specific problem the AI will solve.",
                "AI Pattern/Solution": "The type of AI model or approach (e.g., generative, predictive).",
                "Data Sources": "Where the data will come from.",
                "Value Proposition": "The expected ROI or value delivery.",
                "Key Risks": "Major risks associated with this specific use case."
            }
        },
        "9.4 Prompt Library Log": {
            "is_table": True,
            "fields": {
                "Prompt ID": "Unique identifier.",
                "Use Case": "What the prompt is used for.",
                "Prompt Text": "The actual text or structure of the prompt.",
                "Expected Output": "What a successful response looks like.",
                "Status/Version": "Current version or status of the prompt."
            }
        }
    }
}

for chapter, forms in new_structure.items():
    chapter_dir = os.path.join(base_dir, chapter.replace(" ", "_"))
    if not os.path.exists(chapter_dir):
        os.makedirs(chapter_dir)
        
    for form, data in forms.items():
        form_name = form.split(" ", 1)[1]
        form_dir = os.path.join(chapter_dir, form.replace(" ", "_"))
        if not os.path.exists(form_dir):
            os.makedirs(form_dir)
            
        fields = data["fields"]
        is_table = data["is_table"]
        
        # MD
        md_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.md")
        with open(md_path, 'w') as md:
            md.write(f"---\nForm: {form_name}\n---\n\n")
            md.write(f"# {form_name.upper()}\n\n")
            md.write("**Project Title:** `[Enter Project Title]` &nbsp;&nbsp;&nbsp;&nbsp; **Date Prepared:** `[Enter Date]`\n\n")
            md.write("---\n\n")
            
            if is_table:
                headers = list(fields.keys())
                md.write("| " + " | ".join(headers) + " |\n")
                md.write("|" + "|".join(["---" for _ in headers]) + "|\n")
                for _ in range(5):
                    md.write("| " + " | ".join(["" for _ in headers]) + " |\n")
                md.write("\n\n*Field Guidance:*\n")
                for h in headers:
                    md.write(f"- **{h}:** {fields[h]}\n")
            else:
                for field, desc in fields.items():
                    md.write(f"### {field}\n")
                    md.write(f"*{desc}*\n\n")
                    md.write("> [Enter your response here]\n\n")
                    md.write("---\n\n")
                    
        # JSON
        json_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.json")
        with open(json_path, 'w') as jf:
            json_template = {
                "_llm_instructions": f"Fill out the 'value' properties for each field in this {form_name} template based on the provided project context.",
                "form_name": form_name,
                "fields": {k: {"guidance": v, "value": ""} for k, v in fields.items()}
            }
            json.dump(json_template, jf, indent=4)
            
        # CSV
        csv_path = os.path.join(form_dir, f"{form_name.replace(' ', '_')}.csv")
        with open(csv_path, 'w', newline='') as cf:
            writer = csv.writer(cf)
            writer.writerow(["Field", "Guidance", "LLM_Generated_Value"])
            for field, desc in fields.items():
                writer.writerow([field, desc, ""])

print("Missing forms added successfully.")
