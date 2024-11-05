FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libpq-dev gunicorn &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
        --mount=type=bind,source=uv.lock,target=uv.lock \
        --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
        uv sync --frozen --no-install-project --no-dev

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
        uv sync --frozen --no-dev


#COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT []

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
WORKDIR /app/dadoconcreto_api
EXPOSE 9090
CMD ["gunicorn", "dadoconcreto_api.wsgi:application", "--bind", "0.0.0.0:9090"]
