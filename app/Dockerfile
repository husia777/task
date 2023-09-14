FROM python:3.11

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .
CMD [ "uvicorn app.route:app --host localhost  --port 8080" ]
