FROM nginx:1.15-alpine
COPY nginx-cloud.conf /etc/nginx/conf.d/default.conf
