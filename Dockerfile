# Dockerfile is for building images
FROM python:3.9
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2
WORKDIR /app
COPY upload_data.py upload_data.py
# https://www.tutorialspoint.com/run-vs-cmd-vs-entrypoint-in-docker
ENTRYPOINT [ "python","upload_data.py" ]


