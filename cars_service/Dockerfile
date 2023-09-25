FROM python:3.11-slim-bullseye

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production  # Set DJANGO_ENV to 'production'

# Copy the poetry.lock and pyproject.toml files to the container
COPY pyproject.toml poetry.lock /app/

RUN apt-get update
RUN pip install -U poetry

COPY . /app/
RUN poetry install

# Expose the port the application runs on
EXPOSE 5005

CMD ["poetry", "run", "python3", "cars_service/main.py"]
