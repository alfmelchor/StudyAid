import customtkinter as ctk

root = ctk.CTk()
ctk.set_default_color_theme('/Users/alfonsomelchor/Desktop/Code Files/StudyAid/source/themes/green.json')

switch = ctk.CTkSwitch(root)
switch.pack()

root.mainloop()