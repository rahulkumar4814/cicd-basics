FROM python:3.14-slim
WORKDIR /app
COPY app.py .
USER 1000
ENTRYPOINT ["python", "app.py"]