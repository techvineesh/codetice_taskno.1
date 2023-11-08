import tkinter as tk
from tkinter import messagebox
import pyshorteners
def shorten_url():
    long_url = entry.get()
    if long_url:
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(long_url)
            short_entry.insert(0,short_url)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "Please enter a URL.")

# Create the main window
window = tk.Tk()
window.title("URL Shortener")
window.geometry("400x150")
# Create and configure the widgets
label = tk.Label(window, text="Enter a URL:")
label.pack()

entry = tk.Entry(window)
entry.pack()

#label1 = tk.Label(window, text="output  URL:")
#label1.pack()


shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack()

shortened_url_var = tk.Label(window, text="output  URL:")
shortened_url_var.pack()

short_entry = tk.Entry(window)
short_entry.pack()

# Run the Tkinter main loop
window.mainloop()
