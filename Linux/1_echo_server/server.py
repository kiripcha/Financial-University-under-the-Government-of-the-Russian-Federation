import socket
sock = socket.socket()
print("Начало работы сервера")
sock.bind(('', 9090))
print("Прослушивание порта 9090")
sock.listen(1)
conn, addr = sock.accept()
print("Связь установлена")
while True:
    data=conn.recv(1024)
    if not data:
        print("Данных больше нет")
        break
    print("Получение данных: ", data.decode('utf-8'))
    conn.send(data)
    print('Отправка данных обратно: ', data.decode('utf-8'))
print('Соединение отключено')
conn.close()