import customtkinter as ctk
import tkinter as tk
import json
from tkcalendar import Calendar
import datetime

assn_page_frame = None
assignments_made = []


class AssignmentsPage:  # Class to handle the main frame that holds the header and the individual assignments
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent, corner_radius=0)
        self.frame.propagate(False)
        self.frame.grid(row=1, rowspan=6, column=1, columnspan=6, sticky='nsew')
        self.frame.rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.frame.columnconfigure((1, 2, 3, 4, 5), weight=1)

        # Header Frame
        self.headerFrame = ctk.CTkFrame(self.frame, height=35, corner_radius=0, fg_color='#414c59')
        self.headerFrame.propagate(False)
        self.headerFrame.grid(row=0, column=0, columnspan=6, sticky='nsew')

        self.label = ctk.CTkLabel(self.headerFrame, width=100, height=30, text="Assignment Name",
                                  font=('Arial', 15), text_color='white',).pack(side=tk.LEFT, padx=15)
        self.label = ctk.CTkLabel(self.headerFrame, width=100, height=30, text="Class", text_color='white',
                                  font=('Arial', 15)).pack(side=tk.LEFT, padx=20)
        self.label = ctk.CTkLabel(self.headerFrame, width=100, height=30, text="Due Date", text_color='white',
                                  font=('Arial', 15)).pack(side=tk.LEFT, padx=20)
        self.label = ctk.CTkLabel(self.headerFrame, width=100, height=30, text="Platform", text_color='white',
                                  font=('Arial', 15)).pack(side=tk.LEFT, padx=20)
        self.label = ctk.CTkLabel(self.headerFrame, width=100, height=30, text="Status", text_color='white',
                                  font=('Arial', 15)).pack(side=tk.LEFT, padx=10)

        self.sortbyButton = ctk.CTkOptionMenu(self.headerFrame, width=35, height=25,
                                              values=['Sort By: Due Date', 'Sort By: Status', 'Sort By: Class'],
                                              fg_color='#1C9670', button_color='#1C9670', button_hover_color='#197b5c',
                                              dropdown_hover_color='#197b5c')
        self.sortbyButton.pack(side=tk.RIGHT)

        self.createNewButton = ctk.CTkButton(self.headerFrame, width=35, height=25, text="+", anchor="center", command=self.create_new_assignment)
        self.createNewButton.pack(side=tk.RIGHT)

        # Scrollable Frame, parent for all Assignment frames
        self.childrenFrame = ctk.CTkScrollableFrame(self.frame, corner_radius=0)
        self.childrenFrame.pack(pady=15)
        self.childrenFrame.grid(row=1, rowspan=6, column=1, columnspan=6, sticky='nsew')

    @staticmethod
    def create_new_assignment():
        new = AddAssnWindow()
        new.assn_page_frame = assn_page_frame

    @staticmethod
    def update_assignment_list():
        for assn in assignments_made:
            assn.destroy()


class AddAssnWindow(ctk.CTkToplevel):  # Additional window to handle the options to create a new assignment
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x600")
        self.resizable(False, False)
        self.title("New Assignment")

        self.label = ctk.CTkLabel(self, text="New Assignment", font=('Arial', 22, 'bold', 'underline'))
        self.label.pack(pady=10)

        self.assn_name_hdr = ctk.CTkLabel(self, text="Assignment Name", font=('Arial', 15, 'bold')).pack(pady=8)
        self.assignment_name = ctk.CTkEntry(self, placeholder_text="Assignment Name")
        self.assignment_name.pack(pady=2)

        self.assn_class_hdr = ctk.CTkLabel(self, text="Class", font=('Arial', 15, 'bold')).pack(pady=8)
        self.assignment_class = ctk.CTkOptionMenu(self, width=70,
                                                  values=['Period 0', 'Period 1', 'Period 2', 'Period 3',
                                                          'Period 4', 'Period 5', 'Period 6'], anchor=tk.CENTER)
        self.assignment_class.pack(pady=2)

        self.assn_duedate_hdr = ctk.CTkLabel(self, text="Due Date and Time", font=('Arial', 15, 'bold')).pack(pady=8)
        today = datetime.date.today()

        self.assignment_duedate = Calendar(self, background='#426aa1', year=today.year, month=today.month,
                                           day=today.day)
        self.assignment_duedate.pack(pady=2)

        self.assignment_duetime_hour = ctk.CTkOptionMenu(self, width=60, values=['1', '2', '3', '4', '5', '6', '7', '8',
                                                                                 '9', '10', '11', '12'], anchor=tk.CENTER)
        self.assignment_duetime_hour.place(x=100, y=420)

        self.assignment_duetime_minute = ctk.CTkOptionMenu(self, width=60, values=['00', '15', '30', '45', '59'], anchor=tk.CENTER)
        self.assignment_duetime_minute.place(x=170, y=420)

        self.assignment_duetime_convention = ctk.CTkOptionMenu(self, width=60, values=['AM', 'PM'], anchor=tk.CENTER)
        self.assignment_duetime_convention.place(x=240, y=420)

        self.assn_platform_hdr = ctk.CTkLabel(self, width=100, text="Assignment Platform",
                                              font=('Arial', 15, 'bold')).place(x=125, y=465)
        self.assignment_platform = ctk.CTkEntry(self, width=150, placeholder_text="Assignment Platform")
        self.assignment_platform.place(x=125, y=505)

        self.confirm_assignment = ctk.CTkButton(self, width=100, height=30, text="Create Assignment", command=self.create_assignment)
        self.confirm_assignment.place(x=135, y=560)

    def create_assignment(self):  # Function to create a new assignment
        assignmentName = self.assignment_name.get()
        assignmentClass = self.assignment_class.get()
        assignmentDueDate = self.assignment_duedate.get_date()
        assignmentDueTime = f"{self.assignment_duetime_hour.get()}:{self.assignment_duetime_minute.get()}{self.assignment_duetime_convention.get()}"
        assignmentPlatform = self.assignment_platform.get()
        assignmentStatus = "To Do"
        if len(assignmentClass) < 2 or len(assignmentName) < 2:
            tk.messagebox.showinfo("Missing Values", "One or more entries are empty.", icon='warning')
        else:
            ret_asn = (f"{assignmentName}", f"{assignmentClass[-1]}", f"{assignmentDueDate}", f"{assignmentDueTime}",
                       f"{assignmentPlatform}", f"{assignmentStatus}")
            dict1 = {'name': ret_asn[0], 'class': ret_asn[1], 'duedate': ret_asn[2], 'duetime': ret_asn[3],
                     "platform": ret_asn[4],
                     'status': ret_asn[5]}
            try:
                with open("user_assn.json", "r") as file:
                    dicts = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                dicts = []

            found = False
            for i, d in enumerate(dicts):
                if d.get('name') == dict1.get('name'):
                    found = True
                    if d != dict1:
                        dicts[i] = dict1
                        with open("user_assn.json", "w") as file:
                            json.dump(dicts, file, indent=4)
                    break
            if not found:
                dicts.append(dict1)
                with open("user_assn.json", "w") as file:
                    json.dump(dicts, file, indent=4)

            import_assignments(assn_page_frame)
            self.reset()
            self.destroy()

    def reset(self):  # Resets the additional window
        self.assignment_name.delete(0, tk.END)
        self.assignment_class.set('-')
        self.assignment_duetime_convention.set('PM')
        self.assignment_platform.delete(0, tk.END)


