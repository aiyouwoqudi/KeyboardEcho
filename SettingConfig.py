'''
Author: MaZongyang
Date: 2023-11-29 12:49:51
LastEditors: MaZongyang
LastEditTime: 2023-11-29 13:23:04
Description: 
'''
import tkinter as tk
from tkinter import ttk
from configparser import ConfigParser

class ConfigGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Config GUI")

        # 读取配置文件
        self.config = ConfigParser()
        self.config.read('config.ini')

        # 创建界面组件
        self.create_widgets()

    def create_widgets(self):
        # 创建标签和输入框
        ttk.Label(self, text="窗口透明度").grid(row=2, column=0, padx=10, pady=5)
        self.alpha_entry = ttk.Entry(self)
        self.alpha_entry.grid(row=2, column=1, padx=10, pady=5)
        self.alpha_entry.insert(0, self.config.get('WindowSettings', 'Alpha'))

        ttk.Label(self, text="字体颜色").grid(row=3, column=0, padx=10, pady=5)
        self.color_entry = ttk.Entry(self)
        self.color_entry.grid(row=3, column=1, padx=10, pady=5)
        self.color_entry.insert(0, self.config.get('FontSettings', 'Color'))

        ttk.Label(self, text="字体大小").grid(row=4, column=0, padx=10, pady=5)
        self.size_entry = ttk.Entry(self)
        self.size_entry.grid(row=4, column=1, padx=10, pady=5)
        self.size_entry.insert(0, self.config.get('FontSettings', 'Size'))

        ttk.Label(self, text="保留时间(ms)").grid(row=5, column=0, padx=10, pady=5)
        self.retention_entry = ttk.Entry(self)
        self.retention_entry.grid(row=5, column=1, padx=10, pady=5)
        self.retention_entry.insert(0, self.config.get('DisplaySettings', 'RetentionTime'))

        # 创建保存按钮
        ttk.Button(self, text="保存", command=self.save_config).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Label(self, text="保存配置后重启生效").grid(row=7, column=0, columnspan=2, pady=10)

        # Center the window on the screen
        self.center_window()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the x and y coordinates for the Tk root window
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2

        # Set the dimensions of the window and its position
        self.geometry("+{}+{}".format(x, y))

    def save_config(self):
        self.config.set('WindowSettings', 'Alpha', self.alpha_entry.get())
        self.config.set('FontSettings', 'Color', self.color_entry.get())
        self.config.set('FontSettings', 'Size', self.size_entry.get())
        self.config.set('DisplaySettings', 'RetentionTime', self.retention_entry.get())

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        self.destroy()

if __name__ == '__main__':
    config_gui = ConfigGUI()
    config_gui.mainloop()
