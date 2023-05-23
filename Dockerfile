FROM python:3.10-alpine3.17
WORKDIR /task_1
COPY ./requirements.txt /task_1/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /task_1/requirements.txt
COPY . .
RUN chmod a+x *.sh
CMD ["sh", "app.sh"]