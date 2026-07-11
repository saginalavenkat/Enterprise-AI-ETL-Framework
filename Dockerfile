# ============================================================================
# Enterprise AI ETL Framework
# Docker Image
# ============================================================================

# Step 1: Use official Python image
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy dependency file
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy project files
COPY . .

# Step 6: Default command
CMD ["pytest", "tests/test_end_to_end_workflow.py", "-s", "-v"]