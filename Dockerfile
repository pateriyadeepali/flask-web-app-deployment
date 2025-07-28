FROM registry.access.redhat.com/ubi8/python-38

WORKDIR /app

COPY app.py .

COPY requirement.txt .

RUN pip3 install -r requirement.txt

RUN pip3 install flask

EXPOSE 5000

CMD ["python3", "app.py"]
