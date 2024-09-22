FROM python:3.9

WORKDIR /app

COPY requirements.txt .

ENV DJANGO_SUPERUSER_PASSWORD=admin
ENV DJANGO_SUPERUSER_USERNAME=admin@admin.com
ENV DJANGO_SUPERUSER_EMAIL=admin@admin.com

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
RUN python manage.py migrate --database=djongo
RUN python manage.py createsuperuser --noinput

EXPOSE $PORT

CMD gunicorn lbm.wsgi:application --bind 0.0.0.0:$PORT
