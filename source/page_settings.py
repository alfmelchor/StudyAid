import customtkinter as ctk
import tkinter as tk


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
                                               text="Interaction", hover_color='#1C9670', width=100, height=25,
                                               anchor="n", state='normal',
                                               command=lambda: self.open_settings('Interaction'))
        self.interactionButton.pack(side=tk.LEFT, padx=5)
        self.studyAidButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                            text="Study Aid", hover_color='#1C9670', width=100, height=25,
                                            anchor="n", state='normal',
                                            command=lambda: self.open_settings('StudyAid'))
        self.studyAidButton.pack(side=tk.LEFT, padx=5)
        self.changesButton = ctk.CTkButton(self.options_frame, text_color='white', fg_color="#4e5966",
                                           text="Change Log", hover_color='#1C9670', width=100, height=25,
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

        self.text = tk.Text(self.frame, width=950, height=550, bg='#DBDBDB', fg='black')
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
