# Use a base python image
FROM python:3.12-slim
# Set the working directory inside the container
WORKDIR /app
# Copy the requirements.txt file into the container
COPY requirements.txt .
# Install the dependencies
RUN pip install -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
# Command to run the application
CMD ["python", "-m", "flask", "--app", "prime", "run", "--host=0.0.0.0", "--port=80", "--debug"]

