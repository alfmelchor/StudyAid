import customtkinter as ctk
import tkinter as tk
import json
from tkcalendar import Calendar
import datetime

import page_credentials
import page_assignments
import page_settings

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

ctk.set_appearance_mode("Light")
window = ctk.CTk()  # Creates the root window for the program
window.title("Study Aid - DEVELOPMENT")  # Sets the title for the program
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  # Sets the geometry for the program
window.resizable(False, False)  # Disables resizing, soon to be removed once frame resizing is configured
window.rowconfigure((1, 2, 3, 4, 5), weight=1)
window.columnconfigure((1, 2, 3, 4, 5), weight=1)


class Sidebar:  # Class to handle the Sidebar on the window
    def __init__(self, parent):
        self.parent = parent
        self.active = False
        self.sidebar_frame = ctk.CTkFrame(self.parent, width=130, corner_radius=0, fg_color='#212932')
        self.sidebar_frame.propagate(False)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.sidebar_frame.propagate(False)

        self.dashboardButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                             text="Dashboard", hover_color='#1C9670', width=100, height=25, anchor="w",
                                             command=lambda: open_page('Dashboard'))
        self.dashboardButton.place(x=10, y=20)

        self.assignmentsButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                               text="Assignments", hover_color='#1C9670', width=100, height=25,
                                               anchor="w", command=lambda: open_page('Assignments'))
        self.assignmentsButton.place(x=10, y=60)

        self.studyAidButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                            text="Study Aid", hover_color='#1C9670', width=100, height=25, anchor="w",
                                            command=lambda: open_page('Study Aid'))
        self.studyAidButton.place(x=10, y=100)

        self.settingsButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                            text="Settings", hover_color='#1C9670', width=100, height=25, anchor="w",
                                            command=lambda: open_page('Settings'))
        self.settingsButton.place(x=10, y=140)

        self.versionLabel = ctk.CTkLabel(self.sidebar_frame, text_color='white', fg_color="transparent",
                                         text="Version: --", width=100, height=25)
        self.versionLabel.pack(side=tk.BOTTOM)

        self.lastSaveLabel = ctk.CTkLabel(self.sidebar_frame, text_color='white', fg_color="transparent",
                                          text="Last Saved: --", width=100, height=25)
        self.lastSaveLabel.pack(side=tk.BOTTOM)


# noinspection PyGlobalUndefined
def open_page(page):
    global opened_page
    if page == 'Credentials':  # Opens the Login page
        def credentialsCallback(result):
            open_page('Assignments')
        opened_page = page_credentials.CredentialsMenu(window, credentialsCallback)

    else:
        try:
            opened_page.frame.destroy()
        except NameError:
            pass
        if page == 'Dashboard':  # Opens the Dashboard page
            Sidebar(window)

        elif page == 'Assignments':  # Opens the Assignments page
            Sidebar(window)
            opened_page = page_assignments.AssignmentsPage(window)
            page_assignments.assn_page_frame = opened_page
            page_assignments.import_assignments(opened_page)

        elif page == 'Study Aid':  # Opens the Study Aid page
            Sidebar(window)

        elif page == 'Settings':  # Opens the Settings page
            Sidebar(window)
            opened_page = page_settings.SettingsPage(window)


# Initial Calls
open_page('Settings')

window.mainloop()
