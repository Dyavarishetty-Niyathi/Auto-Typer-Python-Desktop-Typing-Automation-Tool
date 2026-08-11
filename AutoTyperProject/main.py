import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import keyboard
import threading
import time

pyautogui.PAUSE = 0.03
pyautogui.FAILSAFE = True

class AutoTyperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Typer")
        self.root.geometry("700x550")
        self.root.configure(bg="#1e1e1e")

        self.is_typing = False
        self.is_paused = False
        self.current_index = 0
        self.typing_thread = None

        title = tk.Label(
            root,
            text="Auto Typer",
            font=("Arial", 20, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        title.pack(pady=10)

        self.text_box = tk.Text(
            root,
            height=10,
            width=70,
            font=("Arial", 12),
            bg="#2b2b2b",
            fg="white",
            insertbackground="white"
        )
        self.text_box.pack(pady=10)

        controls_frame = tk.Frame(root, bg="#1e1e1e")
        controls_frame.pack(pady=10)

        tk.Label(
            controls_frame,
            text="Typing Speed (seconds per character)",
            bg="#1e1e1e",
            fg="white"
        ).grid(row=0, column=0, padx=10, pady=5)

        self.speed_slider = tk.Scale(
            controls_frame,
            from_=0.01,
            to=0.3,
            resolution=0.01,
            orient="horizontal",
            length=200,
            bg="#1e1e1e",
            fg="white",
            highlightthickness=0
        )
        self.speed_slider.set(0.1)
        self.speed_slider.grid(row=0, column=1, padx=10)

        tk.Label(
            controls_frame,
            text="Start Delay (seconds)",
            bg="#1e1e1e",
            fg="white"
        ).grid(row=1, column=0, padx=10, pady=5)

        self.delay_box = ttk.Combobox(
            controls_frame,
            values=[3, 5, 10],
            width=10
        )
        self.delay_box.set(5)
        self.delay_box.grid(row=1, column=1, padx=10)

        tk.Label(
            controls_frame,
            text="Repeat Count",
            bg="#1e1e1e",
            fg="white"
        ).grid(row=2, column=0, padx=10, pady=5)

        self.repeat_box = tk.Entry(controls_frame, width=12)
        self.repeat_box.insert(0, "1")
        self.repeat_box.grid(row=2, column=1, padx=10)

        button_frame = tk.Frame(root, bg="#1e1e1e")
        button_frame.pack(pady=15)

        start_btn = tk.Button(
            button_frame,
            text="Start",
            command=self.start_typing,
            bg="#4CAF50",
            fg="white",
            width=12,
            relief="flat"
        )
        start_btn.grid(row=0, column=0, padx=10)

        pause_btn = tk.Button(
            button_frame,
            text="Pause / Resume",
            command=self.pause_resume_typing,
            bg="#FFC107",
            fg="black",
            width=15,
            relief="flat"
        )
        pause_btn.grid(row=0, column=1, padx=10)

        stop_btn = tk.Button(
            button_frame,
            text="Stop",
            command=self.stop_typing,
            bg="#F44336",
            fg="white",
            width=12,
            relief="flat"
        )
        stop_btn.grid(row=0, column=2, padx=10)

        self.status_label = tk.Label(
            root,
            text="Status: Stopped",
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="lightgreen"
        )
        self.status_label.pack(pady=10)

        self.progress_label = tk.Label(
            root,
            text="Progress: 0 characters typed",
            font=("Arial", 11),
            bg="#1e1e1e",
            fg="white"
        )
        self.progress_label.pack()

        keyboard.add_hotkey('F6', self.start_typing)
        keyboard.add_hotkey('F7', self.stop_typing)

    def start_typing(self):
        if self.is_typing:
            return

        text = self.text_box.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter some text first.")
            return

        self.is_typing = True
        self.is_paused = False
        self.current_index = 0

        self.typing_thread = threading.Thread(target=self.type_text)
        self.typing_thread.daemon = True
        self.typing_thread.start()

    def type_text(self):
        text = self.text_box.get("1.0", tk.END).strip()
        speed = self.speed_slider.get()
        delay = int(self.delay_box.get())

        try:
            repeat_count = int(self.repeat_box.get())
        except:
            repeat_count = 1

        self.status_label.config(text=f"Status: Starting in {delay} seconds...")
        time.sleep(delay)

        total_text = (text + "\n") * repeat_count
        total_length = len(total_text)

        self.status_label.config(text="Status: Typing...")

        while self.current_index < total_length and self.is_typing:
            if self.is_paused:
                time.sleep(0.1)
                continue

            current_char = total_text[self.current_index]

            if current_char == "":
                pyautogui.press("enter")
            elif current_char == "	":
                pyautogui.press("tab")
            elif current_char == " ":
                pyautogui.press("space")
            else:
                keyboard.write(current_char)

            time.sleep(0.03)
            self.current_index += 1

            self.progress_label.config(
                text=f"Progress: Typed {self.current_index} out of {total_length} characters"
            )

            time.sleep(speed)

        if self.is_typing:
            self.status_label.config(text="Status: Finished")
        else:
            self.status_label.config(text="Status: Stopped")

        self.is_typing = False

    def pause_resume_typing(self):
        if not self.is_typing:
            return

        self.is_paused = not self.is_paused

        if self.is_paused:
            self.status_label.config(text="Status: Paused")
        else:
            self.status_label.config(text="Status: Typing...")

    def stop_typing(self):
        self.is_typing = False
        self.is_paused = False
        self.status_label.config(text="Status: Stopped")

root = tk.Tk()
app = AutoTyperApp(root)
root.mainloop()