FROM python:3.8

ADD run.py .

RUN pip install -r req.txt

CMD ["python", "./run.py"]

