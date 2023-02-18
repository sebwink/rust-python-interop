FROM rust:1.67-slim

RUN apt update && \
    apt install -y python3 python-is-python3 python3-pip python3-venv python3-dev && \
    apt install -y git

RUN python3 -m pip install --user pipx && \
    python3 -m pipx ensurepath

ENV PATH=$PATH:/root/.local/bin

RUN pipx install poetry && \
    pipx install maturin