# Python base image use karein
FROM python:3.9-slim

# Container ke andar 'app' folder banayein
WORKDIR /app

# Sabse pehle requirements copy aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki saara code (app.py, templates) copy karein
COPY . .

# Port expose karein
EXPOSE 8080

# App chalu karne ki command
CMD ["python", "app.py"]