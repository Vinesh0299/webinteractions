"""Provides helper functions for other modules"""

def get_response(request_data, client_address):
    """Function returns response data for requests in synchronous server"""
    print(request_data)
    print(f"Received data from {client_address}")

    response = bytes("unhandled request", "ascii")

    if request_data == "ping":
        print("Ping sent back")
        response = bytes("ping received", "ascii")
    elif request_data == "get":
        print("Received a get request")
        response = bytes("html corresponding to a webpage", "ascii")
    elif request_data == "post":
        print("Received a post request")
        response = bytes("database was updated successfully", "ascii")

    return response
