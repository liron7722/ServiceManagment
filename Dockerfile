# temp stage
FROM python:3.11.0a5-alpine as builder

#RUN addgroup --system app && adduser --system --group app
#RUN addgroup --gid 1001 --system app && adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app
#USER app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
#RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt


# final stage
FROM python:3.11.0a5-alpine

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY main.py .
CMD [ "python3", "./main.py" ]