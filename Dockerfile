FROM python:3.8 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.8
WORKDIR /code/app
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 
COPY . /code/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
