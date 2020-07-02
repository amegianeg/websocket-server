# websocket-server


## Generate self-signed certificate

    openssl req -x509 -newkey rsa:4096 -days 365 -nodes -subj "/C=US/ST=Oregon/L=Portland/O=Company Name/OU=Org/CN=localhost" -keyout key.pem -out cert.pem
