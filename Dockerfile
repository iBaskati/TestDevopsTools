FROM python:3.8

ADD run.py .
ADD req.txt .

RUN pip install -r ./req.txt

CMD ["python", "./run.py"]

