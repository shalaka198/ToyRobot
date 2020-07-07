FROM python:3.8-slim-buster
WORKDIR /usr/src/app
RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

ARG pyenv_value=dev
ENV PY_ENV=$pyenv_value

EXPOSE 80
CMD ["python", "start.py"]