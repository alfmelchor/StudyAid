import customtkinter as ctk
import tkinter as tk
import json
from tkcalendar import Calendar
import datetime

import credentialsPage
import page_assignments
from page_assignments import AssignmentsPage, Assignment, import_assignments

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

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
                                             text="Dashboard", hover_color='#1C9670', width=100, height=25, anchor="w")
        self.dashboardButton.place(x=10, y=20)

        self.transfersButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                             text="Assignments", hover_color='#1C9670', width=100, height=25,
                                             anchor="w")
        self.transfersButton.place(x=10, y=60)

        self.schedulesButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                             text="Study Aid", hover_color='#1C9670', width=100, height=25, anchor="w")
        self.schedulesButton.place(x=10, y=100)

        self.settingsButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                            text="Settings", hover_color='#1C9670', width=100, height=25, anchor="w")
        self.settingsButton.place(x=10, y=140)

        self.versionLabel = ctk.CTkLabel(self.sidebar_frame, text_color='white', fg_color="transparent",
                                         text="Version: --", width=100, height=25)
        self.versionLabel.pack(side=tk.BOTTOM)

        self.lastSaveLabel = ctk.CTkLabel(self.sidebar_frame, text_color='white', fg_color="transparent",
                                          text="Last Saved: --", width=100, height=25)
        self.lastSaveLabel.pack(side=tk.BOTTOM)


def hidePages(credPage, page=None):
    global pg_assignments
    credPage.frame.destroy()
    Sidebar(window)
    Sidebar.active = True
    if page == 'Dashboard':
        pass
    elif page == 'Assignments':
        pg_assignments = AssignmentsPage(window)
        page_assignments.assn_page_frame = pg_assignments
        import_assignments(pg_assignments)
    elif page == 'Transfers':
        pass
    elif page == 'Schedules':
        pass


credentials = credentialsPage.CredentialsMenu(window)

hidePages(credentials, 'Assignments')

window.mainloop()
