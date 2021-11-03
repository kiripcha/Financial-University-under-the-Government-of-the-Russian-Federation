import socket
from threading import Thread
from tkinter import *
from tkinter.font import Font
from time import sleep
from keyboard import *


class Client:
    BUTTON: str = "enter"

    def __init__(self):
        self.socket: socket.socket = self.open_socket()
        self.window: Tk = Tk()
        self.text_field: Text = Text(self.window)
        self.input_field: Entry = Entry(self.window)
        self.is_focused: BooleanVar = BooleanVar()
        self.configure_window()

        self.accept_thread: Thread = Thread(name="accept", target=self.accept)

        self.send_thread: Thread = Thread(name="send", target=self.send)

        self.accept_thread.start()
        self.send_thread.start()

        self.window.mainloop()

    @staticmethod
    def open_socket() -> socket.socket:
        sock: socket.socket = socket.socket()
        try:
            sock.connect(("127.0.0.1", 9091))
        except:
            sock.close()
            raise Exception("Can't connect to the server")
        return sock

    def configure_window(self):
        self.window.title("Client")
        self.window.configure(bg="#4B0082")
        self.window.geometry("400x600")
        self.window.resizable(0, 0)
        self.window.bind('<FocusIn>', lambda _: self.is_focused.set(True))
        self.window.bind('<FocusOut>', lambda _: self.is_focused.set(False))

        self.text_field.configure(font=Font(size=9, weight="bold"), bg="#8A2BE2", fg="#000000", width=380, height=35)
        self.text_field.pack(side=TOP, padx=10, pady=10)

        self.input_field.configure(font=Font(size=9, weight="bold"), bg="#8A2BE2", fg="#000000", width=380)
        self.input_field.pack(side=TOP, padx=10, pady=10)

        self.input_field.focus_set()

    def accept(self):
        while True:
            try:
                data: list = self.socket.recv(2048).decode().split(":")
                user: str = data[0]
                message: str = "".join(data[1:])
                if user == "Введите логин" or \
                        user == "Введите пароль" or \
                        user == "Вход выполнен" or \
                        user == "Задайте пароль":
                    self.text_field.insert(END, f"{user}\n")
                else:
                    self.text_field.insert(END, f"{user} прислал:{message}\n")
            except:
                sleep(0.5)
            finally:
                self.text_field.see(END)

    def send(self):
        while True:
            if is_pressed(self.BUTTON) and self.is_focused.get():
                data: str = self.input_field.get()
                self.input_field.delete(0, END)
                try:
                    self.socket.send(data.encode())
                except:
                    print("Send ERROR")
                finally:
                    sleep(1)


def main():
    Client()


if __name__ == '__main__':
    main()
