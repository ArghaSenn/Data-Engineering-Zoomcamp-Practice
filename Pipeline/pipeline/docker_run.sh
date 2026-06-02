docker run -it --rm \
    --network=pg-network \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ny_taxi_postgres_data:/var/lib/postgresql \
    -p 5432:5432 \
    --name pgdatabase \
    postgres:18


# uv run python ingest_data.py \
#     --pg-user=root \
#     --pg-password=root \
#     --pg-host=localhost \
#     --pg-port=5432 \
#     --pg-database=ny_taxi \
#     --pg-target-table=yellow_taxi_data \
#     --year=2020 \
#     --month=2 \
#     --chunksize=100000

docker run -it --rm \
    --network=pg-network \
    taxi_ingest:v001 \
    --pg-user=root \
    --pg-password=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-database=ny_taxi \
    --pg-target-table=yellow_taxi_data \
    --year=2020 \
    --month=2 \
    --chunksize=100000

docker run -it --rm \
    --network=pg-network \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -v pgadmin_data:/var/lib/pgadmin \
    -p 8085:80 \
    --name pgadmin \
    dpage/pgadmin4