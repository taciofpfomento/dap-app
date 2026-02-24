## DEPS
FROM python:3.13.5-slim as deps
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

## BUILD
FROM deps as build

COPY pyproject.toml uv.lock ./

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \    
    UV_PYTHON_DOWNLOADS=never

RUN uv sync --frozen --no-dev --no-editable && \
    ln -sf /usr/bin/python .venv/bin/python

## RUN
FROM gcr.io/distroless/python3-debian13:debug

EXPOSE 8080

WORKDIR app

COPY --from=build --chown=nonroot:nonroot .venv/ /app/.venv
COPY --chown=nonroot:nonroot src/ /app

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["python", "main.py"]