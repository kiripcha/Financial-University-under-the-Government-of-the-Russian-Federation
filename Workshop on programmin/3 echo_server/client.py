import socket, getpass

def connect(ip, port):
    sock = socket.socket()
    sock.settimeout(1)
    print("Connecting to the server...")

    try:
        sock.connect((ip, port))
    except ConnectionRefusedError as err:
        print(err)
        return False
    except TypeError:
        return False
    print("Connection accept")

    while True:
        try:
            data = sock.recv(1024)
        except socket.timeout:
            break
    print("Message received")
    print(data.decode())

    while True:
        msg = input("Typing a message to server >>> ")
        print("\nSending data...")
        sock.send(msg.encode())
        if msg == "exit":
            break
        try:
            data = sock.recv(1024)
        except socket.timeout:
            continue
        print("Message received")
        print(data.decode())

    sock.close()
    return True

ip = getpass.getpass(prompt = "Write the ip address >>> ")
if ip == "":
    ip = "127.0.0.1"
port = getpass.getpass(prompt = "Write the port >>> ")
if port == "":
    port = 12345
else:
    try:
        port = int(port)
    except:
        print("Incorrect port")

logical = False
connCount = 0
while not logical and connCount<5:
    logical = connect(ip, port)
    if not logical:
        connCount += 1
    else:
        connCount=0
if connCount==5:
    print('Server close. Was 5 attempt to connect')