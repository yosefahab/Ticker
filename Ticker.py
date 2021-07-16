import tkinter as tk
from tkinter import ttk

class counter:
    def __init__(self, window):
        self.defSecs = 1199
        self.totalSecs = self.defSecs
        self.counter = tk.StringVar()
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

        self.mainframe = tk.Frame(
            self.window, background='#2f3745', height=300, width=110)
        self.mainframe.grid(row=0, column=0)
        self.mainframe.bind("<Button-3>", self.do_popup)

        self.radio = tk.IntVar()
        self.menu = tk.Menu(self.mainframe,
                            bg="#2f3745", fg='white',
                            bd=5, relief="flat",
                            activebackground='#313b47', activeforeground='white',
                            tearoff=0)
        self.timeMenu = tk.Menu(self.menu, tearoff=0, bg="#2f3745", fg='white',
                                bd=0, relief="flat",
                                activebackground='#313b47', activeforeground='white', selectcolor='white')
        for i in range(6):
            self.timeMenu.add_radiobutton(label=f"{i*5+20} minutes", 
            selectcolor='white',variable= self.radio,value=i,command=self.selection)
        self.menu.add_cascade(label="Time", menu=self.timeMenu)
        self.menu.add_separator()
        self.menu.add_command(
            label="\tClose\t", command=lambda: self.window.destroy())

        self.start = tk.Button(self.mainframe, text='Start',
                               width=8, borderwidth=0.01,
                               font=18,
                               bg="#2f3745", fg='white',
                               activebackground='#313b47', activeforeground='white',
                               command=self.Start)
        self.reset = tk.Button(self.mainframe,
                               text='Reset',
                               width=8, borderwidth=0.01,
                               font=18,
                               bg="#2f3745", fg='white',
                               activebackground='#313b47', activeforeground='white',
                               state='disabled',
                               command=self.Reset)
        self.start.grid(row=3, column=1)
        self.reset.grid(row=3, column=3)

        self.num = tk.Label(self.mainframe,
                            textvariable=self.counter,
                            font=18,
                            bd=1,
                            bg="#2f3745", fg='white',
                            pady=6)
        self.num.grid(row=0, column=2)

    def updateNum(self):
        self.totalSecs = self.defSecs
        minutes = int((self.totalSecs/60)+1 % 60)
        seconds = int((self.totalSecs+1) % 60)
        self.counter.set(f"{minutes:02}:{seconds:02}")

    def selection(self):
        self.defSecs = (int(self.radio.get())*300 + 1200)-1
        if self.running == False:
            self.updateNum()

    def do_popup(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)
        self.menu.grab_release()

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
        self.selection()
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
        self.breakWin = tk.Toplevel(self.window)
        self.breakWin.iconbitmap("clock.ico")
        self.breakWin.title("Break Time")
        self.breakWin.attributes('-alpha', 0.95)
        self.breakWin.resizable(False, False)
        self.breakWin.attributes('-fullscreen', 1)
        self.breakWin.grab_set()
        fm = tk.Frame(self.breakWin, bg="gray13")
        fm.pack(fill=tk.BOTH, expand=1)

        brTxt = tk.Label(fm, text="Time for a break",
                         font=("Arial", 25), fg="white", bg="gray13")
        brTxt.pack(side=tk.TOP, expand=1)

        txt = tk.Label(fm, text="for 20 seconds, look at something 20 feet away",
                       font=("Arial", 20), fg="#706F6C", bg="gray13")
        txt.pack(side=tk.TOP, expand=1)

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
        self.pBar = ttk.Progressbar(fm, orient=tk.HORIZONTAL, style="Horizontal.TProgressbar",
                                    mode='determinate', maximum=30,
                                    length=300, value=-1)
        self.pBar.pack(side=tk.TOP, expand=1)

        exitBtn = tk.Button(fm, width=10, text='Exit now', borderwidth=0.01, font=('Arial 12 underline'),
                            command=self.breakWin.destroy, activebackground='gray13',
                            activeforeground='white', bg="gray13", fg='white', relief=tk.FLAT)
        exitBtn.pack(side=tk.TOP, expand=1)
        exitBtn.bind("<Destroy>", lambda x: self.window.deiconify())
        self.breakWin.attributes("-topmost", True)
        self.updateProg()


def main():
    window = tk.Tk()
    app = counter(window)
    window.mainloop()


if __name__ == '__main__':
    main()
