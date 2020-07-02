FROM python:3.7.8

RUN apt update && apt install -y nginx gettext-base && apt-get clean

COPY requirements.txt .
RUN pip install -r requirements.txt

# Configure nginx
COPY nginx /etc/nginx/
# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
COPY run.sh server.py ./

EXPOSE 8888

CMD ./run.sh