import os
import json

from app.document_loader import load_documents
from app.persona_preprocessor import build_persona_query
from app.sections_ranker import rank_sections
from app.subsection_refiner import refine_subsections
from app.utils import get_timestamp

def run_for_folder(input_folder, config_path, output_path, tag):
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Load documents and persona/job
    documents = load_documents(input_folder)
    persona = config['persona']
    job_to_be_done = config['job_to_be_done']

    # Build query and rank sections
    query = build_persona_query(persona, job_to_be_done)
    ranked_sections, top_texts = rank_sections(documents, query)

    # Refine top subsections
    refined_output = refine_subsections(top_texts, ranked_sections)

    # Create final output JSON
    output = {
        "metadata": {
            "input_documents": list(documents.keys()),
            "persona": persona,
            "job_to_be_done": job_to_be_done,
            "processing_timestamp": get_timestamp()
        },
        "extracted_sections": ranked_sections,
        "subsection_analysis": refined_output
    }

    os.makedirs(output_path, exist_ok=True)
    out_filename = os.path.join(output_path, f"challenge1b_output_{tag}.json")
    with open(out_filename, 'w') as f:
        json.dump(output, f, indent=4)

    print(f"[✔] Output saved to: {out_filename}\n")


if __name__ == '__main__':
    input_root = "input"
    config_map = {
        "academic_research": "config_academic.json",
        "business_analysis": "config_business.json",
        "educational_content": "config_education.json"
    }
    output_dir = "output"

    for folder, config_file in config_map.items():
        input_folder = os.path.join(input_root, folder)
        config_path = os.path.join(input_root, config_file)
        print(f"\n[⚙] Running analysis for: {folder}")
        run_for_folder(input_folder, config_path, output_dir, folder)
