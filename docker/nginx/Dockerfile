From nginx:latest
MAINTAINER "VMware<zweixiang@vmware.com>"


COPY ./dist /usr/share/nginx/html
COPY ./conf/nginx.conf /etc/nginx

EXPOSE 8088
EXPOSE 5000

RUN nginx 