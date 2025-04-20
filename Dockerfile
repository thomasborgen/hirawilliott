FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

EXPOSE 8080
# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "hirawilliott/main.py", "--port", "8080", "--host", "0.0.0.0"]

# FROM python:3.12

# ENV PYTHONUNBUFFERED=1

# WORKDIR /app/

# # Install uv
# # Ref: https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
# COPY --from=ghcr.io/astral-sh/uv:0.4.15 /uv /bin/uv

# # Place executables in the environment at the front of the path
# # Ref: https://docs.astral.sh/uv/guides/integration/docker/#using-the-environment
# ENV PATH="/app/.venv/bin:$PATH"

# # Compile bytecode
# # Ref: https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
# ENV UV_COMPILE_BYTECODE=1


# COPY ./pyproject.toml ./uv.lock /app/

# ENV PYTHONPATH=/app

# COPY ./hirawilliott /app/hirawilliott

# RUN uv sync

# CMD ["uv", "run", "fastapi", "run", "--workers", "1" "hirawilliott/main.py"]
