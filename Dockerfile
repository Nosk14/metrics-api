FROM python:3.8-slim
ENV FLASK_APP /usr/local/metrics-api/api.py
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY api /usr/local/metrics-api/
WORKDIR /usr/local/metrics-api/
CMD gunicorn -w 2 -b 0.0.0.0:5000 --log-level DEBUG api:api