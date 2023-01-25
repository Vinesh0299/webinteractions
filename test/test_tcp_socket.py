"""Tests tcp_socket_server module"""

import socket
import unittest

class TCPSocketTestMethods(unittest.TestCase):
    """Contains test cases for tcp_socket_server module"""
    def setUp(self):
        """Server must be started separately, rest of the variables are defined here"""
        self.hostname = "localhost"
        self.port = 8000
        self.port_threaded = 8001

    def test_ping_synchronous(self):
        """Checking the response of ping on the synchronous server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.hostname, self.port))
            sock.sendall(bytes("ping", "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        self.assertEqual(received, "ping received")

    def test_get_synchronous(self):
        """Testing response of get on the synchronous server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.hostname, self.port))
            sock.sendall(bytes("get", "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        self.assertEqual(received, "html corresponding to a webpage")

    def test_post_synchronous(self):
        """Testing response of post on the synchronous server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.hostname, self.port))
            sock.sendall(bytes("post", "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        self.assertEqual(received, "database was updated successfully")

    def test_undefined_synchronous(self):
        """Testing response for an unhandled request on synchronous server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.hostname, self.port))
            sock.sendall(bytes("test", "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        self.assertEqual(received, "unhandled request")

    def test_ping_threaded(self):
        """Testing ping response on threaded server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.hostname, self.port_threaded))
            sock.sendall(bytes("ping", "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        self.assertEqual(received, "ping received")

    def test_get_threaded(self):
        """Testing get response on threaded server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.hostname, self.port_threaded))
            sock.sendall(bytes("get", "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        self.assertEqual(received, "html corresponding to a webpage")

    def test_post_threaded(self):
        """Testing post response on threaded server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.hostname, self.port_threaded))
            sock.sendall(bytes("post", "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        self.assertEqual(received, "database was updated successfully")

    def test_undefined_threaded(self):
        """Testing response for unhandled request on threaded server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.hostname, self.port_threaded))
            sock.sendall(bytes("test", "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        self.assertEqual(received, "unhandled request")
        


if __name__ == "__main__":
    unittest.main()
