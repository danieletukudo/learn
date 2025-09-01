FROM python:3.9.11-slim


WORKDIR /app


COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 8080
ENV FLASK_ENV=production
CMD ["flask", "run"，"--host"，"0.0.0.0"，"--port=8080"］