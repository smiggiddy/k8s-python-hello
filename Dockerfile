FROM alpine:3.16

WORKDIR /app 

EXPOSE 5000 

COPY hello_app main.py ./

RUN apk add python3 py3-pip

RUN pip install flask 

COPY . ./ 

CMD ["python3", "main.py"]