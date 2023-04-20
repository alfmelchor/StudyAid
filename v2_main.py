import customtkinter as ctk
import tkinter as tk
import json
from tkcalendar import Calendar
import datetime

import credentialsPage
from page_assignments import AssignmentsPage, Assignment

ctk.set_appearance_mode("Light")
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
window = ctk.CTk()
window.title("Study Buddy")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.rowconfigure((1, 2, 3, 4, 5), weight=1)
window.columnconfigure((1, 2, 3, 4, 5), weight=1)


class Sidebar:
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
    sidebar = Sidebar(window)
    sidebar.active = True
    if page == 'Dashboard':
        pg_assignments = AssignmentsPage(window)
        import_assignments()

    elif page == 'Transfers':
        pass
    elif page == 'Schedules':
        pass


assignments_made = []


def import_assignments():  # Function to import assignments from the JSON file
    try:
        with open("user_assn.json", "r") as file:
            assignments = json.load(file)
            for assn in assignments:
                assignment = Assignment(pg_assignments.childrenFrame, f"{assn['name']}", f"{assn['class']}",
                                        f"{assn['duedate']}", f"{assn['duetime']}", f"{assn['platform']}",
                                        f"{assn['status']}")
                assignment.assignmentStatus.set(assn['status'])
                assignments_made.append(assignment.frame)

    except json.decoder.JSONDecodeError:
        pass


credentials = credentialsPage.CredentialsMenu(window)
credentials.loginButton.configure(command=lambda credPage=credentials: hidePages(credPage, 'Schedules'))

hidePages(credentials, 'Dashboard')

window.mainloop()
