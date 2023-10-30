FROM python:3.12.0-alpine3.17
COPY . /app
RUN pip install flask redis
CMD ["python", "app/main.py"]

