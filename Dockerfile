FROM fedora:latest

RUN dnf update -y
COPY main.py /APP/main.py

cmd ["python3", "/APP/main.py"]