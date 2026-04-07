import tkinter as tk
from backend import PlacementBackend


backend = PlacementBackend()


def predict():
    try:
        cgpa = float(entry1.get())
        dsa = int(entry2.get())
        aptitude = int(entry3.get())

        result_text = backend.predict_result(cgpa, dsa, aptitude)
        output_label.config(text=result_text)

    except ValueError:
        output_label.config(text="❌ Please enter valid numbers")


# GUI
root = tk.Tk()
root.title("Placement Predictor")
root.geometry("650x500")
root.configure(bg="lightblue")

# Main white frame
frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(
    frame,
    text="Student Placement Predictor",
    font=("Arial", 16, "bold"),
    bg="white"
).pack(pady=10)

tk.Label(frame, text="Enter CGPA", bg="white").pack()
entry1 = tk.Entry(frame)
entry1.pack()

tk.Label(frame, text="Enter DSA Solved", bg="white").pack()
entry2 = tk.Entry(frame)
entry2.pack()

tk.Label(frame, text="Enter Aptitude Score", bg="white").pack()
entry3 = tk.Entry(frame)
entry3.pack()

tk.Button(
    frame,
    text="Predict",
    command=predict,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=20)

output_label = tk.Label(
    frame,
    text="",
    font=("Arial", 12),
    bg="white",
    justify="left"
)
output_label.pack(pady=10)

root.mainloop()