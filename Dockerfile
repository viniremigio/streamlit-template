FROM python:3.10-slim-bookworm

# Python and Poetry setup
ENV \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry's configuration:
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.2

RUN pip3 install poetry==${POETRY_VERSION}

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry install  --no-interaction --no-ansi

COPY . .

ENTRYPOINT ["./entrypoint.sh"]