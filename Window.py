import tkinter.filedialog

from matplotlib import pyplot as plt

from ChildWindows import *
import Population
import numpy as np


class Window:
    def __init__(self, width, height, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+100+75")
        self.root.resizable(False, False)
        self.displayed_time = StringVar(value="0")
        self.displayed_count = StringVar(value="0.0")
        self.button = None

    def run(self):
        self.draw()
        self.root.mainloop()

    def draw(self):
        self.draw_menu()
        frame = Frame(self.root)
        frame.pack(side=LEFT, anchor=N, padx=10)
        Label(frame, text="Текущее время (с)").pack(pady=(10, 0))
        Entry(frame, width=25, textvariable=self.displayed_time, state=DISABLED).pack()
        Label(frame, text="Общая энергия (Дж)").pack(pady=(10, 0))
        Entry(frame, width=25, textvariable=self.displayed_count, state=DISABLED).pack()
        frame = Frame(self.root)
        frame.pack(side=LEFT, padx=12)
        self.button = Button(frame, width=20, height=10, text="Запуск модели", command=self.start_exec)
        self.button.pack()

    def draw_menu(self):
        main_menu = Menu(self.root)

        file_menu = Menu(main_menu, tearoff=0)
        file_menu.add_command(label="Новая система", command=self.create_system)
        main_menu.add_cascade(label="Файл", menu=file_menu)

        main_menu.add_command(label="Параметры", command=self.change_params)
        self.root.configure(menu=main_menu)

    def create_system(self):
        Window1(self.root, "Новая система")

    def change_params(self):
        a = Window2(self.root, "Параметры")
        a.draw()

    def start_exec(self):
        print('\nStarted execution...')
        Population_array = []
        for i in Config.param_values:
            Population_array.append(Population.Population(i[1], i[0], i[2]))
        T_array = np.arange(0, Config.time + Config.delta, Config.delta)
        for i in T_array:
            a = 0
            for population in Population_array:
                population.interaction(Population_array)
                a += population.N
            print("Alln= ", a)
        for population in Population_array:
            plt.plot(T_array, population.array_N, linestyle='--', label=f"id = {population.id}")
        plt.legend()
        plt.show()
