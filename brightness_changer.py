#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import subprocess

class SimpleBrightnessController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Brightness Changer")
        self.root.geometry("450x200")
        self.root.resizable(True, True)
        
        self.monitor_name = self.find_monitor()
        self.current_brightness = 100
        
        if not self.monitor_name:
            self.show_error("No monitor found for xrandr control!")
            return
            
        self.setup_ui()
        
    def find_monitor(self):
        try:
            result = subprocess.run(["xrandr", "--listmonitors"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for line in lines[1:]:  # Skip header
                    if ':' in line:
                        monitor_name = line.split()[-1]
                        return monitor_name
        except:
            pass
        return None
    
    def set_brightness(self, value):
        brightness_percent = int(float(value))
        brightness_float = brightness_percent / 100.0
        brightness_float = max(0.1, min(1.0, brightness_float))  # Clamp between 0.1 and 1.0
        
        try:
            subprocess.run(['xrandr', '--output', self.monitor_name, '--brightness', str(brightness_float)], 
                         check=True)
            self.brightness_label.config(text=f"Brightness: {brightness_percent}%")
            self.current_brightness = brightness_percent
        except Exception as e:
            self.brightness_label.config(text=f"Brightness: {brightness_percent}% (Error)")
            print(f"Error setting brightness: {e}")
    
    def setup_ui(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=1)
        
        self.brightness_label = ttk.Label(main_frame, 
                                        text=f"Brightness: {self.current_brightness}%",
                                        font=("Arial", 12))
        self.brightness_label.grid(row=0, column=0, pady=(0, 15), sticky="ew")
        
        self.brightness_scale = ttk.Scale(main_frame, 
                                        from_=10, 
                                        to=100,
                                        orient=tk.HORIZONTAL,
                                        length=350,
                                        command=self.set_brightness)
        self.brightness_scale.set(self.current_brightness)
        self.brightness_scale.grid(row=1, column=0, pady=(0, 20), sticky="ew")
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=(0, 15), sticky="ew")
        button_frame.columnconfigure((0,1,2,3), weight=1)
        
        ttk.Button(button_frame, text="25%", 
                  command=lambda: self.brightness_scale.set(25)).grid(row=0, column=0, padx=2, sticky="ew")
        ttk.Button(button_frame, text="50%", 
                  command=lambda: self.brightness_scale.set(50)).grid(row=0, column=1, padx=2, sticky="ew")
        ttk.Button(button_frame, text="75%", 
                  command=lambda: self.brightness_scale.set(75)).grid(row=0, column=2, padx=2, sticky="ew")
        ttk.Button(button_frame, text="100%", 
                  command=lambda: self.brightness_scale.set(100)).grid(row=0, column=3, padx=2, sticky="ew")
        
        info_label = ttk.Label(main_frame, 
                             text=f"Monitor: {self.monitor_name} (Software control)",
                             font=("Arial", 9))
        info_label.grid(row=3, column=0, pady=(10, 0), sticky="ew")
    
    def show_error(self, message):
        error_window = tk.Toplevel()
        error_window.title("Error")
        error_window.geometry("300x100")
        ttk.Label(error_window, text=message).pack(pady=20)
        ttk.Button(error_window, text="OK", command=error_window.destroy).pack()
    
    def run(self):
        if hasattr(self, 'monitor_name') and self.monitor_name:
            self.root.mainloop()

if __name__ == "__main__":
    app = SimpleBrightnessController()
    app.run()