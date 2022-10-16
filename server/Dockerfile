FROM python:3.10.8-alpine

WORKDIR /usr/src/app/server

COPY . .
RUN pip install --no-cache-dir -r ./requirements.txt

ENV PYTHONUNBUFFERED=1

CMD [ "python", "./main.py" ]