class Assignment:  # Class that creates individual assignment objects
    def __init__(self, parent, assignmentName="", assignmentClass="", assignmentDueDate="", assignmentDueTime="",
                 assignmentPlatform="", assignmentStatus="To Do"):
        self.parent = parent
        self.assignmentName = assignmentName
        self.assignmentClass = assignmentClass
        self.assignmentDueDate = assignmentDueDate
        self.assignmentDueTime = assignmentDueTime
        self.assignmentStatus = assignmentStatus
        self.assignmentPlatform = assignmentPlatform

        self.frame = ctk.CTkFrame(self.parent, width=1450, height=40)
        self.frame.propagate(False)
        self.frame.pack(anchor='nw', padx=5, pady=5)

        self.assignmentNameLabel = ctk.CTkLabel(self.frame, text=f'{self.assignmentName}', width=120, height=30)
        self.assignmentNameLabel.pack(side=tk.LEFT, padx=15)

        self.assignmentClassLabel = ctk.CTkLabel(self.frame, text=f'{self.assignmentClass}', width=120, height=30)
        self.assignmentClassLabel.pack(side=tk.LEFT, padx=20)

        self.assignmentDueDateLabel = ctk.CTkLabel(self.frame,
                                                   text=f'{self.assignmentDueDate} at {self.assignmentDueTime}',
                                                   width=120, height=30)
        self.assignmentDueDateLabel.pack(side=tk.LEFT, padx=5)

        self.assignmentPlatformLabel = ctk.CTkLabel(self.frame, text=f'{self.assignmentPlatform}', width=120, height=30)
        self.assignmentPlatformLabel.pack(side=tk.LEFT, padx=3)

        self.assignmentStatusLabel = ctk.CTkOptionMenu(self.frame, width=80, height=25,
                                                       values=['To Do', 'Doing', 'Done'], anchor=tk.CENTER,
                                                       command=lambda value, instname=assignmentName: self.update_status(value,
                                                                                                                  instname))
        self.assignmentStatusLabel.set(f'{self.assignmentStatus}')
        self.assignmentStatusLabel.pack(side=tk.LEFT, padx=35)

    @staticmethod
    def update_status(new_status, assn_name):  # Function to update the status of individual assignments
        with open('user_assn.json', 'r') as file:
            assignments = json.load(file)

        for item in assignments:
            if item['name'] == assn_name:
                if new_status == 'Done':
                    assignments.remove(item)
                    break
                else:
                    item['status'] = new_status

        with open('user_assn.json', "w") as file:
            json.dump(assignments, file, indent=4)

        import_assignments(assn_page_frame)


def import_assignments(page):  # Function to import assignments from the JSON file
    AssignmentsPage.update_assignment_list()
    try:
        with open("user_assn.json", "r") as file:
            assignments = json.load(file)
            for assn in assignments:
                assignment = Assignment(page.childrenFrame, f"{assn['name']}", f"{assn['class']}",
                                        f"{assn['duedate']}", f"{assn['duetime']}", f"{assn['platform']}",
                                        f"{assn['status']}")
                assignment.assignmentStatusLabel.set(assn['status'])
                assignments_made.append(assignment.frame)

    except json.decoder.JSONDecodeError:
        pass
