# AFWSCE
Asynchronous fastapi websocket server and client WITHOUT a browser, example

### How to host a server on your own machine
    step 1: modify the routes and functions to your liking
    step 2 do not put anything on the internet that is http, make sure to at least use a self signed certificate and authentication for this server
    step 2 authentication and self signed certificates are not present in this example
    step 3 change `localhost` to your your ip address `0.0.0.0` if you are hosting the server on the cloud
    step 4 if you are not using a cloud, you will need to port forward whatever port you are running this server on
    step 4 after you have port forwarded, you will need a way of identifying the computer that is hosting the server on your network
    step 5 `pip instal -r requirements.txt`
    step 6 `python the_server.py`

### Python version
  python 3.8 +
