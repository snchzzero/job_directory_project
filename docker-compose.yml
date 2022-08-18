version: '3.7'

services:
#  db:
#    image: postgres:10.1-alpine
#    volumes:
#      - postgres_data:/var/lib/postgresql/data/
  web:
    build: .
    command: python /usr/src/job_directory_project/manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/usr/src/job_directory_project
    ports:
      - 8000:8000
volumes:
  postgres_data: