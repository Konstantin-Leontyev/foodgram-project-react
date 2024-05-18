FROM python:3.9

RUN apt-get update && \
    apt-get -y install -f && \
    apt-get -y full-upgrade && \
    apt-get -y autoremove && \
    apt-get -y autoclean && \
    apt-get -y clean

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip && \
    pip install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod +x run_app.sh
ENTRYPOINT ["/app/run_app.sh"]