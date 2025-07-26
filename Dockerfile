FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Set environment variable for NLTK data
ENV NLTK_DATA=/app/nltk_data

# ✅ Copy downloaded tokenizer into the Docker image
COPY nltk_data/ /app/nltk_data/

# ✅ Copy application source code
COPY . .

# ✅ Run multi-case runner script
CMD ["python", "run_pipeline.py"]
