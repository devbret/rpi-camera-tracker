# Raspberry Pi Camera Tracker

Runs continuously on a Raspberry Pi to periodically capture photos using the Pi camera, analyze their color characteristics and log results to a CSV file.

## Overview

More specifically, every 15 seconds this program takes a low-resolution image with `raspistill`, loads the image using `Pillow`, converts all pixel colors from RGB to HLS and computes the average hue and lightness across the image. Each measurement is timestamped and appended to `color_analysis.csv`, with the file and header created automatically if they do not already exist. The script is designed for long-running environmental or lighting analysis and can be cleanly stopped while preserving all collected data.

## Set Up Instructions

This application is intended to run on a Raspberry Pi computer, with the Raspberry Pi OS already installed. Below are the required software programs and instructions for installing and using this application.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps For Use

1. Install the above programs

2. Open a terminal

3. Clone this repository using `git` by running the following command: `git clone git@github.com:devbret/rpi-camera-tracker.git`

4. Navigate to the repo's directory by running: `cd rpi-camera-tracker`

5. Create a virtual environment with this command: `python3 -m venv venv`

6. Activate your virtual environment using: `source venv/bin/activate`

7. Install the needed dependencies for running the script: `pip install -r requirements.txt`

8. Run the program using this command: `python3 app.py`

9. To exit the virtual environment (venv), type this command in the terminal: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Capture images at fixed intervals in order to extract average hue and lightness values

- Log color analysis data to a CSV file for long-term tracking and visualization of lighting conditions

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
