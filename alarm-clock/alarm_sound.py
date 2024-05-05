import tkinter as tk
from tkinter.font import Font
import pygame.mixer
import wave
import os
from os.path import relpath
from threading import Thread
import random

class AlarmSound():
    def __init__(self, parent, set_window=False):
        self.parent = parent
        self.set_window = set_window
        self.thread = Thread(target=self.on_active, daemon=True)
        
        self.mp3_files = [relpath("alarm-clock/assets/sounds/beep1.mp3"),
                          relpath("alarm-clock/assets/sounds/beep2.mp3"),
                          relpath("alarm-clock/assets/sounds/beep3.mp3")]
        
        self.file = random.choice(self.mp3_files)
        
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(self.file)
        self.thread.start()

    def on_active(self):
        if self.set_window is True:
            self.window = tk.Toplevel(self.parent)
            self.window.title("Alarm Alarm!")
            self.label = tk.Label(self.window, text="Alarm Alarm !",
                                  font=Font(family='Helvetica', size=36, weight='bold'))
            self.stop_button = tk.Button(self.window, text="DUR",
                                         command=self.stop_sound,
                                         font=Font(family='Helvetica', size=20))
            self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=3)
            self.stop_button.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.sound.play(loops=-1)
        else:
            self.sound.play(loops=-1)

    def stop_sound(self):
        self.sound.stop()
        if self.set_window is True:
            self.window.destroy()
        self.parent.alarm_sound = None

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x100")
    root.minsize(400, 100)
    root.title("Alarm ses testi")
    alarm_sound = AlarmSound(root, set_window=True)
    root.mainloop()
