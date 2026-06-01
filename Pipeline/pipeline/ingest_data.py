import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

# year = 2020
# month = 2
# chunksize=100000
# pg_user = "root"
# pg_password = "root"
# pg_host = "localhost"
# pg_port = "5432"
# pg_database = "ny_taxi"
# pg_target_table = "yellow_taxi_data"

@click.command()
@click.option('--pg-user', default='root', help='Postgres User')
@click.option('--pg-password', default='root', help='Postgres Password')
@click.option('--pg-host', default='localhost', help='Postgres host')
@click.option('--pg-port', default='5432', type= int , help='Postgres Port')
@click.option('--pg-database', default='ny_taxi' , help='Postgres Database')
@click.option('--pg-target-table', default='yellow_taxi_data' , help='Postgres Table')
@click.option('--year', default=2020, type= int , help='Data year')
@click.option('--month', default=2, type= int , help='Data month')
@click.option('--chunksize', default=100000, type= int , help='Chunk Size')


def run(year, month, chunksize, pg_user, pg_password, pg_host, pg_port, pg_database, pg_target_table):
    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"

    engine = create_engine(f'postgresql+psycopg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}')

    df_iter= pd.read_csv(
        prefix + f"yellow_tripdata_{year}-{month:02d}.csv.gz",
        dtype=dtype,
        parse_dates=parse_dates,
        chunksize=chunksize
    )

    first = True
    for df_chunk in tqdm(df_iter):
        print("Processing chunk of size:", len(df_chunk))

        #Create the Table if it doesn't exists
        if first:
            df_chunk.head(n=0).to_sql(
                name=pg_target_table,
                con=engine,
                if_exists="replace")

            first = False

        #Insert data
        df_chunk.to_sql(
            name=pg_target_table,
            con=engine,
            if_exists="append")

        print("Inserted:", len(df_chunk))


if __name__ == "__main__":
    run()
