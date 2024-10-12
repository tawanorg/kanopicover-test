FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
 
EXPOSE 80

ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=80
ENV PYTHONPATH=/app

# Run tests and then start the Flask application
CMD /bin/sh -c "pytest -v && flask run --host=0.0.0.0"