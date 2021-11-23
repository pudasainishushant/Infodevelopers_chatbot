FROM python:3.7
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN apt install -y supervisor
RUN pip install --upgrade pip==20.2
# RUN pip install rasa==2.8.13
#RUN pip install SQLAlchemy==1.3.22
ENV RASA_X_PASSWORD="ChatbotDataTrainer"
ADD . /app
WORKDIR /app
#RUN pip install --ignore-installed -r requirements.txt --no-cache-dir
# RUN rasa train
#RUN pip install langdetect

#RUN pip install -U pip
#RUN pip install --use-feature=2020-resolver rasa-x==0.39.3 --extra-index-url https://pypi.rasa.com/simple
RUN pip3 install --use-feature=2020-resolver rasa-x --extra-index-url https://pypi.rasa.com/simple
#RUN rasa train
# CMD rasa x --no-prompt

COPY ./init/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD /usr/bin/supervisord

