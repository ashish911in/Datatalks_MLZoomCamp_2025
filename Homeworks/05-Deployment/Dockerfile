FROM agrigorev/zoomcamp-model:2025

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install uv (fast dependency manager)
RUN pip install uv

# Copy pyproject.toml and optional poetry.lock
COPY pyproject.toml ./

# Install dependencies from pyproject.toml
RUN uv pip install --system --no-deps .

# ✅ Explicitly install uvicorn
RUN uv pip install uvicorn

# Copy the rest of your app
COPY . .

# Expose the port FastAPI will run on
EXPOSE 9696

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "Predict_FastAPI:app", "--host", "0.0.0.0", "--port", "9696"]