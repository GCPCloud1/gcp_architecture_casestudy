# Import Python runtime and set up working directory
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
# Install any necessary dependencies
RUN pip3 install -r requirements.txt
COPY patient_data.csv /app/
COPY templates/ /app/templates/
COPY patient.py /app/patient.py
# Open port 8080 for serving the webpage
EXPOSE 8080
# Run app.py when the container launches
CMD ["python3", "patient.py"]