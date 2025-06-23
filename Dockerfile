FROM python:3.11.7
RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /AutoFilterBot
WORKDIR /AutoFilterBot
COPY . /AutoFilterBot
CMD ["python", "bot.py"]
