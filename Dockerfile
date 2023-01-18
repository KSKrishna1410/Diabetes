FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 8080:8081
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python flask_api.py
