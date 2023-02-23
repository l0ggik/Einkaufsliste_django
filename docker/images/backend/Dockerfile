FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /django

WORKDIR /django
COPY requirements.txt /django/
RUN pip install -r requirements.txt
COPY . /django/

EXPOSE 8738

CMD python manage.py collectstatic --no-input ; python manage.py runserver 0.0.0.0:8738
