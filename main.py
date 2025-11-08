# main.py
import tkinter as tk
from tkinter import ttk
from mood_analyzer import analyze_mood

# --- Constants: Professional Fonts ---
FONT_FAMILY = "Helvetica"  # Modern, clean, professional
TITLE_FONT = (FONT_FAMILY, 22, "bold")       # Main headings
SUBTITLE_FONT = (FONT_FAMILY, 16, "bold")   # Section headings
BODY_FONT = (FONT_FAMILY, 13)               # Standard body text
INPUT_FONT = (FONT_FAMILY, 14)              # Input fields
RESULT_FONT = (FONT_FAMILY, 15, "italic")  # Results or feedback text
MOOD_DISPLAY_FONT = (FONT_FAMILY, 14, "bold")  # Mood display
BUTTON_FONT = (FONT_FAMILY, 13, "bold")    # Buttons

# --- Themes ---
THEMES = {
    
    "dark": {
        "bg": "#2c3e50", "fg": "#ecf0f1", "input_bg": "#34495e",
        "btn_bg": "#3498db", "btn_active": "#2980b9", "exit_btn_bg": "#e74c3c", "exit_btn_active": "#c0392b",
        "positive": "#2ecc71", "negative": "#e74c3c", "motivational": "#3498db", "neutral": "#95a5a6"
    },
    "light": {
        "bg": "#f4f6f7", "fg": "#000000", "input_bg": "#9bc7ca",
        "btn_bg": "#55a9ca", "btn_active": "#3498db", "exit_btn_bg": "#e74c3c", "exit_btn_active": "#c0392b",
        "positive": "#2ad6dc", "negative": "#c0392b", "motivational": "#2980b9", "neutral": "#7f8c8d"
    }
}
current_theme = "dark"
user_name = ""

# --- Functions ---
def apply_theme(theme_name):
    """Applies the selected theme to all widgets."""
    global current_theme
    current_theme = theme_name
    theme = THEMES[theme_name]
    
    root.config(bg=theme["bg"])
    main_frame.config(bg=theme["bg"])
    title_label.config(bg=theme["bg"], fg=theme["fg"])
    mood_display_label.config(bg=theme["bg"], fg=theme["fg"])
    result_label.config(bg=theme["bg"])
    
    text_input.config(bg=theme["input_bg"], fg=theme["fg"], insertbackground=theme["fg"])
    
    style.configure("TButton", background=theme["btn_bg"], foreground=theme["fg"])
    style.map("TButton", background=[('active', theme["btn_active"])])
    style.configure("Exit.TButton", background=theme["exit_btn_bg"])
    style.map("Exit.TButton", background=[('active', theme["exit_btn_active"])])
    
    theme_button.config(text="Light Mode" if theme_name == "dark" else "Dark Mode")

def toggle_theme():
    """Toggles between dark and light themes."""
    apply_theme("light" if current_theme == "dark" else "dark")

def check_mood(event=None):
    """Gets the user's input, analyzes the mood, and updates the GUI."""
    user_input = text_input.get("1.0", "end-1c").strip()
    theme = THEMES[current_theme]
    
    if user_input:
        mood, message = analyze_mood(user_input)
        mood_display_label.config(text=f"Detected Mood: {mood.capitalize()}")
        result_label.config(text=message)
        
        color_map = {"positive": theme["positive"], "negative": theme["negative"], "motivational": theme["motivational"], "neutral": theme["neutral"]}
        result_label.config(fg=color_map.get(mood, theme["neutral"]))
    else:
        mood_display_label.config(text="")
        result_label.config(text="Please enter how you feel.", fg=theme["neutral"])
    return "break"

def show_exit_screen():
    """Displays a thank you message and closes the app."""
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    theme = THEMES[current_theme]
    main_frame.config(bg=theme["bg"])
    
    thank_you_label = tk.Label(main_frame, text=f"Thank you for using Mood Checker, {user_name}!", font=TITLE_FONT, bg=theme["bg"], fg=theme["fg"])
    thank_you_label.pack(expand=True)
    
    root.after(2500, root.destroy)

def custom_ask_name():
    """Creates a custom dialog to ask for the user's name."""
    dialog = tk.Toplevel(root)
    dialog.title("Welcome")
    dialog.geometry("350x180")
    dialog.resizable(False, False)
    
    theme = THEMES["dark"]
    dialog.config(bg=theme["bg"])
    
    dialog.transient(root)
    dialog.grab_set()
    
    # Center the dialog
    root.update_idletasks()
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_w = root.winfo_width()
    root_h = root.winfo_height()
    dialog_x = root_x + (root_w // 2) - (350 // 2)
    dialog_y = root_y + (root_h // 2) - (180 // 2)
    dialog.geometry(f"+{dialog_x}+{dialog_y}")

    name_var = tk.StringVar()

    def on_submit():
        global user_name
        user_name = name_var.get().strip()
        if not user_name:
            user_name = "there"
        dialog.destroy()

    prompt_label = tk.Label(dialog, text="What's your name?", font=(FONT_FAMILY, 14), bg=theme["bg"], fg=theme["fg"])
    prompt_label.pack(pady=(20, 10))

    name_entry = tk.Entry(dialog, textvariable=name_var, font=INPUT_FONT, bg=theme["input_bg"], fg=theme["fg"], insertbackground=theme["fg"], bd=0, justify='center')
    name_entry.pack(pady=10, padx=20, fill='x')
    name_entry.focus_set()
    name_entry.bind("<Return>", lambda event: on_submit())

    submit_button = ttk.Button(dialog, text="Continue", command=on_submit, style="TButton")
    submit_button.pack(pady=10)
    
    root.wait_window(dialog)

# --- GUI Setup ---
root = tk.Tk()
root.title("Mood Checker")
root.geometry("550x450")
root.minsize(450, 400)

# Center and maximize window
root.update_idletasks()
root.state('zoomed')
root.eval('tk::PlaceWindow . center')

custom_ask_name()

# --- Style ---
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=BODY_FONT, borderwidth=0, padding=12, relief="flat")

# --- Widgets ---
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=30, pady=20)
main_frame.columnconfigure(0, weight=1)

theme_button = ttk.Button(main_frame, text="Light Mode", command=toggle_theme, style="TButton")
theme_button.grid(row=0, column=0, sticky="ne", pady=(0, 10))

title_label = tk.Label(main_frame, text=f"How are you feeling today, {user_name}?", font=TITLE_FONT)
title_label.grid(row=1, column=0, pady=(10, 20))

text_input = tk.Text(main_frame, height=5, font=INPUT_FONT, bd=0, relief="flat", wrap="word", highlightthickness=0)
text_input.grid(row=2, column=0, sticky="ew", pady=(0, 20))
text_input.focus_set()
text_input.bind("<Return>", check_mood)

check_button = ttk.Button(main_frame, text="Check Mood", style="TButton", command=check_mood)
check_button.grid(row=3, column=0, sticky="W", padx=20, pady=(0, 20))



mood_display_label = tk.Label(main_frame, text="", font=MOOD_DISPLAY_FONT)
mood_display_label.grid(row=4, column=0, pady=(0, 5))

result_label = tk.Label(main_frame, text="", font=RESULT_FONT)
result_label.grid(row=5, column=0, pady=(0, 20))

exit_button = ttk.Button(main_frame, text="Exit", command=show_exit_screen, style="Exit.TButton")
exit_button.grid(row=6, column=0, pady=(20, 0), sticky="s")
main_frame.rowconfigure(6, weight=1)

apply_theme("dark")
root.mainloop()
print("Program finished")