# Use the official lightweight Python image
FROM python:3.11-slim

# Expose the mandatory port required by Hugging Face Spaces natively
EXPOSE 7860

# Establish server path parameters
ENV STREAMLIT_SERVER_PORT=7860
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Set up the base directory routing map
WORKDIR /app

# Set up a safe non-root user environment profile
RUN useradd -m -u 1000 user && chown -R user:user /app
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Copy package installation registers first to leverage cache matrices
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all remaining project code and folder elements explicitly to the app path root
COPY --chown=user . .

# Launch the Streamlit server engine out of the box
CMD ["streamlit", "run", "app.py"]
