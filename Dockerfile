FROM mcr.microsoft.com/playwright/python:v1.59.0-noble

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better cache)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your whole project (including /tests)
COPY . .

# Default command to run tests with HTML report
CMD ["python", "main.py"]