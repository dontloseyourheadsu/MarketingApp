# docker/fastapi/Dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt   # SQLAlchemy, PyMySQL, Pydantic, Faker, passlib[bcrypt] …

COPY . .

# default CMD can be overridden by docker-compose
CMD ["uvicorn", "apps.fastapi_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
