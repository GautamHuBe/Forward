FROM python:3.12.3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

COPY . .

CMD ["bash", "start.sh"]
 
 
 
