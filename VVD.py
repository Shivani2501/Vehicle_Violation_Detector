import tkinter as tk
from tkinter import *
from PIL import ImageTk
import vlc
import tkinter.messagebox as messagebox
#import pymysql
import os
import smtplib as s
from tkinter import filedialog
import easygui


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, Analysis_MessagePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Vehicle Violation Detector')
        self.controller.state('zoomed')
        # self.controller.iconphoto(False, tk.PhotoImage(file='health-report.png'))
        self.image_frame = ImageTk.PhotoImage(file="purple_texture.jpg")
        self.img = Label(self, image=self.image_frame)
        self.img.place(x=0, y=0, width=1600, height=800)

        heading1 = Label(
            self,
            text=" Vehicle Violation Detector ",
            bg="#1e0033",
            fg="#dfb3ff",
            relief=RAISED,
            borderwidth=4,
            font=('Times', 45)
        )
        heading1.place(x=430, y=80, height=100)

        main_frame = Label(
            self,
            bd=2,
            bg='#1e0033', relief=RAISED, borderwidth=4,
            padx=100,
            pady=100
        )
        main_frame.place(x=450, y=250, width=640, height=380)

        owner = Label(
            self,
            text="Username:",
            bg="#1e0033", fg="#dfb3ff",
            font=("Times", 20)
        )
        owner.place(x=600, y=320, width=120)

        password = Label(
            self,
            text="Password:",
            bg="#1e0033", fg="#dfb3ff",
            font=("Times", 20)
        )
        password.place(x=600, y=420, width=120)

        my_username = tk.StringVar()
        register_owner = Entry(
            self,
            bg="#CCCCCC",
            textvariable=my_username,
            font=("Times", 18)
        )
        register_owner.place(x=740, y=320, width=200)

        my_password = tk.StringVar()
        register_password = Entry(
            self,
            bg="#CCCCCC",
            textvariable=my_password,
            show="*",
            font=("Times", 18)
        )
        register_password.place(x=740, y=420, width=200)

        def check_password():
            if my_username.get() == 'admin123' and my_password.get() == '12345':
                my_username.set('')
                my_password.set('')
                invalid_password['text'] = ""
                controller.show_frame('Analysis_MessagePage')
            else:
                messagebox.showwarning("Error", "Enter Valid Id and Password", parent=self.controller)

        Login_btn = Button(
            self,
            width=12,
            font=("Times", 16),
            cursor="hand2",
            bg='#a6a6a6', fg='#1e0033', borderwidth=3,
            text='Login',
            command=check_password
        )
        Login_btn.place(x=610, y=510)

        exit_btn = Button(
            self,
            width=12,
            text='Exit',
            font=("Times", 16),
            cursor='hand2',
            bg='#a6a6a6', fg='#1e0033', borderwidth=3,
            command=self.quit
        )
        exit_btn.place(x=790, y=510)

        invalid_password = Label(
            self,
            text="",
            bg="#1e0033",
            fg="orange",
            font=("Times", 18)
        )
        invalid_password.place(x=610, y=565, width=338)


