#!/bin/sh

envsubst '$BACKEND_API' < /etc/nginx/nginx-template.conf > /etc/nginx/nginx.conf

echo "----------------------------------------------"
cat /etc/nginx/nginx.conf
echo "----------------------------------------------"

echo "Running Nginx..."
nginx

echo "Running Websocket server..."
python3 -u server.py
