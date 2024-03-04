## NOTES:

## Currently, it seems that the command to disable icons through the terminal
## also disables the Desktop right-click or control-click function. Not sure if there
## is a way to bring this back with another terminal command. The function comes back
## when re-enabled. The other note to make is that the text labels can appear on top
## of each other if Disabled/Enabled is activated in rapid succession because of the .after().
## This isn't much more than an aesthetic issue at times, but could be adjusted in the future.


## Core library imports:
import tkinter
from tkinter import *
import customtkinter
import os


## Setting application theme to system default of light or dark and color theme to blue:
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


## Class of entire application:
class App(customtkinter.CTk):
    

    ## Dimensions of application window:
    WIDTH = 300
    HEIGHT = 100
    

    ## Application start:
    def __init__(self):
        super().__init__()


        ## Title of application header:
        self.title("macOS Icon Hider")
        ## Set application dimensions into action:
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        ## Allowed minimum size of application window:
        self.minsize(300, 100)
        ## Allowed maximum size of application window:
        self.maxsize(300, 100)


        ## Labels of text linked to button commands:
        ## Disable button label:
        def string_disable():
            textD = Label(self,
                            ## Text label customization:
                            text="Begone messy desktop!",  
                            font="OpenSans-Bold 16", 
                            padx=3,)
            ## Place text label and remove the label after 5 seconds:
            textD.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
            textD.after(5000, textD.destroy)


        ## Enable button label:
        def string_enable():
            textE = Label(self,
                            ## Text label customization:
                            text="Welcome back messy desktop!",  
                            font="OpenSans-Bold 16", 
                            padx=3,)
            ## Place text label and remove the label after 5 seconds:
            textE.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
            textE.after(5000, textE.destroy)
            

        ## Disable button program below this line:
        def button_event_off():
            ## Hides destop icons and restarts Finder:
            os.system("defaults write com.apple.finder CreateDesktop false; killall Finder")
            ## Exits terminal:
            os.system("exit")

        button_one = customtkinter.CTkButton(master=self,
                            ## Button customization:
                            width=120,
                            height=32,
                            border_width=0,
                            corner_radius=8,
                            text="Disable Icons",
                            fg_color="red",
                            text_color="white",
                            hover_color="#a80000",
                            ## Button executes both Enabled event functions:
                            command=lambda:[button_event_off(), string_disable()])
        button_one.place(relx=0.25, rely=0.7, anchor=tkinter.CENTER)


        ## Enable button program below this line:
        def button_event_on():
            ## Hides destop icons and restarts Finder:
            os.system("defaults write com.apple.finder CreateDesktop true; killall Finder")
            ## Exits terminal:
            os.system("exit")

        button_two = customtkinter.CTkButton(master=self,
                            ## Button customization:
                            width=120,
                            height=32,
                            border_width=0,
                            corner_radius=8,
                            text="Enable Icons",
                            text_color="white",
                            ## Button executes both Enabled event functions:
                            command=lambda:[button_event_on(), string_enable()])
        button_two.place(relx=0.75, rely=0.7, anchor=tkinter.CENTER)
   

## Application end/loop:
if __name__ == "__main__":
    app = App()
    app.mainloop()