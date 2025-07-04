# syntax=docker/dockerfile:1.5

# ---------------------------
# 1) Builder-Stage
# ---------------------------
FROM python:3.12-slim-bookworm AS builder

ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive \
    UV_LINK_MODE=copy \
    UV_OVERRIDE_PYTHON_VERSION=3.12.0

# System-Dependencies für Build
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential libpq-dev curl git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# uv-Installer - Official method from docs
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/
COPY --from=ghcr.io/astral-sh/uv:latest /uvx /usr/local/bin/

# Python-Abhängigkeiten installieren
WORKDIR /build
COPY pyproject.toml uv.lock* ./
RUN --mount=type=cache,target=/root/.cache/pip \
    uv pip install --prefix=/install --no-compile --reinstall --strict -r pyproject.toml

# ---------------------------
# 2) Dev-Stage
# ---------------------------
FROM builder AS dev

# Pfad anpassen
ENV PATH="/install/bin:${PATH}"

# Non-root user (matches devcontainer.json remoteUser)
ARG USERNAME=vscode
ARG UID=1000
RUN useradd -m -u ${UID} -s /bin/bash ${USERNAME}

# Ensure workspace directory is writable by the non-root user
RUN mkdir -p /workspace && chown -R ${USERNAME}:${USERNAME} /workspace

# Arbeitsverzeichnis, Quellcode & Dev-Tools
WORKDIR /workspace
COPY --chown=${UID}:${UID} . .
RUN pip install --user \
        pre-commit black isort flake8 mypy ipython \
    && rm -rf /root/.cache/pip

USER ${USERNAME}
EXPOSE 8000

# Keep container running for development
CMD ["sleep", "infinity"]

# ---------------------------
# 3) Runtime-Stage
# ---------------------------
FROM python:3.12-slim-bookworm AS final

ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive

# Nur Runtime-Pakete
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        ca-certificates libpq5 curl \
    && rm -rf /var/lib/apt/lists/*

# Nicht-root-User
ARG USERNAME=vscode UID=1000
RUN useradd -m -u ${UID} -s /bin/bash ${USERNAME}

# uv & Python-Pakete vom Builder
COPY --from=builder /usr/local/bin/uv /usr/local/bin/uv
COPY --from=builder /usr/local/bin/uvx /usr/local/bin/uvx
COPY --from=builder /install /usr/local

WORKDIR /workspace
COPY --chown=${USERNAME}:${USERNAME} . .
USER ${USERNAME}
EXPOSE 8000

# Healthcheck & Entry
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/health || exit 1
ENTRYPOINT ["uv", "run", "app:app", "--host", "0.0.0.0", "--port", "8000"]
