import re

def simple_sentence_split(text):
    # Split text by punctuation marks followed by whitespace and capital letters
    return re.split(r'(?<=[.!?]) +(?=[A-Z])', text)

def refine_subsections(texts: list, metas: list):
    """Extract the first 3 sentences from each relevant section."""
    result = []
    for text, meta in zip(texts, metas):
        sentences = simple_sentence_split(text)
        snippet = ' '.join(sentences[:3])  # Take first 3 sentences
        result.append({
            "document": meta["document"],
            "refined_text": snippet,
            "page_number": meta["page_number"]
        })
    return result
