FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Sync dependencies
RUN uv sync

# Set environment
ENV PYTHONPATH=/app/src

# Expose port
EXPOSE 8000

# Run the server
CMD ["uv", "run", "src/notte_mcp/server.py"]