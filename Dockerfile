# Base image of the container
FROM python:3.12.1-slim

# Copying uv from the virtual env
COPY --from=ghcr.io/astral-sh/uv:latest /uv/ bin