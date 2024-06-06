import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Simulated data for demonstration purposes
categories = ["Cádiz", "Chacanes", "Mensajero", "Redes sociales", "Compras: Mercado", "De compras: Moda y Belleza"]
data = {
    "App Name": [f"App{i}" for i in range(1, 21)],
    "Downloads": [i * 1000 for i in range(1, 21)],
    "Date": pd.date_range(start="2021-12-01", periods=20, freq='D')
}

# Create directories for storing results
if not os.path.exists("results"):
    os.makedirs("results")
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Function to create and save a CSV file
def save_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Function to create and save a download graph screenshot
def save_screenshot(data, app_name, category):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Downloads'], marker='o')
    plt.title(f"Downloads Over Time for {app_name} in {category}")
    plt.xlabel('Date')
    plt.ylabel('Downloads')
    plt.grid(True)
    plt.savefig(f"screenshots/{category}_{app_name}.png")
    plt.close()

# Main process to handle each category
for category in categories:
    # Simulating data extraction for each category
    app_data = {
        "App Name": data["App Name"],
        "Downloads": data["Downloads"],
        "Date": data["Date"]
    }
    
    # Save the top 20 apps list to a CSV
    csv_filename = f"results/{category}_top_20_apps.csv"
    save_csv(app_data, csv_filename)
    
    # Save the download data graph and screenshots for each app
    for app in app_data["App Name"]:
        app_specific_data = {
            "Date": app_data["Date"],
            "Downloads": [d + i*50 for i, d in enumerate(app_data["Downloads"])]  # Simulated download data trend
        }
        
        # Save the app-specific download data to a CSV
        app_csv_filename = f"results/{category}_{app}_downloads.csv"
        save_csv(app_specific_data, app_csv_filename)
        
        # Save a screenshot of the download graph
        save_screenshot(app_specific_data, app, category)

print("Data extraction and visualization complete!")
