FROM python:buster

ENV SRV_DEBUG=True
ENV SRV_HOST=0.0.0.0
ENV SRV_PORT=9000
ENV FLASK_APP=app

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9000

CMD ["python3", "-m", "src"]