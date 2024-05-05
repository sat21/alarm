import tkinter as tk
from tkinter.font import Font
from time import strftime, localtime, sleep
from threading import Thread


class Clock(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.time = strftime("%I:%M:%S %p", localtime())
        
        self.kill = False

        self.time_label = tk.Label(self, text=self.time,
                                   font=Font(family='Helvetica', size=36,
                                             weight='bold'))
       
        self.time_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.thread = Thread(target=self.update, daemon=True)

    def update(self):
        while True:
            if self.kill:
                break
            self.time = strftime("%I:%M:%S %p", localtime())
           
            self.time_label["text"] = self.time
           
            sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("saat")
    root.geometry("600x185")
    root.minsize(400, 150)
    clock = Clock(root)
    clock.pack(fill=tk.BOTH, expand=1)
    clock.thread.start()
    root.mainloop()