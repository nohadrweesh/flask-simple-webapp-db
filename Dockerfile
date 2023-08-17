FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY templates templates
COPY app.py .

EXPOSE 8080

ENV MYSQL_HOST=localhost

CMD [ "python","app.py" ]