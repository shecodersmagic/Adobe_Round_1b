from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_sections(documents: dict, query: str, top_k: int = 5):
    """
    Rank all pages in all documents by their relevance to the query.
    Returns: top_k section metadata and corresponding text content.
    """
    all_texts = []
    metadata = []

    for doc_name, pages in documents.items():
        for i, text in enumerate(pages):
            # Use first non-empty line as title if available
            lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
            title = lines[0][:80] if lines else "Untitled Section"
            all_texts.append(text)
            metadata.append({
                "document": doc_name,
                "section_title": title,
                "page_number": i + 1  # this will be moved after importance rank in formatting
            })

    # TF-IDF based similarity scoring
    tfidf = TfidfVectorizer(stop_words='english').fit_transform(all_texts + [query])
    query_vec = tfidf[-1]
    doc_vecs = tfidf[:-1]
    scores = cosine_similarity(query_vec, doc_vecs)[0]

    top_indices = sorted(range(len(scores)), key=lambda i: -scores[i])[:top_k]
    ranked = [metadata[i] for i in top_indices]
    for rank, meta in enumerate(ranked, 1):
        meta['importance_rank'] = rank

    # Reorder metadata keys for required output format
    for section in ranked:
        reordered = {
            "document": section["document"],
            "section_title": section["section_title"],
            "importance_rank": section["importance_rank"],
            "page_number": section["page_number"]
        }
        section.clear()
        section.update(reordered)

    top_texts = [all_texts[i] for i in top_indices]

    return ranked, top_texts
