FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf .
RUN cp nginx.conf /etc/nginx/conf.d/