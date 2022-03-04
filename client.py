from socket import *

while True: # Handles errors if proper format not used, will continue requesting for proper input
    # Request for input from user for server address, port number, request code & message to reverse
    data = input("Please enter server address, port number, request code and message all seperated by a space: ")
    data = data.split() # Split input by spaces into an array
    if len(data) < 4: # Wrong number of input values
        print("Input values not formatted properly. Try again!")
    elif not data[1].isnumeric() or not data[2].isnumeric(): # Input values not numbers
        print("Port number and request code aren't numbers. Try again!")
    else:
        server_address = str(data[0])
        n_port = int(data[1])
        req_code = int(data[2])
        message = " ".join(data[3:]) # Message may be separated by space so join into string
        client_socket = socket(AF_INET, SOCK_STREAM)
        try:
            client_socket.connect((server_address, n_port))
            print("This is the message:", message) # Print message to be sent
            print("Requesting a connection to", server_address, "on port", n_port)
            client_socket.send(str(req_code).encode())
            break
        except:
            print("There was a problem with your input. Try again!")

message_from_server = client_socket.recv(1024).decode() # Receives message from server
if message_from_server == "Connection terminated!": # If request code wrong, terminate
    print("Your request code was wrong. Connection terminated!")
    client_socket.close()
else: # If request code sent was right, receive random port and send message
    r_port = int(message_from_server)
    print("Your request code was right!")
    client_socket.close()
    client_socket_udp = socket(AF_INET, SOCK_DGRAM)
    client_socket_udp.sendto(message.encode(), (server_address, r_port)) # Send message as UDP datagram to port
    print("Sending message as UDP datagram on port", str(r_port) + "...")
    modified_message, server_address = client_socket_udp.recvfrom(2048) # Receive modified message
    print("This is the reversed message:", modified_message.decode()) # Print modified message
    print("The session has ended!")
    client_socket_udp.close()