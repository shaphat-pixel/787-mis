#setting base image
FROM python:3.8-alpine

#for logging
ENV PYTHONUNBUFFERED 1

#for not creating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

#specifying our working directory
WORKDIR /app/mis

#copying requirements.txt file to the working directory
COPY requirements.txt /app/mis/

# Build psycopg2-binary from source -- add required dependencies
RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
        pip install --no-cache-dir -r requirements.txt && \
        apk --purge del .build-deps

#copying the content of the backend application into our Docker container.
COPY . /app/mis/

#the starting command for our container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]