import tkinter as tk
from tkinter import messagebox, font, ttk
import joblib
import numpy as np

# Load the pre-trained model
model_filename = 'random_forest_model.pkl'
model = joblib.load(model_filename)

# Function to make a prediction
def predict_class():
    try:
        # Collect input values
        inputs = np.array([
            float(entry_obj_ID.get()),
            float(entry_alpha.get()),
            float(entry_delta.get()),
            float(entry_u.get()),
            float(entry_g.get()),
            float(entry_r.get()),
            float(entry_i.get()),
            float(entry_z.get()),
            float(entry_run_ID.get()),
            float(entry_rereun_ID.get()),
            float(entry_cam_col.get()),
            float(entry_field_ID.get()),
            float(entry_spec_obj_ID.get()),
            float(entry_redshift.get()),
            float(entry_plate.get()),
            float(entry_MJD.get()),
            float(entry_fiber_ID.get())
        ]).reshape(1, -1)

        # Predict the class using the loaded model
        prediction = model.predict(inputs)
        prediction_text = f'Predicted Class: {prediction[0]}'

        # Display the result in the output label
        result_label.config(text=prediction_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Astronomical Object Classification")

# Create a frame and canvas for scrolling
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

canvas = tk.Canvas(main_frame)
scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Place canvas and scrollbar in the main window
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create a heading label for the window
heading_font = font.Font(scrollable_frame, size=18, weight='bold')
heading_label = tk.Label(scrollable_frame, text="Stellar Classification", font=heading_font)
heading_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

# Create labels and entry fields for each attribute
fields = [
    "Object Identifier", "Right Ascension (alpha)", "Declination (delta)", "Ultraviolet filter (u)", 
    "Green filter (g)", "Red filter (r)", "Near Infrared filter (i)", "Infrared filter (z)", 
    "Run Number", "Rerun Number", "Camera Column", "Field Number", "Spectroscopic Object ID", 
    "Redshift", "Plate ID", "Modified Julian Date (MJD)", "Fiber ID"
]

entries = []
for i, field in enumerate(fields):
    label = tk.Label(scrollable_frame, text=field)
    label.grid(row=i+1, column=0, sticky='e', padx=5, pady=5)
    entry = tk.Entry(scrollable_frame)
    entry.grid(row=i+1, column=1, padx=5, pady=5)
    entries.append(entry)

# Map entry fields to variables
(entry_obj_ID, entry_alpha, entry_delta, entry_u, entry_g, entry_r, 
 entry_i, entry_z, entry_run_ID, entry_rereun_ID, entry_cam_col, 
 entry_field_ID, entry_spec_obj_ID, entry_redshift, entry_plate, 
 entry_MJD, entry_fiber_ID) = entries

# Create a button to submit the input and predict the class
predict_button = tk.Button(scrollable_frame, text="Predict Class", command=predict_class)
predict_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

# Label to display the prediction result
result_label = tk.Label(scrollable_frame, text="", font=('Arial', 14))
result_label.grid(row=len(fields)+2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
