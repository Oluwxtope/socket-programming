from socket import *
import random

while True: # Handles errors if proper format not used, will continue requesting for proper input
    # Requests for input from user for server port number and request code
    data = input("Please enter the port number and request code seperated by a space: ")
    data = data.split()
    if len(data) < 2 or len(data) > 2: # Wrong number of input values
        print("Input values not formatted properly. Try again!")
    elif not data[0].isnumeric() or not data[1].isnumeric(): # Input values not numbers
        print("Input values aren't numbers. Try again!")
    else:
        n_port = int(data[0])
        req_code = int(data[1])
        server_socket = socket(AF_INET, SOCK_STREAM)
        try: # Bind n_port to server_socket, if any errors request diff port # from client
            server_socket.bind(('', n_port))
            server_socket.listen(1) # Accepts 1 connection at a time
            print("The server is awaiting a TCP connection on port", n_port, "...")
            break # Break out of loop and accept incoming connections
        except:
            print("You can't access that port. Try again!")
    print("\n")

# Loop to accept incoming TCP connections from clients
while True:
    connection, address = server_socket.accept()
    print("The server has accepted a connection from", address[0], "on welcoming port", address[1])
    client_req_code = int(connection.recv(1024).decode())
    if req_code != client_req_code: # Checks if the client and server request code is equal
        # If request code not equal, will send client error message and terminate welcoming port
        connection.send("Connection terminated!".encode())
        print("The clients request code was wrong. Connection to", address[0], "is severed!")
        connection.close()
    else:
        # If request code from client and server match, create UDP socket and receive message
        print("The clients request code was right! Creating a UDP socket...")

        while True: # Will loop until a free random port number is found
            r_port = random.randint(1024, 65536) # Choose random port number to send UDP datagram
            server_socket_udp = socket(AF_INET, SOCK_DGRAM)
            try: # Bind port number to UDP socket, handle error looping to find diff random number
                server_socket_udp.bind(('', r_port))
                break
            except:
                continue
        # Sends random port number chosen and bound to UDP socket to client on welcoming port
        connection.send(str(r_port).encode())
        connection.close() # End welcoming port
        
        print("The server is awaiting a UDP datagram on port", r_port, "from", address[0])
        message, client_address = server_socket_udp.recvfrom(2048) # Receives message from client
        print("The client sent this sentence:", message.decode())
        modified_message = message.decode()[::-1] # Reverses the message received
        print("This is the reverse of that sentence:", modified_message)
        server_socket_udp.sendto(modified_message.encode(), client_address) # Sends reversed message to client
        print("The server has sent the reversed sentence to client", str(address[0]) + ".", "The session has ended!")
    print("\nThe server is awaiting a TCP connection on port", n_port, "again...")