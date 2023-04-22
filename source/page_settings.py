import customtkinter as ctk
import tkinter as tk
import json


class SettingsPage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, width=970, height=600, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, column=1, sticky='nw')

        self.options_frame = ctk.CTkFrame(self.frame, width=970, height=40, corner_radius=0, fg_color='#414c59')
        self.options_frame.propagate(False)
        self.options_frame.pack(side=tk.TOP)

        self.startupButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                           text="Startup", hover_color='#1C9670', width=100, height=25, anchor="n",
                                           command=lambda: self.open_settings('Startup'))
        self.startupButton.pack(side=tk.LEFT, padx=5)
        self.interactionButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                               text="Interaction", hover_color='#1C9670', width=100, height=25,
                                               anchor="n", command=lambda: self.open_settings('Interaction'))
        self.interactionButton.pack(side=tk.LEFT, padx=5)
        self.studyAidButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                            text="Buddy", hover_color='#1C9670', width=100, height=25,
                                            anchor="n", state='disabled',
                                            command=lambda: self.open_settings('StudyAid'))
        self.studyAidButton.pack(side=tk.LEFT, padx=5)
        self.debugButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                         text="Debug", hover_color='#1C9670', width=100, height=25,
                                         anchor="n", state='disabled', command=lambda: self.open_settings('Debug'))
        self.debugButton.pack(side=tk.LEFT, padx=5)

        self.open_settings('Startup')

    def open_settings(self, settings):
        if settings == 'Startup':
            page = StartupSettings(self.frame)
        elif settings == 'Interaction':
            page = InteractionSettings(self.frame)
        elif settings == 'StudyAid':
            page = StudyAidSettings(self.frame)
        elif settings == 'Debug':
            page = DebugSettings(self.frame)


class StartupSettings:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, width=1480, height=850, corner_radius=0)
        self.frame.propagate(False)
        self.frame.pack()


class InteractionSettings:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, width=1480, height=850, corner_radius=0)
        self.frame.propagate(False)
        self.frame.pack()


class StudyAidSettings:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, width=1480, height=850, corner_radius=0)
        self.frame.propagate(False)
        self.frame.pack()


class DebugSettings:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, width=1480, height=850, corner_radius=0)
        self.frame.propagate(False)
        self.frame.pack()
