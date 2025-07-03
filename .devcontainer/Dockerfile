# syntax=docker/dockerfile:1.5
FROM python:3.12-slim AS base

# -----------------------------------------------------------------------------
# 1) System basics
# -----------------------------------------------------------------------------
ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive

# Install build & runtime OS packages in one layer
RUN apt-get update -y \
 && apt-get install --no-install-recommends -y \
      curl git ca-certificates build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------------------------
# 2) Install uv (fast dependency manager)
# -----------------------------------------------------------------------------
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# -----------------------------------------------------------------------------
# 3) Create user (avoid running as root)
# -----------------------------------------------------------------------------
ARG USERNAME=vscode
ARG UID=1000
RUN useradd -m -u ${UID} -s /bin/bash ${USERNAME}
USER ${USERNAME}
WORKDIR /workspace

# -----------------------------------------------------------------------------
# 4) Caching layer for Python deps
# -----------------------------------------------------------------------------
# When a pyproject.toml or uv.lock changes, invalidate cache
COPY --chown=${USERNAME}:${USERNAME} pyproject.toml uv.lock* /tmp/pypkg/

RUN --mount=type=cache,target=/home/${USERNAME}/.cache/uv \
    cd /tmp/pypkg \
 && uv pip install --system --no-compile --reinstall --require-virtualenv=false --strict \
 && uv pip sync

# -----------------------------------------------------------------------------
# 5) Final copy – source code
# -----------------------------------------------------------------------------
COPY --chown=${USERNAME}:${USERNAME} . /workspace 