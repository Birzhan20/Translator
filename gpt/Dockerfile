FROM python:3.11

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

ADD . .

EXPOSE 8010

CMD ["uvicorn", "NLP:app", "--host", "0.0.0.0", "--port", "8010", "--proxy-headers"]