import ast
import tkinter as tk
from tkinter import *
import requests
from bs4 import BeautifulSoup
from PIL import ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting up Initial Things
        self.title("Neon White Leaderboard Tracker")
        self.geometry("720x550")
        self.resizable(True, True)
        self.iconphoto(False, tk.PhotoImage(file="assets/Neon-White.png"))


        canvas = Canvas(width=600, height=800, bg='blue')
        canvas.pack(expand=YES, fill=BOTH)

        image = ImageTk.PhotoImage(file="File route")
        canvas.create_image(10, 10, image=image, anchor=NW)

        # Creating a container
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize Frames
        self.frames = {}
        self.EnterTimes = EnterTimes
        self.Leaderboard = Leaderboard

        # Can use for more functionality later
        # self.TimeEditor = TimeEditor

        # Defining Frames and Packing it
        for F in {EnterTimes, Leaderboard}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(EnterTimes)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise()  ## This line will put the frame on front


# ---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class EnterTimes(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Enter Times", font=('Times', '20'))
        label.grid(row=0, column=0, pady=10, padx=0)

        ## ADD CODE HERE TO DESIGN THIS PAGE

        username_label = Label(self, text="Name", font=('Times', '20'))
        substage_label = Label(self, text="Substage", font=('Times', '20'))
        time_label = Label(self, text="Time", font=('Times', '20'))

        self.user = StringVar(self)
        self.user.set("Adam")
        self.w = OptionMenu(self,self.user, "Adam", "Austin")

        # self.username_entry = Entry(self, width=20, relief="solid")
        self.substage_entry = Entry(self, width=20, relief="solid")
        self.time_entry = Entry(self, width=20, relief="solid")

        submit_button = Button(self, text="Submit", font=('Times', '20'), command=lambda: self.submit(parent))

        username_label.grid(row=1, column=0, pady=0, padx=0)
        substage_label.grid(row=2, column=0, pady=0, padx=0)
        time_label.grid(row=3, column=0, pady=0, padx=0)

        self.w.grid(row=1, column=1, pady=0, padx=0)

        # self.username_entry.grid(row=1, column=1, pady=0, padx=0)
        self.substage_entry.grid(row=2, column=1, pady=0, padx=0)
        self.time_entry.grid(row=3, column=1, pady=0, padx=0)

        submit_button.grid(row=4, column=0, pady=0, padx=0)

    def submit(self, parent):
        url = "http://ifyx.xyz/"

        username = self.user.get()
        substage = self.substage_entry.get()
        time = self.time_entry.get()

        self.substage_entry.delete(0, END)
        self.time_entry.delete(0, END)

        if username == "Adam":
            username = "1"
            print("changed to 1")
        elif username == "Austin":
            username = "2"

        with requests.Session() as s:

            data = s.get(url)
            soup = BeautifulSoup(data.text, "html.parser")
            form = soup.find("form")
            token_value = form.find_all("input")[0]["value"]

            payload = {"csrf_token": token_value,
                       "name": username,
                       "substage": str(substage),
                       "time": str(time)
                       }

            result = s.post("http://ifyx.xyz/", data=payload)

            print(result.status_code)

        if result.status_code == 200:
            parent.show_frame(parent.Leaderboard)
        else:
            error_label = Label(self, text="error, try again", font=('Times', '20'))
            error_label.grid(row=3, column=3)

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Enter Times", command=lambda: parent.show_frame(parent.EnterTimes))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)

        # Leaderboard menu
        leaderboard_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Leaderboard", menu=leaderboard_menu)
        leaderboard_menu.add_command(label="View Times", command=lambda: parent.show_frame(parent.Leaderboard))

        # Can use for more functionality later
        # leaderboard_menu.add_command(label="Enter Times", command=lambda: parent.show_frame(parent.TimeEditor))
        leaderboard_menu.add_separator()

        # help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")
        help_menu.add_separator()

        return menubar

    # ---------------------------------------- Validation PAGE FRAME / CONTAINER ------------------------------------------------------------------------


