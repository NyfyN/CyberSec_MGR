from settings import *

import customtkinter as ctk
import tkinter as tk
import subprocess


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

### INIT APPLICATION ###
        # Set defaults values of application
        self.title("CyberSec APP")  # CHANGE IT WHEN IT DONE
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)
        self.mainwindow()
        # Set icons and icon folder

### MAIN WINDOW AND PARAMETERS ###
    def mainwindow(self) -> None:
        # grid layout 4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # add sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self, width=WIDTH//10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nswe")

        # add checkbox frame
        self.checkbox_frame = ctk.CTkFrame(self, width=WIDTH//20)
        self.checkbox_frame.grid(row=0, column=5, rowspan=2, sticky="ne")

        # right checkboxes
        self.checkbox = ctk.CTkCheckBox(
            self.checkbox_frame, text="Placehoder", command=self.test_checkbox)
        self.checkbox.grid(row=0, column=1, padx=10, pady=(20, 10), sticky="e")

        # add main frame with system task list
        self.main_frame = ctk.CTkFrame(self, width=WIDTH, height=HEIGHT)
        self.main_frame.grid(row=0, column=2, sticky="w")

        # main label with tasks
        self.tasks_label = ctk.CTkLabel(
            self.main_frame, width=WIDTH, height=HEIGHT, text=self.tasklist("brave.exe"))
        self.tasks_label.grid(row=0, column=0, sticky="w")

        # add sidebar
        self.sidebar_logo_name = ctk.CTkLabel(
            self.sidebar_frame,
            text="CYBERSEC",
            font=ctk.CTkFont(size=32, weight="bold")
        )

        self.sidebar_logo_name.grid(
            row=0, column=0, padx=10, pady=(20, 10), sticky="nswe")

        # ADD SIDEBAR TABS

        # home tab
        self.home_tab = ctk.CTkButton(
            self.sidebar_frame,
            corner_radius=0,
            height=80,
            border_spacing=10,
            text="Home",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            bg_color=("gray70", "gray30"),
            # image=image, ----> Add it when icons are added
            anchor="w",
            font=ctk.CTkFont(size=20),
            # command=self.home_button_event ----> Add it when func "select_frames" is finished
        )
        self.home_tab.grid(row=1, column=0, sticky="ew")

        # TODO: Add more buttons and thinking about events on it

    # Buttons section

    # TODO: add button tabs

### APPLICATION METHODS ###

    def select_frame(self, frame_name: str) -> None:
        pass

    def test_checkbox(self) -> int:
        print(self.checkbox.get())

    def tasklist(self, process: str) -> str:
        parameter = f'/FI "ImageName eq {process}"'
        sub = subprocess.Popen(
            f'tasklist {parameter}', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = sub.communicate()
        result = stdout.decode('utf-8', 'ignore')
        # err = stderr.decode('utf-8', 'ignore') ----> Use it for error messages
        return result

### SYSTEM PREFERENCES METHODS ###

    def change_appearance(self, mode: str) -> None:
        ctk.change_appearance_mode(mode)

    def change_UI_scaling(self, percentage: str) -> None:
        scaling_size = int(percentage.replace("%", ""))//100
        ctk.set_window_scaling(scaling_size)

    def run(self) -> None:
        self.mainloop()


def main() -> None:
    app = App()
    app.run()


if __name__ == "__main__":
    main()
