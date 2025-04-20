FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

# Install uv
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.4.15 /uv /bin/uv

# Place executables in the environment at the front of the path
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#using-the-environment
ENV PATH="/app/.venv/bin:$PATH"

# Compile bytecode
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
ENV UV_COMPILE_BYTECODE=1

# uv Cache
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#caching
ENV UV_LINK_MODE=copy

COPY ./pyproject.toml ./uv.lock /app/

# Install dependencies
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
RUN uv sync --frozen --no-install-project

ENV PYTHONPATH=/app

# COPY ./scripts /app/scripts
# Copy alembic migrations and files
# COPY alembic.ini /app/
# COPY ./alembic /app/alembic

COPY ./pyproject.toml ./uv.lock /app/

# move server into the app folder
# COPY ./app /app/app
COPY ./hirawilliott /app/hirawilliott

# Sync the project
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
RUN target=/root/.cache/uv \
    uv sync


EXPOSE 8080

CMD ["fastapi", "run", "--workers", "4", "--port", "8080" "hirawilliott/main.py"]
