import customtkinter as ctk
import tkinter as tk
from PIL import Image
import time
import json


class StudyAidPage:
    def __init__(self, parent):
        self.parent = parent
        self.session = None
        self.frame = ctk.CTkFrame(self.parent, width=970, height=600, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, column=1, sticky='nw')

        self.options_frame = ctk.CTkFrame(self.frame, width=970, height=40, corner_radius=0, fg_color='#414c59')
        self.options_frame.propagate(False)
        self.options_frame.pack(side=tk.TOP)

        self.timedButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                         text="Timed Session", hover_color='#1C9670', width=100, height=25,
                                         anchor="n", command=lambda: self.open_session('Timed'))
        self.timedButton.pack(side=tk.LEFT, padx=5)
        self.focusButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                         text="Focus Session", hover_color='#1C9670', width=100, height=25,
                                         anchor="n", command=lambda: self.open_session('Focus'))
        self.focusButton.pack(side=tk.LEFT, padx=5)

        self.open_session()

    def open_session(self, session_type=None):
        if self.session is not None:
            self.session.frame.destroy()

        if session_type == 'Timed':
            self.session = TimedSession(self.frame)
        else:
            self.session = FocusSession(self.frame)


class TimedSession:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, width=970, height=560)
        self.frame.propagate(False)
        self.frame.pack()

        self.session = ctk.CTkLabel(self.frame, text="Session 1", font=('Arial', 15)).pack(pady=5)
        self.timer = ctk.CTkLabel(self.frame, text="00:00:00", font=('Arial', 60, 'bold'))
        self.timer.pack(pady=0)

        self.start_button = ctk.CTkButton(self.frame, width=80, text="START", fg_color='#1C9670', hover_color='#197b5c',
                                          command=self.start_timer)
        self.start_button.place(x=355, y=130)

        self.stop_button = ctk.CTkButton(self.frame, width=80, text="STOP", fg_color='#1C9670', hover_color='#197b5c',
                                         command=self.stop_timer, state=ctk.DISABLED)
        self.stop_button.place(x=450, y=130)

        self.reset_button = ctk.CTkButton(self.frame, width=80, text="RESET", fg_color='#1C9670', hover_color='#197b5c', state='disabled', command=self.reset_timer)
        self.reset_button.place(x=545, y=130)

        self.start_time = None
        self.is_running = False
        self.elapsed_time = 0
        self.timer_id = None

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.configure(state=ctk.DISABLED)
            self.stop_button.configure(state=ctk.NORMAL)

            self.start_time = time.time() - self.elapsed_time
            self.update_timer()

    def update_timer(self):
        self.elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(self.elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        self.timer.configure(text="{:02.0f}:{:02.0f}:{:02.0f}".format(hours, minutes, seconds))

        if self.is_running:
            self.timer_id = self.parent.after(1000, self.update_timer)

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.reset_button.configure(state=ctk.NORMAL)
            self.start_button.configure(state=ctk.NORMAL)
            self.stop_button.configure(state=ctk.DISABLED)

            if self.timer_id:
                self.parent.after_cancel(self.timer_id)

    def reset_timer(self):
        self.elapsed_time = 0
        self.timer.configure(text="00:00:00")


class FocusSession:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, width=970, height=560)
        self.frame.propagate(False)
        self.frame.pack()

        self.session = ctk.CTkLabel(self.frame, text="Focus Session", font=('Arial', 20, 'bold')).pack(pady=10)

        self.timer_up = ctk.CTkButton(self.frame, text="", command=self.increment_timer, width=35, height=10,
                                      fg_color='#1C9670', hover_color='#197b5c',
                                      image=ctk.CTkImage(light_image=Image.open('icons/arrow_icon.png').rotate(180),
                                                         size=(15, 12)))
        self.timer_up.pack()

        self.timer = ctk.CTkLabel(self.frame, text="00:00:00", font=('Arial', 60, 'bold'))
        self.timer.pack()

        self.timer_down = ctk.CTkButton(self.frame, text="", command=self.decrement_timer, width=35, height=10,
                                        fg_color='#1C9670', hover_color='#197b5c',
                                        image=ctk.CTkImage(light_image=Image.open('icons/arrow_icon.png'),
                                                           size=(15, 12)))
        self.timer_down.pack()

        self.start_button = ctk.CTkButton(self.frame, width=80, text="START", fg_color='#1C9670', hover_color='#197b5c',
                                          command=self.start_timer, state='disabled')
        self.start_button.place(x=350, y=190)

        self.pause_button = ctk.CTkButton(self.frame, width=80, text="PAUSE", fg_color='#1C9670', hover_color='#197b5c',
                                          command=self.pause_timer, state='disabled')
        self.pause_button.place(x=445, y=190)

        self.reset_button = ctk.CTkButton(self.frame, width=80, text="RESET", fg_color='#1C9670', hover_color='#197b5c',
                                          command=self.reset_timer, state='disabled')
        self.reset_button.place(x=540, y=190)

        self.timer_running = False
        self.paused = False
        self.total_seconds = 0

    def increment_timer(self):
        self.total_seconds += 60
        self.update_time()

    def decrement_timer(self):
        if self.total_seconds >= 60:
            self.total_seconds -= 60
            self.update_time()

    def update_time(self):
        hours = self.total_seconds // 3600
        minutes = (self.total_seconds // 60) % 60
        seconds = self.total_seconds % 60
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.timer.configure(text=time_string)
        if self.total_seconds == 0:
            self.start_button.configure(state='disabled')
        else:
            self.start_button.configure(state='normal')
            self.reset_button.configure(state='normal')

    def start_timer(self):
        self.timer_running = True
        self.pause_button.configure(state='normal')
        self.run_timer()

    def run_timer(self):
        if self.timer_running:
            self.total_seconds -= 1
            self.update_time()
            if self.total_seconds > 0:
                self.frame.after(1000, self.run_timer)
            else:
                self.timer_running = False

    def pause_timer(self):
        self.timer_running = False
        self.paused = True

    def reset_timer(self):
        self.timer_running = False
        self.total_seconds = 0
        self.pause_button.configure(state='disabled')
        self.reset_button.configure(state='disabled')
        self.update_time()
