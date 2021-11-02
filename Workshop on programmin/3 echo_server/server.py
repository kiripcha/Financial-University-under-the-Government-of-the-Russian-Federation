import random, socket, sys

sock = socket.socket()

portt = 12345
while True:
    try:
        sock.bind(('127.0.0.1', portt))
        print("Connect to {}".format(portt))
        break
    except OSError as oserr:
        print("Port {} not avaliable".format(portt))
        portt = random.randint(1024, 65535)

sock.listen(0)
print("Working...")

def listening(sock):
    conn, addr = sock.accept()
    print("Client {} connect".format(addr))
    with open("clients.txt", 'a+') as clients:
        clients.seek(0, 0)
        for line in clients:
            if addr[0] in line:
                conn.send(('Hello ' + line.replace(addr[0], '')).encode())
                break
        else:
            conn.send('Enter your name!'.encode())
            username = conn.recv(1024).decode()
            clients.write('\n' + username + addr[0])

    ret = False
    msg = ""

    while True:
        print("Data from client:")
        try:
            data = conn.recv(1024)
        except (ConnectionResetError, ConnectionAbortedError) as err:
            print(err, addr)
            return
        msg = data.decode()
        print(msg)
        if msg == "exit":
            ret = True
            break
        if not data:
            break
        conn.send(data)
        print("Sending data to client...")
    conn.close()
    print("Client {} passed out".format(addr))
    return ret


ret = False
while not ret:
    ret = listening(sock)
print("Stop server")