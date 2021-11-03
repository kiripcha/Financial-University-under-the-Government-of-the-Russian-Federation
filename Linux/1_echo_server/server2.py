from socket import *

Host = "localhost"
Port = 9090 #порт
addr = (Host, Port) #кортеж для хранения адреса сервера
sock = socket(AF_INET, SOCK_DGRAM) #новый объект
sock.bind(addr) #привязка к адресу
connections = []
print("Связь с клиентом установлена")
while True:
    conn, addr = sock.recvfrom(1024) #получаем данные
    line = conn.decode() #декодинг строки
    print(conn.decode())
    line2 = input("Ответ клиенту: ")
    line2 = line2.encode()#строка в байты
    sock.sendto(line2, addr)#данные отправляются в сокет
print("Соединение с клиентом прекращено")
conn.close()