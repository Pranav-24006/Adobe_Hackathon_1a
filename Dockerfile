# Use AMD64-compatible Python image and force platform compatibility
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all source files
COPY src/ src/
COPY requirements.txt .
COPY run.sh .

# Install system dependencies (for PyMuPDF or PDFMiner compatibility)
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure script is executable
RUN chmod +x run.sh

# Set the entrypoint to the run script
ENTRYPOINT ["./run.sh"]
