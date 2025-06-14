#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import subprocess

class SimpleBrightnessController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Brightness Changer")
        self.root.geometry("640x480")
        self.root.resizable(False, False)
        
        # Configure dark theme colors
        self.colors = {
            'bg': '#2b2b2b',
            'fg': '#ffffff',
            'accent': '#5294e2',
            'button_bg': '#404040',
            'button_hover': '#4a4a4a',
            'scale_bg': '#3c3c3c',
            'scale_fg': '#5294e2'
        }
        
        # Apply dark theme
        self.root.configure(bg=self.colors['bg'])
        
        # Configure ttk styles for dark theme
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure frame style
        self.style.configure('Dark.TFrame', 
                           background=self.colors['bg'])
        
        # Configure label style
        self.style.configure('Dark.TLabel',
                           background=self.colors['bg'],
                           foreground=self.colors['fg'],
                           font=('Ubuntu', 12))
        
        self.style.configure('Title.TLabel',
                           background=self.colors['bg'],
                           foreground=self.colors['fg'],
                           font=('Ubuntu', 18, 'bold'))
        
        self.style.configure('Info.TLabel',
                           background=self.colors['bg'],
                           foreground='#cccccc',
                           font=('Ubuntu', 10))
        
        # Configure button style
        self.style.configure('Dark.TButton',
                           background=self.colors['button_bg'],
                           foreground=self.colors['fg'],
                           borderwidth=1,
                           focuscolor='none',
                           font=('Ubuntu', 10, 'bold'))
        
        self.style.map('Dark.TButton',
                      background=[('active', self.colors['button_hover']),
                                ('pressed', self.colors['accent'])])
        
        # Configure scale style
        self.style.configure('Dark.Horizontal.TScale',
                           background=self.colors['bg'],
                           darkcolor=self.colors['scale_bg'],
                           lightcolor=self.colors['scale_bg'],
                           troughcolor=self.colors['scale_bg'],
                           bordercolor=self.colors['scale_bg'],
                           arrowcolor=self.colors['fg'],
                           focuscolor='none')
        
        self.style.map('Dark.Horizontal.TScale',
                      background=[('active', self.colors['accent'])])
        
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
        
        main_frame = ttk.Frame(self.root, padding="40", style='Dark.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=1)
        
        # Title label
        title_label = ttk.Label(main_frame,
                               text="Ubuntu Brightness Control",
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, pady=(0, 30), sticky="ew")
        
        self.brightness_label = ttk.Label(main_frame, 
                                        text=f"Brightness: {self.current_brightness}%",
                                        style='Dark.TLabel')
        self.brightness_label.grid(row=1, column=0, pady=(0, 20), sticky="ew")
        
        self.brightness_scale = ttk.Scale(main_frame, 
                                        from_=10, 
                                        to=100,
                                        orient=tk.HORIZONTAL,
                                        length=500,
                                        style='Dark.Horizontal.TScale',
                                        command=self.set_brightness)
        self.brightness_scale.set(self.current_brightness)
        self.brightness_scale.grid(row=2, column=0, pady=(0, 30), sticky="ew")
        
        button_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        button_frame.grid(row=3, column=0, pady=(0, 30), sticky="ew")
        button_frame.columnconfigure((0,1,2,3), weight=1)
        
        ttk.Button(button_frame, text="25%", style='Dark.TButton',
                  command=lambda: self.brightness_scale.set(25)).grid(row=0, column=0, padx=5, sticky="ew")
        ttk.Button(button_frame, text="50%", style='Dark.TButton',
                  command=lambda: self.brightness_scale.set(50)).grid(row=0, column=1, padx=5, sticky="ew")
        ttk.Button(button_frame, text="75%", style='Dark.TButton',
                  command=lambda: self.brightness_scale.set(75)).grid(row=0, column=2, padx=5, sticky="ew")
        ttk.Button(button_frame, text="100%", style='Dark.TButton',
                  command=lambda: self.brightness_scale.set(100)).grid(row=0, column=3, padx=5, sticky="ew")
        
        info_label = ttk.Label(main_frame, 
                             text=f"Monitor: {self.monitor_name} • Software brightness control",
                             style='Info.TLabel')
        info_label.grid(row=4, column=0, pady=(20, 0), sticky="ew")
    
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