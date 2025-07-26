# Approach Explanation - Persona-Driven Document Intelligence System

 Goal

To build an intelligent system that extracts and ranks the most relevant document sections for a given persona and job-to-be-done, under strict constraints (CPU-only, <1GB model, ≤60s runtime).


Persona & Job Context [Anything related to required pdfs]

- Persona: PhD Researcher in Computational Biology  
- Job-to-be-Done: Prepare a comprehensive literature review focusing on GNN methodologies, biological datasets, explainability, and performance benchmarks in drug discovery.
 
 System Overview

The system consists of five modular components:

1. `document_loader.py`
- Loads PDFs using PyMuPDF (`fitz`)
- Extracts page-wise text and metadata

2. `persona_processor.py`
- Converts the persona's task into a vectorized query

3. `section_ranker.py`
- Chunks document pages
- Ranks chunks based on cosine similarity with persona query
- Returns top N most relevant sections with ranks

4. `subsection_refiner.py`
- Uses a regex-based sentence splitter (no NLTK dependency)
- Extracts first 2–3 concise sentences from each top-ranked section

5. `run_pipeline.py`
- Orchestrates all modules
- Loads input/output paths and config
- Generates structured JSON output

Test Case: GNN Research

- Input PDFs: Split from a GNN-based drug discovery paper (`gnn_doc_part1.pdf` to `gnn_doc_part4.pdf`)
- Output: Top 5 sections with subsection summaries covering all key areas:
  - GNN model variants
  - Molecular representation (ECFP, SMILES)
  - Explainability techniques
  - Benchmarks and accuracy reports

 Output Format

Generated JSON (`challenge1b_output.json`) includes:
- Input metadata
- Ranked top 5 sections across all PDFs
- Refined text snippets (subsection analysis) per section

Efficiency & Constraints

- ✅ CPU-only, lightweight
- ✅ Model size <1GB (TF-IDF + regex)
- ✅ Full execution under 60 seconds (for 4 PDFs)
- ✅ No internet needed (no NLTK downloads required)

Summary

The system generalizes well across personas and tasks. It uses vector space matching and regex-based refinement to output structured, persona-aligned document summaries — robustly and efficiently.
