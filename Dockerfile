FROM python:3.10-slim

WORKDIR /api

COPY ./system_appointments/requirements/main.txt .

RUN pip install --no-cache-dir -r main.txt

EXPOSE 8000

CMD [ "bash", "docker/build.sh" ]