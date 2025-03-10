FROM python:3.8-slim-buster

RUN apt update -y && apt install -y \
    awscli \
    gcc \
    g++ \
    python3-dev \
    libzstd-devWORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt
RUN pip install upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install --upgrade accelerate

CMD ["python3","app.py"]