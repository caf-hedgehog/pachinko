FROM python:3.11.3-slim AS dev

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt update && apt upgrade -y \
&& pip install --upgrade pip && pip install pipenv --no-cache-dir

WORKDIR /workspace/api

EXPOSE 8000

WORKDIR /api
COPY ./ /api/

RUN pipenv install --system --deploy --ignore-pipfile

# ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
