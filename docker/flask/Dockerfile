FROM python:3.7
MAINTAINER "VMware<zweixiang@vmware.com>"
ENV PIPURL "https://pypi.tuna.tsinghua.edu.cn/simple"

COPY ./ app

WORKDIR /app
EXPOSE 5000

# RUN pip install -r requirements.txt
RUN pip install -i $PIPURL -r requirements.txt
RUN pip install -i $PIPURL pymysql==0.9.3

CMD python ./src/app.py