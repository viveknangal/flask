FROM python:latest
RUN pip install flask gunicorn
EXPOSE 8080 # this only serves as documentation ,port are exposed using -P
WORKDIR /opt/
COPY . /opt/
ENTRYPOINT ["gunicorn"]
CMD ["-b","0.0.0.0:9090","first:app"]
