FROM python:3-slim

ADD usercredentials.py /

RUN pip install tornado
RUN pip install requests


CMD [ "python", "./usercredentials.py" ]