class Leaderboard(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        header_frame = Frame(self, container, bg="white")
        header_frame.pack()

        myscrollbar = Scrollbar(self, orient="vertical")
        myscrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)

        label = tk.Label(self, text="Leaderboard", font=('Times', '20'))
        label.pack(pady=0, padx=0)

        # ADD CODE HERE TO DESIGN THIS PAGE
        time_frame = Frame(self, container, bg="white")
        time_frame.pack()

        refresh_button = Button(header_frame, text="Refresh", command=lambda: self.refresh(time_frame, container))
        refresh_button.pack(pady=0, padx=0)

        self.populate_board(time_frame, container)

    def populate_board(self, time_frame, container):

        try:
            response = requests.get(url="http://127.0.0.1:5000/data")
            byte_str = response.content
            dict_str = byte_str.decode("UTF-8")
            mydata = ast.literal_eval(dict_str)
        except:
            mydata = None

        if mydata is not None:
            substage_col_number = 1

            for i in mydata["stages"]:
                stage_frame = Frame(time_frame, container, bg="white", pady=5, )
                stage_frame.pack(anchor="w")

                stage_name = tk.Label(stage_frame, text=i['name'], font=('Times', '12', 'bold'), bg="white", width=20)
                stage_name.grid(row=0, column=0, sticky="nw")

                # needs to be a function to add all users to the table
                user_row = 1
                for user in i["users"]:
                    user_label = tk.Label(stage_frame, text=user["name"], bg="white", font=('Times', '10'))
                    user_label.grid(row=user_row, column=0, sticky="nw", padx=20)

                    user_row += 1
                for substage in i['substages']:
                    if substage != "":
                        substage_name = tk.Label(stage_frame, text=substage, bg="white", font=('Times', '10'), width=15)
                        substage_name.grid(row=0, column=substage_col_number, sticky="w")

                        # add function to add all user times for current substage

                        user_row = 1
                        for user in i["users"]:
                            try:
                                user_time = user["times"][substage_col_number - 1][0]
                                if user_time == "":
                                    user_time = "00:00"
                            except:
                                user_time = "00:00"

                            user_label = tk.Label(stage_frame, text=user_time, bg="white", font=('Times', '10'))
                            user_label.grid(row=user_row, column=substage_col_number, sticky="nw", padx=20)

                            user_row += 1

                        # test_time_label1 = tk.Label(stage_frame, text="00:00:00", bg="white", font=('Times', '10'))
                        # test_time_label1.grid(row=2, column=substage_col_number)

                        substage_col_number += 1
                substage_col_number = 1

    def refresh(self, frame, container):

        for widget in frame.winfo_children():
            widget.destroy()

        response = requests.get(url="http://127.0.0.1:5000/data")

        byte_str = response.content
        dict_str = byte_str.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print(repr(mydata))
        self.populate_board(frame, container)

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Choose User", command=lambda: parent.show_frame(parent.EnterTimes))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)

        # Leaderboard menu
        leaderboard_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Leaderboard", menu=leaderboard_menu)
        leaderboard_menu.add_command(label="View Times", command=lambda: parent.show_frame(parent.Leaderboard))

        # Can use for more functionality later
        # leaderboard_menu.add_command(label="Enter Times", command=lambda: parent.show_frame(parent.TimeEditor))
        leaderboard_menu.add_separator()

        # help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")
        help_menu.add_separator()

        return menubar

    # ---------------------------------------- TimeEditor PAGE FRAME / CONTAINER --------------------------------------


# class TimeEditor(tk.Frame):
#     def __init__(self, parent, container):
#         super().__init__(container)
#
#         label = tk.Label(self, text="Add a time", font=('Times', '16'))
#         label.pack(pady=0, padx=0)
#
#         ## ADD CODE HERE TO DESIGN THIS PAGE
#
#     def create_menubar(self, parent):
#         menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")
#
#         ## Filemenu
#         filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
#         menubar.add_cascade(label="File", menu=filemenu)
#         filemenu.add_command(label="Choose User", command=lambda: parent.show_frame(parent.EnterTimes))
#         filemenu.add_separator()
#         filemenu.add_command(label="Exit", command=parent.quit)
#
#         ## Leaderboard menu
#         leaderboard_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Leaderboard", menu=leaderboard_menu)
#         leaderboard_menu.add_command(label="View Times", command=lambda: parent.show_frame(parent.Leaderboard))
#         leaderboard_menu.add_command(label="Enter Times", command=lambda: parent.show_frame(parent.TimeEditor))
#         leaderboard_menu.add_separator()
#
#         ## help menu
#         help_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Help", menu=help_menu)
#         help_menu.add_command(label="About")
#         help_menu.add_separator()
#
#         return menubar


if __name__ == "__main__":
    app = App()
    app.mainloop()
