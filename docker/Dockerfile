FROM python:3.6
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt

EXPOSE 3000
CMD ["python", "/app/main.py"]