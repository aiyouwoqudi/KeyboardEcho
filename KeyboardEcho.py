from configparser import ConfigParser
from tkinter import PhotoImage
import tkinter as tk
import SettingConfig
import keyboard
import logging
import sys
import os

class AlwaysOnTopWindow(tk.Tk):
    def __init__(self, config):
        tk.Tk.__init__(self)

        # 从配置文件中读取窗口设置
        self.alpha = config.getfloat('WindowSettings', 'Alpha')

        # 获取屏幕宽度和高度
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # 设置窗口大小为桌面的1/5
        self.width = screen_width // 5
        self.height = screen_height // 5

        # 从配置文件中读取字体设置
        font_color = config.get('FontSettings', 'Color')
        font_size = config.getint('FontSettings', 'Size')

        # 从配置文件中读取显示设置
        self.retention_time = config.getint('DisplaySettings', 'RetentionTime')

        # 隐藏窗口边框
        self.overrideredirect(True)

        # 始终置于最前面
        self.attributes('-topmost', True)

        # 设置窗口大小
        self.geometry(f'{self.width}x{self.height}+100+100')

        # 设置窗口背景色为黑色，透明度
        self.configure(bg='#000000')  # 设置背景色为黑色
        self.attributes('-alpha', self.alpha)  # 设置透明度

        # 添加标签，文字居中
        self.label = tk.Label(self, text="", font=('Helvetica', font_size), fg=font_color, bg='#000000')
        self.label.pack(padx=10, pady=10, expand=True)

        # icon_image = PhotoImage(file="./image/cl.png" )

        # 添加关闭按钮
        self.settings_button = tk.Button(self, text="X", command=self.close_py, bg='#A5A5A5')
        # 将按钮放置在右上角
        self.settings_button.pack(side="right", anchor="ne", padx=10, pady=10)

        # 添加设置按钮
        self.settings_button = tk.Button(self, text="设置", command=self.open_settings, bg='#A5A5A5')
        self.settings_button.pack(side="left", padx=10, pady=10)

        # style.configure("Custom.TButton", background="#BDBBBB")  # 设置背景色为红色

        # 添加重启按钮
        # self.restart_button = tk.Button(self, text="重启", command=self.restart_program)
        # self.restart_button.place(relx=1.0, rely=1.0, anchor='se')

        # 注册回调函数来处理按键事件
        keyboard.hook(self.on_key_event)

        # 记录信息到日志
        logging.info('Application started.')

    # def restart_program(self):
    #     python = sys.executable
    #     os.execl(python, python, *sys.argv)

    def close_py(self):
        try:
            os._exit(0)
        except Exception as e:
            # 记录异常到日志
            logging.error(f'Error opening settings: {str(e)}')

    def open_settings(self):
        # 打开设置窗口
        try:
            config_gui = SettingConfig.ConfigGUI()
            config_gui.mainloop()
        except Exception as e:
            # 记录异常到日志
            logging.error(f'Error opening settings: {str(e)}')

    def on_key_event(self, e):
        try:
            result = f'{e.name} {e.event_type}'
            # 更新标签文本
            self.label.config(text=result)
            # 在保留时间后清空标签文本
            self.after(self.retention_time, self.clear_label)
        except Exception as e:
            # 记录异常到日志
            logging.error(f'Error processing key event: {str(e)}')

    def clear_label(self):
        try:
            # 清空标签文本
            self.label.config(text="")
        except Exception as e:
            # 记录异常到日志
            logging.error(f'Error clearing label: {str(e)}')

if __name__ == '__main__':
    try:
        # 读取配置文件
        config = ConfigParser()
        config.read('config.ini')

        always_on_top_window = AlwaysOnTopWindow(config)
        always_on_top_window.mainloop()
    except Exception as e:
        # 记录异常到日志
        logging.error(f'Unexpected error: {str(e)}')