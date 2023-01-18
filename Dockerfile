FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5001:5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
CMD python app1.py
