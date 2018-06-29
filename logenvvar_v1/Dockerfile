FROM python:3-slim

ADD logenvvar.py /

RUN pip install tornado
RUN pip install requests


CMD [ "python", "./logenvvar.py" ]
