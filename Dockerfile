FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user --no-cache-dir -r requirements.txt
COPY templates templates
COPY app.py .

EXPOSE 8080

ENV MYSQL_HOST=localhost

CMD [ "python","app.py" ]