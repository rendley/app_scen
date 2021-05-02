# pull official base image
FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./entrypoint.sh .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

# copy project
COPY . .

ENTRYPOINT ["chmod", "+x",  "/usr/src/app/entrypoint.sh"]