FROM python:3.10-slim

RUN apt-get update && apt-get -y install gcc vim postgresql-client libpq-dev

WORKDIR /app

COPY ./system_appointments/requirements/main.txt .
RUN pip install --no-cache-dir -r main.txt

CMD ["bash", "docker/build.sh"]