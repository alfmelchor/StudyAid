import customtkinter as ctk
import tkinter as tk
import json
from PIL import Image

with open('config.json', 'r') as file:
    data = json.load(file)
    version = data['Version']
    appearance = data['Appearance']
    accent_color = data["Accent_Color"]
    file.close()


class SettingsPage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent.root, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, rowspan=6, column=1, columnspan=6, sticky='nsew')
        self.frame.rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.frame.columnconfigure((1, 2, 3, 4, 5), weight=1)

        self.options_frame = ctk.CTkFrame(self.frame, height=40, corner_radius=0, fg_color='#414c59')
        self.options_frame.propagate(False)
        self.options_frame.grid(row=0, column=0, columnspan=6, sticky='nsew')

        self.interactionButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                               text="Interaction", width=100, height=25,
                                               anchor="n", state='normal',
                                               command=lambda: self.open_settings('Interaction'))
        self.interactionButton.pack(side=tk.LEFT, padx=5)
        self.studyAidButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                            text="Study Aid", width=100, height=25,
                                            anchor="n", state='normal',
                                            command=lambda: self.open_settings('StudyAid'))
        self.studyAidButton.pack(side=tk.LEFT, padx=5)
        self.changesButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                           text="Change Log", width=100, height=25,
                                           anchor="n", state='normal',
                                           command=lambda: self.open_settings('ChangeLog'))
        self.changesButton.pack(side=tk.LEFT, padx=5)

        self.open_settings('Interaction')

    def open_settings(self, settings):
        if settings == 'Interaction':
            page = InteractionSettings(self.frame)
        elif settings == 'StudyAid':
            page = StudyAidSettings(self.frame)
        elif settings == 'ChangeLog':
            page = ChangeLog(self.frame)


class InteractionSettings:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, rowspan=6, columnspan=6, sticky='nsew')

        # Settings Variables
        self.active_accent_button = None
        self.active_color = None

        # Section Header
        ctk.CTkLabel(self.frame, text="Appearance", font=('TimesNewRoman', 20, 'bold')).pack(anchor='nw', padx=10,
                                                                                             pady=10)

        # Section Body
        ctk.CTkLabel(self.frame, text="Choose your accent color.", font=('TimesNewRoman', 15)).pack(anchor='nw',
                                                                                                    padx=10, pady=5)
        self.green_accent = ctk.CTkButton(self.frame, text="", width=30, height=30, corner_radius=30,
                                          fg_color='#1C9670', hover_color='#197b5c',
                                          command=lambda: self.set_active_color('green'))
        self.green_accent.place(x=10, y=85)
        self.blue_accent = ctk.CTkButton(self.frame, text="", width=30, height=30, corner_radius=30,
                                         fg_color='#3a7ebf', hover_color='#325882',
                                         command=lambda: self.set_active_color('blue'))
        self.blue_accent.place(x=50, y=85)
        self.red_accent = ctk.CTkButton(self.frame, text="", width=30, height=30, corner_radius=30, fg_color='red',
                                        hover_color='dark red',
                                        command=lambda: self.set_active_color('red'))
        self.red_accent.place(x=90, y=85)
        self.yellow_accent = ctk.CTkButton(self.frame, text="", width=30, height=30, corner_radius=30,
                                           fg_color='yellow', hover_color='#ccc233',
                                           command=lambda: self.set_active_color('yellow'))
        self.yellow_accent.place(x=130, y=85)

        self.set_active_color(accent_color)

    def set_active_color(self, color):
        if self.active_accent_button is not None:
            self.active_accent_button.configure(border_width=0)

        if color == 'green':
            self.green_accent.configure(border_color='white', border_width=2)
            self.active_accent_button = self.green_accent
        elif color == 'blue':
            self.blue_accent.configure(border_color='white', border_width=2)
            self.active_accent_button = self.blue_accent
        elif color == 'red':
            self.red_accent.configure(border_color='white', border_width=2)
            self.active_accent_button = self.red_accent
        elif color == 'yellow':
            self.yellow_accent.configure(border_color='white', border_width=2)
            self.active_accent_button = self.yellow_accent

        self.active_color = color

        with open('config.json', 'r') as file:
            data = json.load(file)

        data['Accent_Color'] = self.active_color

        with open('config.json', 'w') as file:
            json.dump(data, file, indent=2)


class StudyAidSettings:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, rowspan=6, columnspan=6, sticky='nsew')

        ctk.CTkLabel(self.frame, text="Study Aid Window", font=('TimesNewRoman', 20, 'bold')).pack(anchor='nw', padx=10,
                                                                                                   pady=10)
        ctk.CTkLabel(self.frame, text="Show pop-up window for study sessions", font=('TimesNewRoman', 15)).pack(
            anchor='nw', padx=10, pady=5)
        self.sawin_show = ctk.CTkSwitch(self.frame, text="", command=self.write_settings)
        self.sawin_show.place(x=330, y=56)

        ctk.CTkLabel(self.frame, text="Minimize window automatically on new page", font=('TimesNewRoman', 15)).pack(
            anchor='nw', padx=10, pady=5)
        self.sawin_automin = ctk.CTkSwitch(self.frame, text="", command=self.write_settings)
        self.sawin_automin.place(x=330, y=93)

        ctk.CTkLabel(self.frame, text="Focus Session Settings", font=('TimesNewRoman', 20, 'bold')).pack(anchor='nw',
                                                                                                         padx=10,
                                                                                                         pady=10)
        ctk.CTkLabel(self.frame, text="Allow manual breaks", font=('TimesNewRoman', 15)).pack(anchor='nw', padx=10,
                                                                                              pady=5)
        ctk.CTkSwitch(self.frame, text="").place(x=165, y=180)

        ctk.CTkLabel(self.frame, text="Frequency of breaks", font=('TimesNewRoman', 15)).pack(anchor='nw', padx=10,
                                                                                              pady=5)
        ctk.CTkOptionMenu(self.frame, values=['15 min', '30 min'], width=50, height=25).place(x=165, y=217)

        self.read_settings()

    def read_settings(self):
        with open('config.json', 'r') as file:
            data = json.load(file)

        if data["SAWIN_SHOW"] == 1:
            self.sawin_show.select()
        if data["SAWIN_AUTOMIN"] == 1:
            self.sawin_automin.select()

    def write_settings(self):
        with open('config.json', 'r') as file:
            data = json.load(file)

        data['SAWIN_SHOW'] = self.sawin_show.get()
        data['SAWIN_AUTOMIN'] = self.sawin_automin.get()

        with open('config.json', 'w') as file:
            json.dump(data, file, indent=2)





class ChangeLog:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, rowspan=6, columnspan=6, sticky='nsew')

        if appearance == 'Dark':
            cl_bg = '#333333'
            cl_fg = 'white'
        else:
            cl_bg = '#DBDBDB'
            cl_fg = 'black'

        self.text = tk.Text(self.frame, width=950, height=550, bg=cl_bg, fg=cl_fg)
        self.text.pack()

        with open('changelog.txt', 'r') as changelog:
            changelog_text = changelog.read()
            self.text.insert('1.0', changelog_text)

        self.text.tag_configure('bold', font=('TkDefaultFont', 12, 'bold'))
        start_idx = '1.0'
        while True:
            start_idx = self.text.search('VERSION', start_idx, 'end')
            if not start_idx:
                break
            line_end_idx = self.text.search('\n', start_idx, 'end')
            if not line_end_idx:
                line_end_idx = 'end'
            self.text.tag_add('bold', start_idx, line_end_idx)
            start_idx = line_end_idx

        self.text.configure(state='disabled')
