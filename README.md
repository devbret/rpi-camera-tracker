# Raspberry Pi Camera Tracker

Runs continuously on a Raspberry Pi computer, periodically capturing photos with the Pi camera, analyzing their color characteristics and logging the results to a CSV file.

## Application Overview

Captures and analyzes environmental color and light data at regular 15-second intervals using a Raspberry Pi camera.

During each cycle, the script takes a low-resolution image with `raspistill`, saves it as a temporary image file and processes it with `Pillow`. The image pixels are converted from RGB to HLS color space so the program can calculate the average hue and lightness of the captured scene.

Each reading is then saved to `color_analysis.csv` with a timestamp, hue value and lightness value. If the CSV file does not already exist, the script automatically creates it and writes the appropriate header row.

This application is intended for long-running environmental, lighting or color-temperature-adjacent analysis. It can run continuously until stopped with `CTRL + C`, while preserving all measurements already written to the CSV file.

## Basic Setup Instructions

This application is intended to run on a Raspberry Pi computer, with the Raspberry Pi OS already installed. Below are the required software programs and instructions for installing and using this tool.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps For Use

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/rpi-camera-tracker.git`

4. Navigate to the repo's directory: `cd rpi-camera-tracker`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate your virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Run the program: `python3 app.py`

9. Exit the virtual environment: `deactivate`

## Other Considerations

Here you will find additional details about the repository itself, rather than the setup or operation of the application. More specifically, below is a summary of the skills this project is meant to demonstrate, followed by the licensing terms for the code and information on how to get in touch.

### Abilities Demonstrated

This project repo is intended to demonstrate an ability to do the following:

- Capture recurring image samples from a Raspberry Pi camera to monitor changes in environmental lighting over time

- Convert image color data into measurable hue and lightness values for simple long-term color analysis

- Record each timestamped measurement in a CSV file for later review, visualization or comparison

- Collect continuous environmental color data without requiring manual image analysis

### License Information

This project is released under the MIT License, with the full text available in the repository's [LICENSE](LICENSE) file. Which means you are free to use, modify, publish, distribute and sell copies of this software, including for commercial purposes, so long as the original copyright notice and permission notice are included with any substantial portion of the code. The software is provided "as is", without warranty of any kind and the copyright holder is not liable for any claim or damages arising from its use.

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
