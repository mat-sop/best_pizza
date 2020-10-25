FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /best_pizza
WORKDIR /best_pizza
COPY . /best_pizza/

RUN pip install -r requirements.txt
RUN python best_pizza/manage.py migrate

EXPOSE 8000
CMD ["python", "best_pizza/manage.py", "runserver", "0.0.0.0:8000"]
