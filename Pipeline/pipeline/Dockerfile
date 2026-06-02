# Base image of the container
FROM python:3.12.1-slim

# Copying uv from the virtual env
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Create Working directiory
WORKDIR /app

#Add env varaibles to path
ENV PATH="/app/.venv/bin:$PATH"

#Copying dependency files first
COPY pyproject.toml .python-version uv.lock ./

#Install dependencies from lock
RUN uv sync --locked

#Copy ingest_data file
COPY ingest_data.py .

#Set entrypoint
ENTRYPOINT ["python", "ingest_data.py"]