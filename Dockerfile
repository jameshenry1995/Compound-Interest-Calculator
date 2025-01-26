# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /Compound-Interest-Calculator

# Install necessary system dependencies (e.g., for altair, polars, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container
COPY requirements.txt /Compound-Interest-Calculator/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the application files to the container
COPY . /Compound-Interest-Calculator

# Expose the port Streamlit uses (default is 8501)
EXPOSE 8501

# Command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "main_interest_calculator_script.py", "--server.headless=true", "--server.port=8501"]
