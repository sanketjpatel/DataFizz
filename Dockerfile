FROM python:2.7-slim
MAINTAINER sanketjpatel "sanketpatel.301090@gmail.com"
COPY src /
RUN pip install -r requirements.txt
WORKDIR /app
ENV DATA_DIR "../data"
ENV OUT_DIR ".."
CMD ["python", "app.py"]
