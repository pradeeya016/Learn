FROM almalinux:latest
RUN dnf install -y python3 python3-pip && \
    dnf clean all 
RUN pip install flask

WORKDIR /opt/flask
COPY app.py .
COPY template/ template/
EXPOSE 5000
CMD ["python3", "app.py"]
