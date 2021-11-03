import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
print("Связь установлена")
while True:
    line = input()
    sock.send(line.encode("utf-8"))
    if line == "exit" or line =="":
        sock.close()
        break
    print(f'Отправка данных серверу {line}')
    data = sock.recv(1024)
    print(f"Получение данных от сервера: {data.decode('utf-8')}")
print("Соединение разорвано")