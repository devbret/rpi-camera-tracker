# Raspberry Pi Camera Tracker

Runs continuously on a Raspberry Pi to periodically capture photos using the Pi camera, analyze their color characteristics and log results to a CSV file.

## Overview

More specifically, every 15 seconds this program takes a low-resolution image with `raspistill`, loads the image using `Pillow`, converts all pixel colors from RGB to HLS and computes the average hue and lightness across the image. Each measurement is timestamped and appended to `color_analysis.csv`, with the file and header created automatically if they do not already exist. The script is designed for long-running environmental or lighting analysis and can be cleanly stopped while preserving all collected data.
