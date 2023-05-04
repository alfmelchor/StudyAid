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
        self.frame = ctk.CTkFrame(self.parent, corner_radius=0)
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
        elif settings == 'StudyAidSettings':
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
                                          command=lambda: self.set_active_color(self.green_accent, 'green'))
        self.green_accent.place(x=10, y=85)
        self.blue_accent = ctk.CTkButton(self.frame, text="", width=30, height=30, corner_radius=30,
                                         fg_color='#3a7ebf', hover_color='#325882',
                                         command=lambda: self.set_active_color(self.blue_accent, 'blue'))
        self.blue_accent.place(x=50, y=85)
        self.red_accent = ctk.CTkButton(self.frame, text="", width=30, height=30, corner_radius=30, fg_color='red',
                                        hover_color='dark red',
                                        command=lambda: self.set_active_color(self.red_accent, 'red'))
        self.red_accent.place(x=90, y=85)
        self.yellow_accent = ctk.CTkButton(self.frame, text="", width=30, height=30, corner_radius=30,
                                           fg_color='yellow', hover_color='#ccc233',
                                           command=lambda: self.set_active_color(self.yellow_accent, 'yellow'))
        self.yellow_accent.place(x=130, y=85)

    def set_active_color(self, accent, color):
        if self.active_accent_button is not None:
            self.active_accent_button.configure(border_width=0)

        accent.configure(border_color='white', border_width=2)
        self.active_accent_button = accent
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
