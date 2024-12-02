FROM python:3.10-slim

WORKDIR /APP

COPY APP/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY APP/ .

COPY Models /APP/Models

COPY data /APP/data

EXPOSE 8000

CMD ["uvicorn", "mlapi:app", "--host", "0.0.0.0", "--port", "8000"]
