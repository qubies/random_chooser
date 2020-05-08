from python:latest
RUN apt-get update && apt-get install git
RUN mkdir /code
WORKDIR /code
RUN pip3 install PyInquirer tabulate cowsay
COPY ./chooser.py /code
COPY ./choices.json /code
CMD python3 chooser.py

