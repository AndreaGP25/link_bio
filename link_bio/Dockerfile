FROM python:3.12

#ENV REDIS_URL=redis://redis PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.12 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["reflex", "run", "--env", "prod", "--backend-only" ]

#CMD reflex run --env prod --backend-only