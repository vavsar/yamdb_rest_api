FROM python:3.8.5

WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD gunicorn yamdb_final.wsgi:application --bind 0.0.0.0:8000
