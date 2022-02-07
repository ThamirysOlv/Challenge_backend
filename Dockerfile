FROM python:3
EXPOSE 5000
WORKDIR /app
COPY models models
COPY routes routes
COPY app.py /app
COPY Dockerfile /app
COPY docker-compose.yml /app
COPY requirements.txt /app
COPY serializer.py /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "/bin/sh", "-c", "sleep 15 && flask db init && flask db migrate && flask db upgrade && python app.py" ]