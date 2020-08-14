FROM mysql:5.7


ENV MYSQL_USER root
ENV MYSQL_PASSWORD root
COPY ./sql /tmp/sql
RUN mv /tmp/sql/*.sql /docker-entrypoint-initdb.d
RUN rm -rf /tmp/sql
#COPY ./sql/DoctorJoe.sql /mydata.sql