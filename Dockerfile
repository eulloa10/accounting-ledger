# Use the official Python runtime image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app/ledger

# Set environment variables
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements first for better caching
COPY requirements.txt /app/ledger
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/ledger

# Expose the Django port
EXPOSE 8000

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
