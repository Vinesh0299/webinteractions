[![Coverage Status](https://coveralls.io/repos/github/Vinesh0299/webinteractions/badge.svg?branch=main)](https://coveralls.io/github/Vinesh0299/webinteractions?branch=main)

This package aims towards providing API interfaces for various python libraries which results in reduction of
writing boilerplate code for each project using these libraries, instead users can use this package to complete
initial setup with as less as a single function call.

For example, if a user wants to create a TCP server then instead of going through and setting up all the details,
the user can simple run a function that creates a TCP server running on socketserver library, the user only needs to
provide the hostname and port number for the server to start, like shown below

```python
    from webinteractions.server_client.tcp_socket_server import create_tcp_synchronous()
    create_tcp_synchronous(hostname="localhost", port=8000)
    Listening on localhost:8000
```

