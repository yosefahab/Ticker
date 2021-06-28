import tkinter
from tkinter import ttk


class counter:
    def __init__(self, window):
        self.defSecs = 1199  # 19:59
        self.totalSecs = self.defSecs
        self.counter = tkinter.StringVar()
        self.counter.set("20:00")
        self.running = False

        self.window = window
        self.window.iconbitmap("clock.ico")
        self.window.title("Ticker")
        self.window.attributes('-alpha', 0.85)
        self.window.geometry("300x110")
        self.window.eval('tk::PlaceWindow . center')
        self.window.resizable(False, False)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.configure(bg='#2f3745')

        self.mainframe = tkinter.Frame(
            self.window, background='#2f3745', height=300, width=110)
        self.mainframe.grid(row=0, column=0)

        self.start = tkinter.Button(self.mainframe, text='Start',
                                    width=8, borderwidth=0.01,
                                    font=18,
                                    bg="#2f3745", fg='white',
                                    activebackground='#313b47', activeforeground='white',
                                    command=self.Start)
        self.reset = tkinter.Button(self.mainframe,
                                    text='Reset',
                                    width=8, borderwidth=0.01,
                                    font=18,
                                    bg="#2f3745", fg='white',
                                    activebackground='#313b47', activeforeground='white',
                                    state='disabled',
                                    command=self.Reset)
        self.start.grid(row=3, column=1)
        self.reset.grid(row=3, column=3)

        self.num = tkinter.Label(self.mainframe,
                                 textvariable=self.counter,
                                 font=18,
                                 bd=1, width=10,
                                 bg="#2f3745", fg='white',
                                 pady=6)
        self.num.grid(row=0, column=2)

    def countdown(self):
        if self.totalSecs > 0 and self.running == True:
            minutes = int((self.totalSecs/60) % 60)
            seconds = int((self.totalSecs) % 60)
            self.totalSecs -= 1
            self.counter.set(f"{minutes:02}:{seconds:02}")
            self.window.after(1000, lambda: self.countdown())
        else:
            if self.totalSecs <= 0:
                self.Break()
            self.Reset()

    def Start(self):
        self.running = True
        self.start['state'] = 'disabled'
        self.reset['state'] = 'normal'
        self.countdown()

    def Reset(self):
        self.running = False
        self.counter.set("20:00")
        self.totalSecs = self.defSecs
        self.start['state'] = 'normal'
        self.reset['state'] = 'disabled'

    def updateProg(self):
        self.pBar['value'] += 1
        if self.pBar['value'] < self.pBar['maximum']:
            self.breakWin.after(1000, self.updateProg)
        else:
            self.breakWin.destroy()

    def Break(self):
        self.window.withdraw()
        self.breakWin = tkinter.Toplevel(self.window)
        self.breakWin.iconbitmap("clock.ico")
        self.breakWin.title("Break Time")
        self.breakWin.attributes('-alpha', 0.95)
        self.breakWin.resizable(False, False)
        self.breakWin.attributes('-fullscreen', 1)
        self.breakWin.grab_set()
        fm = tkinter.Frame(self.breakWin, bg="gray13")
        fm.pack(fill=tkinter.BOTH, expand=1)

        brTxt = tkinter.Label(fm, text="Time for a break", font=(
            "Arial", 25), fg="white", bg="gray13")
        brTxt.pack(side=tkinter.TOP, expand=1)

        txt = tkinter.Label(fm, text="for 20 seconds, look at something 20 feet away", font=(
            "Arial", 20), fg="#706F6C", bg="gray13")
        txt.pack(side=tkinter.TOP, expand=1)

        s = ttk.Style()
        s.theme_use("clam")
        s.configure("Horizontal.TProgressbar",
                    thickness=5,
                    troughcolor='gray16',
                    bordercolor='gray16',
                    lightcolor='#526882',
                    darkcolor='#526882',
                    foreground='#526882',
                    background='#526882')
        self.pBar = ttk.Progressbar(fm, orient=tkinter.HORIZONTAL, style="Horizontal.TProgressbar",
                                    mode='determinate', maximum=30,
                                    length=300, value=-1)
        self.pBar.pack(side=tkinter.TOP, expand=1)

        exitBtn = tkinter.Button(fm, width=10, text='Exit now', borderwidth=0.01, font=('Arial 12 underline'),
                                 command=self.breakWin.destroy, activebackground='gray13',
                                 activeforeground='white', bg="gray13", fg='white', relief=tkinter.FLAT)
        exitBtn.pack(side=tkinter.TOP, expand=1)
        exitBtn.bind("<Destroy>", lambda x: self.window.deiconify())
        self.updateProg()


def main():
    window = tkinter.Tk()
    app = counter(window)
    window.mainloop()


if __name__ == '__main__':
    main()
