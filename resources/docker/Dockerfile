FROM python:3.9-slim

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m -u 1000 sandbox_user

# Set up the working directory
WORKDIR /sandbox
RUN chown sandbox_user:sandbox_user /sandbox

# Switch to non-root user
USER sandbox_user

# Copy requirements file
COPY --chown=sandbox_user:sandbox_user requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Python path
ENV PYTHONPATH=/sandbox

# Command to run when container starts
CMD ["python"] 