# Socket Programming

## How to run
1. Log into Ubuntu host in command line: "ssh -Y username@ubuntu2004-002.student.cs.uwaterloo.ca". This host will run the server program. Take note of the server address: "ubuntu2004-002". An IP address will work in this case as well
2. Navigate into the directory with the program files on ubuntu2004-002. Run server.py in python3: "python3 server.py"
3. Enter the required parameters each separated by a space (port number and request code). In this case: "1024 13"
This means the server will listen on port 1024 and the required request codes for clients to connect will be 13
4. Log into another Ubuntu host in command line on a new Shell tab: ""ssh -Y username@ubuntu2004-004.student.cs.uwaterloo.ca" . This host will run the client program.
5. Navigate into the directory with the program files on ubuntu2004-004. Run client.py in python3: "python3 client.py"
6. Enter the required parameters each separated by a space (server address, port number, request code and the message). In this case: "ubuntu2004-002 1024 13 A man, a plan, a canal—Panama!"  
This means the client will attempt to connect to the server named ubuntu2004-002 on port 1024 and provide the server with the request code 13 and the message "A man, a plan, a canal—Panama!"
7. The server will send you a reversal of the message. In this example: "!amanaP—lanac a ,nalp a ,nam A".  
The client will terminate.
8. The server will continue to listen for clients attempting to connect. Run the client program once more by going back to step 6 with a different message.
9. To terminate anyone of the programs, hit Ctrl + C

## Miscellaneous info
1. Both programs were written in Python 3. They will not run properly if you initiate it in the command line with "python 'program.py'" instead of "python3 'program.py'"
2. Make sure your inputs are formatted properly although the program will send error messages for any improper formatting.
3. You can run this program on the same machine by following the exact steps outlined above. However, make sure to initiate it in different Shell tabs. 
    1. Navigate to the directory that the program files are stored, then run each program by "python3 'program_name.py'"
    2. When asked for the server address in the client program, enter 'localhost' or '127.0.0.1' as that is the server address when running it on the same machine