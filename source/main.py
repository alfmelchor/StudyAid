import customtkinter as ctk
import tkinter as tk
from PIL import Image
import json

import page_assignments
import page_settings
import page_studyaid

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600

with open('config.json', 'r') as f:
    data = json.load(f)
    version = data['Version']
    appearance = data['Appearance']
    f.close()

ctk.set_appearance_mode(appearance)
ctk.set_default_color_theme('themes/green.json')


class App:  # Creates the root window for the program
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Study Aid")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.root.columnconfigure((1, 2, 3, 4, 5), weight=1)


app = App()


class Sidebar:  # Class to handle the Sidebar on the window
    def __init__(self, parent):
        self.parent = parent
        self.active = False
        self.sidebar_frame = ctk.CTkFrame(self.parent, width=130, corner_radius=0, fg_color='#212932')
        self.sidebar_frame.propagate(False)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)

        self.dashboardButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                             text="Dashboard", hover_color='#1C9670', width=100, height=25, anchor="w",
                                             command=lambda: open_page('Dashboard'),
                                             image=ctk.CTkImage(light_image=Image.open('icons/home.png'),
                                                                size=(15, 12)), state='disabled')
        self.dashboardButton.place(x=10, y=20)
        self.assignmentsButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                               text="Assignments", hover_color='#1C9670', width=100, height=25,
                                               anchor="w", command=lambda: open_page('Assignments'),
                                               image=ctk.CTkImage(light_image=Image.open('icons/assignment.png'),
                                                                  size=(12, 12)))
        self.assignmentsButton.place(x=10, y=60)

        self.studyAidButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                            text="Study Aid", hover_color='#1C9670', width=100, height=25, anchor="w",
                                            command=lambda: open_page('StudyAid'),
                                            image=ctk.CTkImage(light_image=Image.open('icons/noteball.png'),
                                                               size=(12, 12)))
        self.studyAidButton.place(x=10, y=100)

        self.settingsButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                            text="Settings", hover_color='#1C9670', width=100, height=25, anchor="w",
                                            command=lambda: open_page('Settings'),
                                            image=ctk.CTkImage(light_image=Image.open('icons/settings.png'),
                                                               size=(12, 12)))
        self.settingsButton.place(x=10, y=140)

        self.versionLabel = ctk.CTkLabel(self.sidebar_frame, text_color='white', fg_color="transparent",
                                         text=f"Version: {version}", width=100, height=25)
        self.versionLabel.pack(side=tk.BOTTOM)


def open_page(page):
    global opened_page
    try:
        opened_page.frame.destroy()
    except NameError:
        pass
    if page == 'Dashboard':  # Opens the Dashboard page
        Sidebar(app.root)

    elif page == 'Assignments':  # Opens the Assignments page
        Sidebar(app.root)
        opened_page = page_assignments.AssignmentsPage(app.root)
        page_assignments.assn_page_frame = opened_page
        page_assignments.import_assignments(opened_page)

    elif page == 'StudyAid':  # Opens the Study Aid page
        Sidebar(app.root)
        opened_page = page_studyaid.StudyAidPage(app.root)

    elif page == 'Settings':  # Opens the Settings page
        Sidebar(app.root)
        opened_page = page_settings.SettingsPage(app.root)


# Initial Calls
open_page('Settings')

app.root.mainloop()
