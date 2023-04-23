#!/bin/bash
# start pg server and pgadmin containers
# docker-compose -d up 

# build ingestion app image
# docker build -t newest .

# run ingestion app
docker run -it \
    --network=haw057_default newest \
    --username root \
    --password root \
    --server pgdatabase \
    --port 5432 \
    --database ny_taxi \
    --src_url https://people.sc.fsu.edu/~jburkardt/data/csv/hooke.csv \
    --table_name hooke