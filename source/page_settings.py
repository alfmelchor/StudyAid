import customtkinter as ctk
import tkinter as tk
import json


class SettingsPage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, width=1480, height=900, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, column=1, sticky='nw')

        self.sidebar_frame = ctk.CTkFrame(self.frame, width=140, height=900, corner_radius=0, fg_color='#414c59')
        self.sidebar_frame.propagate(False)
        self.sidebar_frame.pack(side=tk.LEFT)

        self.startupButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                           text="Startup", hover_color='#1C9670', width=100, height=25, anchor="w")
        self.startupButton.place(x=10, y=20)
        self.interactionButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                               text="Interaction", hover_color='#1C9670', width=100, height=25,
                                               anchor="w")
        self.interactionButton.place(x=10, y=60)
        self.appearanceButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                              text="Appearance", hover_color='#1C9670', width=100, height=25,
                                              anchor="w")
        self.appearanceButton.place(x=10, y=100)
        self.studyAidButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                            text="Buddy", hover_color='#1C9670', width=100, height=25,
                                            anchor="w")
        self.studyAidButton.place(x=10, y=140)
        self.debugButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                         text="Debug", hover_color='#1C9670', width=100, height=25,
                                         anchor="w")
        self.debugButton.place(x=10, y=180)
