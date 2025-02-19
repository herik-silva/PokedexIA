FROM python:3.10-alphine
WORKDIR /code
COPY requirements.txt requirements.txtRUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "main.py"]