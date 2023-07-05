import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Set the window title
window.title("Python Pizza Deliveries")

# Function to handle size section
def size_section():
    def validate_size():
        size = size_entry.get().upper()
        if size in ["1", "2", "3", "S", "M", "L"]:
            size_frame.destroy()
        elif size in ["Q"]:
            window.destroy()
        else:
            size_entry.delete(0, tk.END)
            size_entry.insert(tk.END, "Invalid size, please enter again.")

    size_frame = tk.Frame(window)
    size_label = tk.Label(size_frame, text="What size pizza do you want?")
    size_entry = tk.Entry(size_frame)
    size_button = tk.Button(size_frame, text="Submit", command=validate_size)

    size_label.pack()
    size_entry.pack()
    size_button.pack()
    size_frame.pack()

# Function to handle pepperoni section
def pepperoni_section():
    def validate_pepperoni():
        add_pepperoni = pepperoni_entry.get().upper()
        if add_pepperoni in ["Y", "N"]:
            pepperoni_frame.destroy()
        else:
            pepperoni_entry.delete(0, tk.END)
            pepperoni_entry.insert(tk.END, "Invalid input, please enter again.")

    pepperoni_frame = tk.Frame(window)
    pepperoni_label = tk.Label(pepperoni_frame, text="Do you want pepperoni?")
    pepperoni_entry = tk.Entry(pepperoni_frame)
    pepperoni_button = tk.Button(pepperoni_frame, text="Submit", command=validate_pepperoni)

    pepperoni_label.pack()
    pepperoni_entry.pack()
    pepperoni_button.pack()
    pepperoni_frame.pack()

# Function to handle extra cheese section
def extra_cheese_section():
    def validate_extra_cheese():
        extra_cheese = extra_cheese_entry.get().upper()
        if extra_cheese in ["Y", "N"]:
            extra_cheese_frame.destroy()
        else:
            extra_cheese_entry.delete(0, tk.END)
            extra_cheese_entry.insert(tk.END, "Invalid input, please enter again.")

    extra_cheese_frame = tk.Frame(window)
    extra_cheese_label = tk.Label(extra_cheese_frame, text="Do you want extra cheese?")
    extra_cheese_entry = tk.Entry(extra_cheese_frame)
    extra_cheese_button = tk.Button(extra_cheese_frame, text="Submit", command=validate_extra_cheese)

    extra_cheese_label.pack()
    extra_cheese_entry.pack()
    extra_cheese_button.pack()
    extra_cheese_frame.pack()

# Call the functions
size_section()
pepperoni_section()
extra_cheese_section()

# Start the Tkinter event loop
window.mainloop()
