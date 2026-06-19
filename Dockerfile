# Use the official lightweight Python image
FROM python:3.11-slim

# Set up a new non-root user for security containment
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Copy and install dependencies
COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the remaining project assets and code files
COPY --chown=user . /app

# Streamlit-specific configurations to listen on Hugging Face's mandatory port 7860
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
