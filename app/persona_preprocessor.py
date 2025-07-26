from typing import Tuple

def build_persona_query(persona: str, job: str) -> str:
    """Combine persona and job into a structured query string."""
    query = (
        f"You are assisting a persona with the following role: {persona}. "
        f"Their specific task is: {job}. "
        f"Extract and prioritize the most relevant sections from the given documents that help accomplish this task."
    )
    return query
