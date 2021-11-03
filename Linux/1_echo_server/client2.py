from socket import * #импортируем библиотеку
Host = "localhost" #сервер
Port = 9090  #порт
addr = (Host, Port)  #кортеж для хранения адреса сервера
sock = socket(AF_INET, SOCK_DGRAM) #новый объект
user = "" #имя клиента
while user == "":
    print("Введите ваше имя: ")
    user = input()
while True:
    line = input("Введите Ваше сообщение: ")
    if line == "exit" or line == "":
        print('Соединение прекращено')
        sock.close() #закрываем сокет

    line = user + ': ' + line
    line = line.encode() #строка в байты
    sock.sendto(line, addr) #данные отправляются в сокет
    line = sock.recvfrom(1024)#получаем данные из сокета
    print(f'Данные от сервера: {line[0].decode()}, {line[1]}')