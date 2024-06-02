FROM python:3.8-slim

# Creating a non-root user and group to run the application with controlled access permissions
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /usr/src/app

# Script used to execute the python code
COPY run_code.py .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Changing ownership of the directory to use newly created user
RUN chown -R appuser:appuser /usr/src/app

# Switch to the non-root user to restrict access permissions
USER appuser

ENTRYPOINT ["python3", "run_code.py"]
