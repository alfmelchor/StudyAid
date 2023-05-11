import customtkinter as ctk
import tkinter as tk
from PIL import Image


class StudyAidPage:
    def __init__(self, parent, elements):
        self.parent = parent
        self.elements_parent = elements
        self.session = None
        self.current_session = None
        self.frame = ctk.CTkFrame(self.parent.root, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, rowspan=6, column=1, columnspan=6, sticky='nsew')
        self.frame.rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.frame.columnconfigure((1, 2, 3, 4, 5), weight=1)

        self.options_frame = ctk.CTkFrame(self.frame, height=40, corner_radius=0, fg_color='#414c59')
        self.options_frame.propagate(False)
        self.options_frame.grid(row=0, column=0, columnspan=6, sticky='nsew')

        self.timedButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                         text="Timed Session", width=100, height=25,
                                         anchor="n", command=lambda: self.open_session('Timed'))
        self.timedButton.pack(side=tk.LEFT, padx=5)
        self.focusButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                         text="Focus Session", width=100, height=25,
                                         anchor="n", command=lambda: self.open_session('Focus'))
        self.focusButton.pack(side=tk.LEFT, padx=5)

        self.open_session()

    def open_session(self, session_type='Focus'):
        if session_type == 'Timed' and self.current_session != 'Timed':
            self.current_session = 'Timed'
            self.session = TimedSession(self, self.elements_parent)
        elif session_type == 'Focus' and self.current_session != 'Focus':
            self.current_session = 'Focus'
            self.session = FocusSession(self)


class StudyAidWindow:
    def __init__(self, parent, elements):
        self.parent = parent
        self.elements = elements
        self.frame = ctk.CTkFrame(self.parent.root, width=40, height=40, corner_radius=40, bg_color='#D9D9D9',
                                  fg_color='#414c59')
        self.frame.propagate(False)
        self.frame_expanded = False
        self.frame.grid(row=6, column=6, padx=5, pady=5, sticky="nsew")
        self.frame.rowconfigure((1, 2, 3, 4), weight=1)
        self.frame.columnconfigure((1, 2, 3), weight=1)

        self.button = ctk.CTkButton(self.frame, text="", bg_color='transparent', width=20, height=20,
                                    corner_radius=20, command=self.frame_action)
        self.button.pack(pady=10)

        self.title = ctk.CTkLabel(self.frame, text="Timed Session", font=('Arial', 20, 'bold'), text_color='white')
        self.title.pack()

        self.timer = ctk.CTkLabel(self.frame, text="00:00:00", font=('Arial', 15), text_color='white')
        self.timer.pack()

    def frame_action(self):
        if self.frame_expanded:
            self.minimize()
            self.frame_expanded = False
        else:
            self.expand()
            self.frame_expanded = True

    def expand(self):
        if self.frame.winfo_width() < 250:
            self.frame.configure(width=self.frame.winfo_width() + 4)

        if self.frame.winfo_height() < 120:
            self.frame.configure(height=self.frame.winfo_height() + 2)

        if self.frame.winfo_width() < 250 or self.frame.winfo_height() < 120:
            self.frame.after(1, self.expand)

    def minimize(self):
        if self.frame.winfo_width() > 40:
            self.frame.configure(width=self.frame.winfo_width() - 4)

        if self.frame.winfo_height() > 40:
            self.frame.configure(height=self.frame.winfo_height() - 2)

        if self.frame.winfo_width() > 40 or self.frame.winfo_height() > 40:
            self.frame.after(1, self.minimize)


class TimedSession:
    def __init__(self, parent, elements):
        self.parent = parent
        self.elements = elements
        self.frame = ctk.CTkFrame(self.parent.frame, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, rowspan=6, column=1, columnspan=6, sticky='nsew')
        self.frame.rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.frame.columnconfigure((1, 2, 3, 4, 5), weight=1)

        self.session = ctk.CTkLabel(self.frame, text="Session 1", font=('Arial', 15)).pack(pady=5)
        self.timer = ctk.CTkLabel(self.frame, text="00:00:00", font=('Arial', 60, 'bold'))
        self.timer.pack(pady=0)

        self.start_button = ctk.CTkButton(self.frame, width=80, text="START",
                                          command=lambda: self.elements.timed_start(self.parent.session))
        self.start_button.grid(row=3, column=2)

        self.stop_button = ctk.CTkButton(self.frame, width=80, text="STOP", command=self.elements.timed_stop)
        self.stop_button.grid(row=3, column=3)

        self.reset_button = ctk.CTkButton(self.frame, width=80, text="RESET", command=self.elements.timed_reset)
        self.reset_button.grid(row=3, column=4)

        self.elements.child = self

    def reset_timer(self):
        self.timer.configure(text="00:00:00")


class FocusSession:
    def __init__(self, parent):
        self.parent = parent.frame
        self.frame = ctk.CTkFrame(self.parent, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, rowspan=6, column=1, columnspan=6, sticky='nsew')
        self.frame.rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.frame.columnconfigure((1, 2, 3, 4, 5), weight=1)

        self.session = ctk.CTkLabel(self.frame, text="Focus Session", font=('Arial', 20, 'bold')).pack(pady=10)

        self.timer_up = ctk.CTkButton(self.frame, text="", command=self.increment_timer, width=35, height=10,
                                      image=ctk.CTkImage(light_image=Image.open('icons/arrow_icon.png').rotate(180),
                                                         size=(15, 12)))
        self.timer_up.pack()

        self.timer = ctk.CTkLabel(self.frame, text="00:00:00", font=('Arial', 60, 'bold'))
        self.timer.pack()

        self.timer_down = ctk.CTkButton(self.frame, text="", command=self.decrement_timer, width=35, height=10,
                                        image=ctk.CTkImage(light_image=Image.open('icons/arrow_icon.png'),
                                                           size=(15, 12)))
        self.timer_down.pack()

        self.start_button = ctk.CTkButton(self.frame, width=80, text="START", command=self.start_timer,
                                          state='disabled')
        self.start_button.grid(row=3, column=2)

        self.pause_button = ctk.CTkButton(self.frame, width=80, text="PAUSE", command=self.pause_timer,
                                          state='disabled')
        self.pause_button.grid(row=3, column=3)

        self.reset_button = ctk.CTkButton(self.frame, width=80, text="RESET", command=self.reset_timer,
                                          state='disabled')
        self.reset_button.grid(row=3, column=4)

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
