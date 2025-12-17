FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/app.py .

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]