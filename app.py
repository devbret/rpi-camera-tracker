import subprocess
import os
import csv
import time
from PIL import Image
from colorsys import rgb_to_hls

CSV_FILE = "color_analysis.csv"
TEMP_IMAGE = "current_image.jpg"

def capture_image():
    """Capture an image using raspistill, overwriting the same file."""
    subprocess.run([
        "raspistill",
        "-o", TEMP_IMAGE,
        "-t", "1000",
        "-w", "640",
        "-h", "480"
    ])

def analyze_image(image_path):
    """Analyze the image to determine common hue and average lightness."""
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    hls_pixels = [rgb_to_hls(r/255, g/255, b/255) for r, g, b in pixels]
    
    hues = [h for h, _, _ in hls_pixels]
    lightness_values = [l for _, l, _ in hls_pixels]
    
    common_hue = round(sum(hues) / len(hues), 2)
    avg_lightness = round(sum(lightness_values) / len(lightness_values), 2)
    
    return common_hue, avg_lightness

def append_to_csv(timestamp, hue, lightness):
    """Append analysis data to a CSV file."""
    file_exists = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Hue", "Lightness"])
        writer.writerow([timestamp, hue, lightness])

def main():
    try:
        print("Starting image capture and analysis. Press Ctrl+C to stop.")
        
        while True:
            timestamp = time.strftime("%Y%m%d%H%M%S")
            
            capture_image()
            print(f"Captured image: {TEMP_IMAGE}")
            
            hue, lightness = analyze_image(TEMP_IMAGE)
            print(f"Analysis - Hue: {hue}, Lightness: {lightness}")
            
            append_to_csv(timestamp, hue, lightness)
            
            time.sleep(15)
    except KeyboardInterrupt:
        print("Stopping the script. CSV data saved.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
