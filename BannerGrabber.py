#!/usr/bin/python3

import socket

def banner(ip, port):

    """
    Connects to a given IP address and port, then attempts to grab and print the banner.
    
    Args:
    ip (str): The IP address to connect to.
    port (int): The port number to connect to.
    """

    try:
        s = socket.socket() # Create a new TCP/IP socket
        s.connect((ip, int(port))) # Ensure port is an integer
        banner_data = s.recv(1024)
        print(banner_data.decode("UTF-8")) # Decode and print the banner data as a string
    except socket.error as e:
        print(f"Socket error :  {e}")  # Handle any socket-related errors and print the error message

    # Ensure the socket is closed, whether or not an error occurred
    finally:
        s.close()    


def main():
    ip = input("Please enter the IP")
    port = str(input("Please input the port"))
    banner(ip, port)

main() #  Entry point of the script, calling the main function



