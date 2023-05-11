import customtkinter as ctk
import tkinter as tk
from PIL import Image
import json
import time

import page_assignments
import page_settings
import page_studyaid

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

with open('config.json', 'r') as f:
    data = json.load(f)
    version = data['Version']
    appearance = data['Appearance']
    accent_color = data["Accent_Color"]
    sawin_show = data["SAWIN_SHOW"]
    sawin_automin = data["SAWIN_AUTOMIN"]
    f.close()

ctk.set_appearance_mode(appearance)


class Application:  # Creates the root window for the program
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Study Aid")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.root.columnconfigure((1, 2, 3, 4, 5), weight=1)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)


class StudyAidTimedElements:
    def __init__(self, parent):
        self.timer = "00:00:00"
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False
        self.timer_id = None
        self.child = None

    def timed_start(self, child):
        if self.is_running is False:
            self.child = child
            self.is_running = True
            self.start_time = time.time() - self.elapsed_time
            self.timed_update()

    def timed_update(self):
        self.elapsed_time = time.time() - self.start_time
        minutes, seconds = divmod(self.elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        self.timer = ("{:02.0f}:{:02.0f}:{:02.0f}".format(hours, minutes, seconds))
        if sawin_show == 1:
            study_window.timer.configure(text=self.timer)
        try:
            self.child.timer.configure(text=self.timer)
        except:
            pass
        if self.is_running:
            self.timer_id = app.root.after(1000, self.timed_update)

    def timed_stop(self):
        if self.is_running:
            self.is_running = False
            if self.timer_id:
                app.root.after_cancel(self.timer_id)

    def timed_reset(self):
        self.timer = "00:00:00"
        if sawin_show == 1:
            study_window.timer.configure(text="00:00:00")
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False
        self.timer_id = None
        self.child.reset_timer()


class StudyAidFocusElements:
    def __init__(self, parent):
        self.timer_running = False
        self.paused = False
        self.total_seconds = 0


app = Application()
sa_timed_elements = StudyAidTimedElements(app)
sa_focus_elements = StudyAidFocusElements(app)
if sawin_show == 1:
    study_window = page_studyaid.StudyAidWindow(app, sa_timed_elements)


class Sidebar:  # Class to handle the Sidebar on the window
    def __init__(self, parent):
        self.parent = parent
        self.active = False
        self.sidebar_frame = ctk.CTkFrame(self.parent, width=130, corner_radius=0, fg_color='#212932')
        self.sidebar_frame.propagate(False)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)

        self.dashboardButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                             text="Dashboard", width=100, height=25, anchor="w",
                                             command=lambda: open_page('Dashboard'),
                                             image=ctk.CTkImage(light_image=Image.open('icons/home.png'),
                                                                size=(15, 12)), state='disabled')
        self.dashboardButton.place(x=10, y=20)
        self.assignmentsButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                               text="Assignments", width=100, height=25,
                                               anchor="w", command=lambda: open_page('Assignments'),
                                               image=ctk.CTkImage(light_image=Image.open('icons/assignment.png'),
                                                                  size=(12, 12)))
        self.assignmentsButton.place(x=10, y=60)

        self.studyAidButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                            text="Study Aid", width=100, height=25, anchor="w",
                                            command=lambda: open_page('StudyAid'),
                                            image=ctk.CTkImage(light_image=Image.open('icons/noteball.png'),
                                                               size=(12, 12)))
        self.studyAidButton.place(x=10, y=100)

        self.settingsButton = ctk.CTkButton(self.sidebar_frame, text_color='white', fg_color="transparent",
                                            text="Settings", width=100, height=25, anchor="w",
                                            command=lambda: open_page('Settings'),
                                            image=ctk.CTkImage(light_image=Image.open('icons/settings.png'),
                                                               size=(12, 12)))
        self.settingsButton.place(x=10, y=140)

        self.versionLabel = ctk.CTkLabel(self.sidebar_frame, text_color='white', fg_color="transparent",
                                         text=f"Version: {version}", width=100, height=25)
        self.versionLabel.pack(side=tk.BOTTOM)


def open_page(page):
    global opened_frame, opened_page
    Sidebar(app.root)

    try:
        opened_frame.frame.destroy()
    except NameError:
        pass

    if page == 'Dashboard':  # Opens the Dashboard page
        pass

    elif page == 'Assignments':  # Opens the Assignments page
        opened_frame = page_assignments.AssignmentsPage(app)
        page_assignments.assn_page_frame = opened_frame
        page_assignments.import_assignments(opened_frame)  # EDIT TO PREVENT SPAMMING // IN IMPORT_ASSIGNMENTS
        opened_page = 'Assignments'

    elif page == 'StudyAid':  # Opens the Study Aid page
        opened_frame = page_studyaid.StudyAidPage(app, sa_timed_elements)
        opened_page = 'StudyAid'
        # sa_timed_elements.child.timer.configure(text=sa_timed_elements.timer)

    elif page == 'Settings':  # Opens the Settings page
        opened_frame = page_settings.SettingsPage(app)
        opened_page = 'Settings'

    if sawin_show == 1:
        study_window.frame.lift()


# Initial Calls
open_page('StudyAid')
app.root.mainloop()
