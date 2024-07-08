FROM python:3.9.6-alpine3.14
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg aria2 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY . .
RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
