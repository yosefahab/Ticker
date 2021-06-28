import tkinter


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

        self.start = tkinter.Button(self.mainframe,
                                    text='Start',
                                    width=8,
                                    bg="#2f3745",
                                    fg='white',
                                    activebackground='#313b47',
                                    activeforeground='white',
                                    font=18,
                                    borderwidth=0.01,
                                    command=self.Start)
        self.reset = tkinter.Button(self.mainframe,
                                    text='Reset',
                                    width=8,
                                    bg="#2f3745",
                                    fg='white',
                                    activebackground='#313b47',
                                    activeforeground='white',
                                    font=18,
                                    borderwidth=0.01,
                                    state='disabled',
                                    command=self.Reset)
        self.start.grid(row=3, column=1)
        self.reset.grid(row=3, column=3)

        self.num = tkinter.Label(self.mainframe,
                                 textvariable=self.counter,
                                 font=18,
                                 bd=1,
                                 width=10,
                                 bg="#2f3745",
                                 fg='white',
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

    def Break(self):
        self.window.withdraw()
        breakWin = tkinter.Toplevel(self.window)
        breakWin.iconbitmap("clock.ico")
        breakWin.title("Break Time")
        breakWin.geometry("600x220")
        breakWin.attributes('-alpha', 0.95)
        breakWin.resizable(False, False)
        breakWin.attributes('-fullscreen', 1)

        fm = tkinter.Frame(breakWin, bg="gray13")
        fm.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        brTxt = tkinter.Label(fm, text="Time for a break", font=(
            "Arial", 25), fg="white", bg="gray13")
        brTxt.pack(side=tkinter.TOP, expand=tkinter.YES)

        exitBtn = tkinter.Button(fm, width=10, text='Exit now', borderwidth=0.01, font=('Arial 12 underline'),
                                 command=breakWin.destroy, activebackground='gray13',
                                 activeforeground='white', bg="gray13", fg='white', relief=tkinter.FLAT)
        exitBtn.pack(side=tkinter.TOP, expand=tkinter.YES)
        exitBtn.bind("<Destroy>", lambda x: self.window.deiconify())


def main():
    window = tkinter.Tk()
    app = counter(window)
    window.mainloop()


if __name__ == '__main__':
    main()
