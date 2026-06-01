docker run -it --rm \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ny_taxi_postgres_data:/var/lib/postgresql \
    -p 5432:5432 \
    postgres:18


uv run python ingest_data.py \
    --pg-user=root \
    --pg-password=root \
    --pg-host=localhost \
    --pg-port=5432 \
    --pg-database=ny_taxi \
    --pg-target-table=yellow_taxi_data \
    --year=2020 \
    --month=2 \
    --chunksize=100000