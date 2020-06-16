FROM python:3


MAINTAINER "VMware<zweixiang@vmware.com>"
ENV PIPURL "https://pypi.tuna.tsinghua.edu.cn/simple"


WORKDIR /demo

COPY . /demo
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Windows 不支持guniicorn
#RUN pip --no-cache-dir install  -i  gevent==1.4.0
#RUN pip --no-cache-dir install  -i  gunicorn==20.0.4
# CMD gunicorn  -c gun.conf app:app