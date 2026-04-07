import tkinter as tk
from PIL import Image, ImageTk
from code import PlacementBackend  # backend

code = PlacementBackend()


def predict():
    try:
        cgpa = float(entry_cgpa.get())
        dsa = int(entry_dsa.get())
        aptitude = int(entry_aptitude.get())
        certifications = int(entry_certifications.get())
        internships = int(entry_internships.get())
        projects = int(entry_projects.get())

        result_text = code.predict_result(cgpa, dsa, aptitude, certifications, internships, projects)
        output_label.config(text=result_text)

    except ValueError:
        output_label.config(text=" Please enter valid numbers")


# ----------------- Main Window -----------------
root = tk.Tk()
root.title("Student Placement Predictor")
root.state('zoomed')  # Full screen

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load background image
image_path = r"C:\Users\sharm\Pictures\Screenshots\Screenshot 2026-04-06 223724.png"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((screen_width, screen_height))  # Resize to full screen
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for full window background
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# ----------------- Frame -----------------
frame = tk.Frame(root, bg="#66cdaa", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Heading
tk.Label(frame, text="Student Placement Predictor", font=("Arial", 25, "bold"), bg="white").pack(pady=10)

# CGPA
tk.Label(frame, text="Enter CGPA", bg="white", font=("Arial", 14)).pack()
entry_cgpa = tk.Entry(frame, font=("Arial", 14))
entry_cgpa.pack(pady=5)

# DSA
tk.Label(frame, text="Enter DSA Solved", bg="white", font=("Arial", 15)).pack()
entry_dsa = tk.Entry(frame, font=("Arial", 14))
entry_dsa.pack(pady=5)

# Aptitude
tk.Label(frame, text="Enter Aptitude Score", bg="white", font=("Arial", 14)).pack()
entry_aptitude = tk.Entry(frame, font=("Arial", 14))
entry_aptitude.pack(pady=5)

# Certifications
tk.Label(frame, text="Enter Number of Certifications", bg="white", font=("Arial", 14)).pack()
entry_certifications = tk.Entry(frame, font=("Arial", 14))
entry_certifications.pack(pady=5)

# Internships
tk.Label(frame, text="Enter Number of Internships", bg="white", font=("Arial", 14)).pack()
entry_internships = tk.Entry(frame, font=("Arial", 14))
entry_internships.pack(pady=5)

# Projects
tk.Label(frame, text="Enter Number of Projects", bg="white", font=("Arial", 14)).pack()
entry_projects = tk.Entry(frame, font=("Arial", 14))
entry_projects.pack(pady=5)

# Predict Button
tk.Button(frame, text="Predict", command=predict, bg="green", fg="white", font=("Arial", 14, "bold")).pack(pady=15)

# Output Label
output_label = tk.Label(frame, text="", font=("Arial", 14), bg="white", justify="left")
output_label.pack(pady=10)

root.mainloop()