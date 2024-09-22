FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE $PORT

CMD gunicorn lbm.wsgi:application --bind 0.0.0.0:$PORT