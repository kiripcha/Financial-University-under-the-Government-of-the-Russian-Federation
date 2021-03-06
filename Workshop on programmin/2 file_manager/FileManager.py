import os
import shutil
from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import showerror


class FileManager:

    def __init__(self):
        self.window = Tk()
        self.top_frame = Frame(self.window)
        self.bottom_frame = Frame(self.window)
        self.file_list = Listbox(self.top_frame, width=50, height=20)
        self.file_content = Listbox(self.top_frame, width=50, height=20)
        self.text = StringVar()
        self.label = Label(self.bottom_frame, width=50, textvariable=self.text)
        self.console = Entry(self.bottom_frame, width=50)
        self.commands = {
            "createdir": self.create_dir, #Создаmь каталог
            "removedir": self.remove_dir, #Удалить каталог
            "changedir": self.change_dir, #Сменить текущий каталог
            "createfiles": self.create_files, #Создать файл
            "writefile": self.write_file, #Записать файл
            "readfile": self.read_file, #Открыть файл
            "removefiles": self.remove_files, #Удалить файлы
            "copyfiles": self.copy_files, #Скопировать файлы
            "movefiles": self.move_files, #Переместить файлы
            "renamefile": self.rename_file, #Переименовать файл
        }
        self.path = os.getcwd()
        self.configure_window()

    def configure_window(self): #Задаём вид нашему окну 
        self.window.title("File manager")
        self.window.bind('<Return>', self.get_command)
        self.top_frame.configure(bg="#4B0082")
        self.bottom_frame.configure(bg="#4B0082")
        self.top_frame.pack(fill=BOTH)
        self.bottom_frame.pack(fill=BOTH)
        self.file_list.pack(side=LEFT, padx=10, pady=10)
        self.file_list.configure(font=Font(size=9, weight="bold"), bg="#9400D3", fg="#FFFFFF",
                                 selectbackground="#FFFFFF", selectforeground="#000000")
        self.file_content.pack(side=RIGHT, padx=10, pady=10)
        self.file_content.configure(font=Font(size=9, weight="bold"), bg="#9400D3", fg="#FFFFFF",
                                    selectbackground="#FFFFFF", selectforeground="#000000")
        self.label.pack(side=TOP, padx=10)
        self.label.configure(font=Font(size=9, weight="bold"), bg="#9400D3", fg="#FFFFFF")
        self.console.pack(side=TOP, padx=10, pady=2)
        self.console.configure(font=Font(size=9, weight="bold"), bg="#9400D3", fg="#FFFFFF")
        self.display_dir_content()
        self.display_path()
        self.window.mainloop()

    def display_dir_content(self): #Обновление текстового поля с содержимым каталога
        self.file_list.delete(0, END)
        for file in os.listdir(os.getcwd()):
            self.file_list.insert(END, file)

    def display_path(self): #Обновление пути
        self.text.set(self.path)

    def display_content(self, content): #Открытие текстового файла и его выведение в текстовое поле
        self.file_content.delete(0, END)
        for line in content:
            self.file_content.insert(END, line)

    def get_command(self, event): #Вызов комманд с проверкой
        line = self.console.get().split(" ")
        self.console.delete(0, END)
        if len(line) > 0:
            command, arguments = line[0], line[1:]
            if command in self.commands.keys():
                self.commands[command](*arguments)
            else:
                showerror("Warning", "There is no such command")
            self.display_path()

    def create_dir(self, *args): 
        if len(args) > 1:
            showerror("Warning", "Too many arguments")
        else:
            dirName = args[0]
            try:
                os.mkdir(self.path + os.sep + dirName)
                self.display_dir_content()
            except Exception as e:
                showerror("Warning", str(e))

    def remove_dir(self, *args): 
        if len(args) > 1:
            showerror("Warning", "Too many arguments")
        else:
            dirName = args[0]
            try:
                shutil.rmtree(self.path + os.sep + dirName)
                self.display_dir_content()
            except Exception as e:
                showerror("Warning", str(e))

    def change_dir(self, *args): 
        if len(args) > 1:
            showerror("Warning", "Too many arguments")
        else:
            try:
                os.chdir(args[0])
                self.path = os.getcwd()
                self.display_dir_content()
            except Exception as e:
                showerror("Warning", str(e))

    def create_files(self, *args): 
        try:
            for file_name in args:
                if ".txt" not in file_name:
                    file_name += ".txt"
                open(file_name, 'a').close()
            self.display_dir_content()
        except Exception as e:
            showerror("Warning", str(e))

    def write_file(self, *args): 
        if len(args) < 2:
            showerror("Warning", "Too few arguments")
        else:
            try:
                file_name, data = args[0], args[1:]
                if ".txt" not in file_name:
                    file_name += ".txt"
                with open(file_name, 'a') as file:
                    file.write(" ".join(data) + "\n")
                self.display_dir_content()
            except Exception as e:
                showerror("Warning", str(e))

    def read_file(self, *args): 
        if len(args) > 1:
            showerror("Warning", "Too many arguments")
        else:
            try:
                file_name = args[0]
                if ".txt" not in file_name:
                    file_name += ".txt"
                with open(file_name, 'r') as file:
                    self.display_content(file)
            except Exception as e:
                showerror("Warning", str(e))

    def remove_files(self, *file_names):
        try:
            for file_name in file_names:
                if ".txt" not in file_name:
                    file_name += ".txt"
                os.remove(file_name)

            self.display_dir_content()
        except Exception as e:
            showerror("Warning", str(e))

    def copy_files(self, *args):
        file_names = args[:-1]
        dirPath = args[-1]
        try:
            for file_name in file_names:
                if ".txt" not in file_name:
                    file_name += ".txt"
                shutil.copy(file_name, dirPath)

            self.display_dir_content()
        except Exception as e:
            showerror("Warning", str(e))

    def move_files(self, *args):
        file_names = args[:-1]
        dirPath = args[-1]
        for file_name in file_names:
            if ".txt" not in file_name:
                file_name += ".txt"
            shutil.move(file_name, dirPath)

        self.display_dir_content()

    def rename_file(self, *args):
        if len(args) > 2:
            showerror("Warning", "Too many arguments")
        elif len(args) < 2:
            showerror("Warning", "Too few arguments")
        else:
            file_name = args[0]
            if ".txt" not in file_name:
                file_name += ".txt"
            new_file_name = args[1]
            if ".txt" not in new_file_name:
                new_file_name += ".txt"
            os.rename(file_name, new_file_name)
        self.display_dir_content()


def main():
    FileManager()


if __name__ == '__main__':
    main()
