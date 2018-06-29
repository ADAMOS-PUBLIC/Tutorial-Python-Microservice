FROM python:3-slim

ADD ms_credentials.py /

RUN pip install tornado
RUN pip install requests


CMD [ "python", "./ms_credentials.py" ]
