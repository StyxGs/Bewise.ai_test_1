FROM python:3.10-alpine3.17
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
RUN chmod a+x ./*.sh
CMD ["sh", "app.sh"]