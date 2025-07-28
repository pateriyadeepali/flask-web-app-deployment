FROM registry.access.redhat.com/ubi8/python-38

WORKDIR /app

COPY app.py .

COPY requirements.txt .

RUN pip3 install --user -r requirements.txt

RUN pip3 install --user flask

EXPOSE 5000

CMD ["python3", "app.py"]
