FROM python:3.12

LABEL authors="SzymKam"

WORKDIR src

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /src/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
