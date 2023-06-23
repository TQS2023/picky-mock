FROM python:3.10-alpine

WORKDIR /app

COPY api/requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code
ADD api /app

# Start the app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]