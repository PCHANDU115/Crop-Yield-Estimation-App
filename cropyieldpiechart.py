import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define the crop yield estimation function
def estimate_yield(crop_type, planting_area, soil_condition, fertilizer, pesticide, water_avail):
    crop_coefficients = {'Wheat': 1.2, 'Corn': 1.5, 'Rice': 1.3}
    soil_coefficients = {'Good': 1.1, 'Average': 1.0, 'Poor': 0.9}

    crop_coeff = crop_coefficients.get(crop_type, 1.0)
    soil_coeff = soil_coefficients.get(soil_condition, 1.0)

    # Calculate the yield estimate considering fertilizers, pesticide, and water
    yield_estimate = crop_coeff * soil_coeff * planting_area + (fertilizer * 0.01) + (pesticide * 0.5) + (water_avail * 0.2)
    return yield_estimate

# Function to plot the Pie Chart
def plot_yield_pie(crop_type, fertilizer, pesticide, water_avail):
    # Pie chart for contributions of fertilizer, pesticide, and water availability to yield
    labels = ['Fertilizer', 'Pesticide', 'Water Availability']
    sizes = [fertilizer, pesticide, water_avail]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99', '#ff6666'])
    plt.title(f"Contributions to {crop_type} Yield")
    
    # Embed the pie chart in Tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Function to update the result and plot
def update_results():
    try:
        crop_type = crop_type_var.get()
        planting_area = float(planting_area_entry.get())
        soil_condition = soil_condition_var.get()
        fertilizer = float(fertilizer_entry.get())
        pesticide = float(pesticide_entry.get())
        water_avail = float(water_avail_entry.get())

        # Estimate the yield based on inputs
        yield_estimate = estimate_yield(crop_type, planting_area, soil_condition, fertilizer, pesticide, water_avail)
        
        # Update result label
        result_label.config(text=f"Estimated Crop Yield: {yield_estimate:.2f} tons")

        # Plotting the pie chart
        plot_yield_pie(crop_type, fertilizer, pesticide, water_avail)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the inputs.")

# GUI setup
root = tk.Tk()
root.title("Crop Yield Estimation Tool")

# Create a frame for the left side (inputs)
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Crop Type
tk.Label(left_frame, text="Select Crop Type:", font=("Arial", 12)).pack(pady=5)
crop_type_var = tk.StringVar(value='Wheat')
crop_type_menu = ttk.Combobox(left_frame, textvariable=crop_type_var, values=['Wheat', 'Corn', 'Rice'], font=("Arial", 12))
crop_type_menu.pack(pady=5)

# Planting Area
tk.Label(left_frame, text="Enter Planting Area (hectares):", font=("Arial", 12)).pack(pady=5)
planting_area_entry = tk.Entry(left_frame, font=("Arial", 12))
planting_area_entry.pack(pady=5)

# Soil Condition
tk.Label(left_frame, text="Select Soil Condition:", font=("Arial", 12)).pack(pady=5)
soil_condition_var = tk.StringVar(value='Good')
soil_condition_menu = ttk.Combobox(left_frame, textvariable=soil_condition_var, values=['Good', 'Average', 'Poor'], font=("Arial", 12))
soil_condition_menu.pack(pady=5)

# Fertilizer Usage
tk.Label(left_frame, text="Enter Fertilizer Usage (kg/ha):", font=("Arial", 12)).pack(pady=5)
fertilizer_entry = tk.Entry(left_frame, font=("Arial", 12))
fertilizer_entry.pack(pady=5)

# Pesticide Usage
tk.Label(left_frame, text="Enter Pesticide Usage (L/ha):", font=("Arial", 12)).pack(pady=5)
pesticide_entry = tk.Entry(left_frame, font=("Arial", 12))
pesticide_entry.pack(pady=5)

# Water Availability
tk.Label(left_frame, text="Enter Water Availability (mm):", font=("Arial", 12)).pack(pady=5)
water_avail_entry = tk.Entry(left_frame, font=("Arial", 12))
water_avail_entry.pack(pady=5)

# Result Label
result_label = tk.Label(left_frame, text="Estimated Crop Yield: ", font=("Arial", 14))
result_label.pack(pady=10)

# Update Button
update_button = tk.Button(left_frame, text="Estimate Yield", command=update_results, font=("Arial", 12))
update_button.pack(pady=10)

# Create a frame for the right side (graph area)
plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)

# Start the Tkinter GUI
root.mainloop()
