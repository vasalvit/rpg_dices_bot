FROM python:3
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENV FLASK_APP /code/main.py
ENV FLASK_HOST 0.0.0.0
ENV FLASK_PORT 80
CMD flask run --host=$FLASK_HOST --port=$FLASK_PORT