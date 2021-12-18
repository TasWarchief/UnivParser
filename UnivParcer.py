from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Radiobutton
import threading
from threading import Thread
from parclas import Parcer

class Parcer_app(Tk):
    def __init__(self):
        super().__init__()
        
        # Настройки окна
        self.program_name = "UnivParcer 0.1a-1"
        self.geometry("480x240")
        #self.resizable(width = False, height = False)
        self.title(self.program_name)
        
        # Меню
        self.menu = Menu(self)
        
        # Меню UnivParcer
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Exit", command = self.destroy)
        self.menu.add_cascade(label = "UnivParcer", menu = self.file_menu)
        
        # Меню Plugins
        self.plugins_menu = Menu(self.menu,tearoff = 0)
        self.plugins_menu.add_command(label = "Get Plugin")
        self.menu.add_cascade(label = "Plugins", menu = self.plugins_menu)
        
        # Меню Help
        self.help_menu = Menu(self.menu, tearoff = 0)
        self.help_menu.add_command(label = "Tutorial")
        self.help_menu.add_command(label = "About UnivParcer")
        self.help_menu.add_command(label = "About Me")
        self.menu.add_cascade(label = "Help",menu = self.help_menu)
        
        self.config(menu=self.menu)
        ###### Рамка для иструментов ######
        self.fun_frame_url = Frame(self,bd = 2, highlightbackground = "#4d4d4d", highlightthickness = 1)
        self.fun_frame_url.pack(side = TOP)

        # Рамка для текстового поля
        self.text_frame = Frame(self, bd = 2, highlightbackground = "#4d4d4d", highlightthickness = 1)
        self.text_frame.pack(side = TOP)

        # Рамка для радиокнопок
        self.radio_frame = Frame(self, bd = 2, highlightbackground = "#4d4d4d", highlightthickness = 1 )
        self.radio_frame.pack(side = TOP)
        
        ###### Рамка для сохранения в файл ######
        self.save_frame = Frame(self, bd = 2)
        self.save_frame.place(x = 332, y = 202)

        self.page_change_frame = Frame(self, bd = 2)
        self.page_change_frame.place(x = 12, y = 202)
    
        # Текст URL
        self.url_label = Label(self.fun_frame_url, text = "URL:")
        self.url_label.grid(column = 0, row = 0)

        # Текстовое поле URL
        self.url_text = Entry(self.fun_frame_url, width = 15)
        self.url_text.grid(column = 1, row = 0)

        # Текст Element
        self.element_label = Label(self.fun_frame_url, text = "Element:")
        self.element_label.grid(column = 3, row = 0)

        # Текстовое поле Element
        self.element_text = Entry(self.fun_frame_url, width = 15)
        self.element_text.grid(column = 4, row = 0)

        # Текст Class
        self.class_label = Label(self.fun_frame_url, text = "Class:")
        self.class_label.grid(column = 5, row = 0)

        # Текстовое поле Class
        self.class_text = Entry(self.fun_frame_url, width = 15)
        self.class_text.grid(column = 6, row = 0)

        # Кнопка Search
        self.parcer_button = Button(self.fun_frame_url, text = "Search",command = self.do_parser_thread)
        self.parcer_button.grid(column = 7, row = 0)

        # Текстовое поле для вывода
        self.text = scrolledtext.ScrolledText(self.text_frame,width = 50, height = 10)
        #text.configure(state = "disabled")
        self.text.grid(column = 0, row = 0)
        
        # Переменная радиокнопок
        self.rad_var = IntVar()
        self.rad_var.set(1)
        
        # Радиокнопка Links
        self.rad1 = Radiobutton(self.radio_frame, text = "Links", variable = self.rad_var,  value = 1)
        self.rad1.grid(column = 0, row = 0)
        
        # Радиокнопка Clear
        self.rad2 = Radiobutton(self.radio_frame, text = "Clear", variable = self.rad_var,value = 2)
        self.rad2.grid(column = 1, row = 0)
        
        # Радиокнопка Not Clear
        self.rad3 = Radiobutton(self.radio_frame, text = "Not Clear", variable = self.rad_var,  value = 3)
        self.rad3.grid(column = 2, row = 0)
        
        # Кнопка Save
        self.save_button = Button(self.save_frame, text = "Save", command = self.save_to_file)
        self.save_button.grid(column = 1, row = 0)
        
        # Текст для Save
        self.save_text = Entry(self.save_frame, width = 15)
        self.save_text.grid(column = 0, row = 0)

        self.change_button = Button(self.page_change_frame, text = "Page", command = self.change_page_thread)
        self.change_button.grid(column = 0, row = 0)

        self.text_changer = Entry(self.page_change_frame, width = 15)
        self.text_changer.grid(column = 1, row = 0)
    
    # Парсер одной страницы
    def do_parser(self):
        
        self.text.delete("1.0","end")
        
        pars = Parcer()
        
        pars.url = self.url_text.get()
        pars.element = self.element_text.get()
        pars.cls = self.class_text.get()
        
        self.mode = self.rad_var.get()
        self.content = ""
        
        if self.mode == 1:
            self.content = pars.show_links()
            self.text.insert(3.0, self.content)
        elif self.mode == 2:
            self.content = pars.find_clear()
            self.text.insert(3.0, self.content)
        elif self.mode == 3:
            self.content = pars.find_text()
            self.text.insert(3.0, self.content)
    
    # Сохранение
    def save_to_file(self):
        
        if self.text_changer.get() == "":
            if self.save_text.get() != "":
                f = open(self.save_text.get(),'a',encoding = "utf-8" )
                f.write(str(self.content))
                f.close()
        
        elif self.change_content != "":
            if self.save_text.get() != "":
                f = open(self.save_text.get(),'a', encoding = "utf-8")
                f.write(str(self.change_content))
                f.close()

    # Парсер множества страниц
    def change_page(self):
        
        self.text.delete("1.0","end")
        
        self.change = self.text_changer.get()
        if "-" not in self.change:
            self.change = self.change.split(',')
        elif "-" in self.change:
            self.change = self.change.split('-')
            self.change = list(range(int(self.change[0]),int(self.change[1]) + 1))
        pars = Parcer()
        pars.element = self.element_text.get()
        pars.cls = self.class_text.get()
        
        self.mode = self.rad_var.get()
        self.change_content = ""
        
        cyc = 0
        
        for cha in self.change:
            
            pars.url = self.url_text.get() + str(cha)
            
            if self.mode == 1:
                cyc += 1
                
                loading = self.program_name + " | Loading " + str(cyc) + "/" + str(len(self.change))
                self.title(loading)

                self.content = pars.show_links()
                self.text.insert(3.0, self.content)
            
            elif self.mode == 2:
                cyc += 1
                
                loading = self.program_name + " | Loading " + str(cyc) + "/" + str(len(self.change))
                self.title(loading)

                self.content = pars.find_clear()
                self.text.insert(3.0, self.content)

            elif self.mode == 3:
                cyc += 1
                
                loading = self.program_name + " | Loading " + str(cyc) + "/" + str(len(self.change))
                self.title(loading)
                
                self.content = pars.find_text()
                self.text.insert(3.0, self.content)

            
            self.change_content += self.content
        
        self.text.delete("1.0","end")
        self.text.insert(3.0, self.change_content)
        
        self.title(self.program_name)
    
    # Поток парсера множетсва страниц
    def change_page_thread(self):
        thread = Thread(target = self.change_page)
        thread.start()
    
    # Поток парсера одной страницы
    def do_parser_thread(self):
        thread = Thread(target = self.do_parser)
        thread.start()


if __name__ == "__main__":
    
    app = Parcer_app()
    app.mainloop()

 
