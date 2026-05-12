FROM python:slim

COPY requirements.txt . .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","new.py"]