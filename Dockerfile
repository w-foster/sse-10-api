# Use official Python image as base
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy only the necessary files (excluding files listed in .dockerignore)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy remaining project files
COPY app /app

# Expose FastAPI's default port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "book_server:app", "--host", "0.0.0.0", "--port", "8000"]




