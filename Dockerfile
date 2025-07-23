FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y curl \
  && curl -LsSf https://astral.sh/uv/install.sh | sh \
  && mv /root/.local/bin/uv /usr/local/bin/uv \
  && mv /root/.local/bin/uvx /usr/local/bin/uvx \
  && apt-get clean && rm -rf /var/lib/apt/lists/*


RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "main.py"]
