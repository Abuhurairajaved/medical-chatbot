import os
import xml.etree.ElementTree as ET
import pandas as pd
import json

# Paths
medquad_dir = r"C:\Users\abuhuraira.javaid\Downloads\MedQuAD"
output_dir = r"D:\chatbot\dataset"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Initialize data storage
data_list = []

# Loop through each folder in MedQuAD
for folder in os.listdir(medquad_dir):
    folder_path = os.path.join(medquad_dir, folder)
    
    if os.path.isdir(folder_path):
        # Process each XML file
        for file in os.listdir(folder_path):
            if file.endswith(".xml"):
                file_path = os.path.join(folder_path, file)
                
                # Parse XML
                tree = ET.parse(file_path)
                root = tree.getroot()
                
                doc_id = root.attrib.get("id", "Unknown")
                focus = root.find("Focus").text if root.find("Focus") is not None else "Unknown"

                # Extract Q&A Pairs
                for qapair in root.findall(".//QAPair"):
                    question = qapair.find("Question").text if qapair.find("Question") is not None else ""
                    answer = qapair.find("Answer").text if qapair.find("Answer") is not None else ""
                    qtype = qapair.find("Question").attrib.get("qtype", "general") if qapair.find("Question") is not None else "general"

                    data_list.append({
                        "document_id": doc_id,
                        "topic": focus,
                        "question": question,
                        "answer": answer,
                        "qtype": qtype,
                        "source": folder
                    })

# Save as CSV
csv_path = os.path.join(output_dir, "medquad_dataset.csv")
df = pd.DataFrame(data_list)
df.to_csv(csv_path, index=False, encoding="utf-8")

# Save as JSON
json_path = os.path.join(output_dir, "medquad_dataset.json")
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

print(f"Dataset saved at:\nCSV: {csv_path}\nJSON: {json_path}")