class Analysis_MessagePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        self.image_frame = ImageTk.PhotoImage(file="purple_texture.jpg")
        self.img = Label(self, image=self.image_frame)
        self.img.place(x=0, y=0, width=1600, height=800)

        def Home_p():
            controller.show_frame('HomePage')

        heading2 = Label(
            self,
            text=" Analysis ",
            bg="#1e0033",
            fg="#dfb3ff",
            relief=RAISED,
            font=("Times", 35)
        )
        heading2.place(x=330, y=50, height=60)

        heading3 = Label(
            self,
            text=" Message ",
            bg="#1e0033",
            fg="#dfb3ff",
            relief=RAISED,
            font=("Times", 35)
        )
        heading3.place(x=900, y=50, height=60)

        # frame
        frame0 = Frame(self, bg='#1e0033', relief=RAISED, borderwidth=4)
        frame0.place(x=240, y=150, width=350, height=500)

        def analyze_video():
            global player
            while True:
                choice = easygui.buttonbox(title="Video_Analysis",
                                           msg="Play - To play a Video          "
                                               "Pause - To pause a Video\n"
                                               "Resume - To resume a video      "
                                               "Stop - To Stop a Video\n"
                                               "Note - To Note Car No",
                                           choices=["Play", "Pause", "Resume", "Stop", "Note"])

                print(choice)
                if choice == "Play":
                    media = easygui.fileopenbox(title="Choose media to open")
                    player = vlc.MediaPlayer(media)
                    player.play()
                elif choice == "Pause":
                    player.pause()
                elif choice == "Stop":
                    player.stop()
                elif choice == "Resume":
                    player.play()
                elif choice == "Note":
                    entry = easygui.enterbox(title="Note", msg="Enter Car No")
                    print(entry)
                else:
                    break

        title0 = Label(frame0, text="Analyze\nVideo", font=("times new roman", 40, "bold"), bg="#1e0033",
                       fg="#dfb3ff").place(
            x=80, y=30)

        btn_analyze = Button(frame0, text="\nAnalyze\n", font=("times new roman", 30, "bold"), cursor="hand2",
                             bg='#a6a6a6', fg='#1e0033', borderwidth=6, command=analyze_video,
                             ).place(x=80, y=250, width=200)

        frame1 = Frame(self, bg='#1e0033', relief=RAISED, borderwidth=4)
        frame1.place(x=640, y=150, width=700, height=500)

        title = Label(frame1, text="* Search Here:", font=("times new roman", 20, "bold"), bg="#1e0033",
                      fg="#dfb3ff").place(
            x=50, y=30)
        # ------------
        # self.var_owner=StringVar()
        owner = Label(frame1, text="Owner Name", font=("times new roman", 15, "bold"), bg="#1e0033",
                      fg="#dfb3ff").place(
            x=50, y=100)
        self.txt_owner = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_owner.place(x=50, y=135, width=250, height=32)

        carId = Label(frame1, text="Car No.", font=("times new roman", 15, "bold"), bg="#1e0033", fg="#dfb3ff").place(
            x=370,
            y=100)
        self.txt_carId = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_carId.place(x=370, y=135, width=250, height=32)

        email = Label(frame1, text="Email Id", font=("times new roman", 15, "bold"), bg="#1e0033", fg="#dfb3ff").place(
            x=50,
            y=200)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_email.place(x=50, y=235, width=250, height=32)

        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="#1e0033",
                        fg="#dfb3ff").place(
            x=370, y=200)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_contact.place(x=370, y=235, width=250, height=32)

        # ------------
        btn_search = Button(frame1, text="Search", font=("times new roman", 16, "bold"), cursor="hand2",
                            bg='#a6a6a6', fg='#1e0033', borderwidth=3,  command=self.fetch,
                            ).place(x=50, y=300, width=250, height=50)
        btn_send = Button(frame1, text="Send Message", font=("times new roman", 16, "bold"), cursor="hand2",
                          bg='#a6a6a6', fg='#1e0033', borderwidth=3, command=self.sendmessage).place(x=375, y=300, width=250, height=50)
        btn_back = Button(frame1, text="Back", font=("times new roman", 16, "bold"), cursor="hand2",
                          bg='#a6a6a6', fg='#1e0033', borderwidth=3, command=Home_p
                          ).place(x=50, y=380, width=250, height=50)
        btn_exit = Button(frame1, text="Exit", font=("times new roman", 16, "bold"),
                          bg='#a6a6a6', fg='#1e0033', borderwidth=3, command=self.quit,
                          cursor="hand2").place(x=375, y=380, width=250, height=50)

        # -------------
        #   Database code

    def clear(self):
        self.txt_owner.delete(0, END)
        self.txt_carId.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_contact.delete(0, END)

    
     def submit(self):
         if self.txt_owner.get() == "" or self.txt_carId.get() == "" or self.txt_email.get() == "" or self.txt_contact.get() == "":
             messagebox.showerror("Error", "All Field are Required", parent=self.controller)
    
         else:
             try:
                 con = pymysql.connect(host="localhost", user="root", passwd="", database="python_project")
                 c = con.cursor()
                 c.execute("select * from myproject where idl=%s", self.txt_carId.get())
                 row = c.fetchall()
                 print(row)
                 c.execute("insert into myproject (owner, idl, email_id, phone) values(%s,%s,%s,%s)",
                           (
                               self.txt_owner.get(),
                               self.txt_carId.get(),
                               self.txt_email.get(),
                               self.txt_contact.get()
                           )
                           )
                 con.commit()
                 con.close()
                 messagebox.showinfo("Success", "Sucessfully Saved!", parent=self.controller)
                 self.clear()
             except Exception as es:
                 messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.controller)
                 print(self.txt_owner.get(),
                       self.txt_carId.get(),
                       self.txt_email.get(),
                       self.txt_contact.get()
                       )

    def fetch(self):
        if self.txt_carId.get() == "":  #connect database
            messagebox.showwarning("Warning", "Please Enter Car id", parent=self.controller)
        else:
            con = pymysql.connect(host="localhost", user="root", passwd=" ", database="python_project")
            c = con.cursor()
            c.execute("select * from myproject where idl=%s", self.txt_carId.get())
            row = c.fetchall()

            for rows in row:
                self.txt_owner.insert(0, rows[1])
                # self.txt_carId.insert(0, rows[2])
                self.txt_email.insert(0, rows[3])
                self.txt_contact.insert(0, rows[4])
            con.close()

    def sendmessage(self):
        if self.txt_email.get() == "": #connect database
            messagebox.showwarning("Warning", "Please enter your email", parent=self.controller)
        else:
            ob = s.SMTP("smtp.gmail.com", 587)
            ob.starttls()
            ob.login("example@gmail.com", " ")
            subject = "Sending Email using python"
            body = "This is project mail"
            message = "Subject:{}\n\n{}".format(subject, body)
            ob.sendmail("example", self.txt_email.get(), message)
            messagebox.showinfo("Success", "Sucessfully send!", parent=self.controller)
            ob.quit()
            self.clear()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
