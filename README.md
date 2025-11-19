# Death Star Image Transmission

## Project Overview
This project was developed as a team challenge with a budget constraint of $300. The mission: **retrieve and securely transfer 10 specific "Death Star" images from a collection of 100** found on a thumb drive, using a method that avoids conventional networking and physical connections—no WiFi, no wired Ethernet, and no physical transfer mediums that could risk interception under 10 minutes. All image transmission must be encrypted druing transmission and occur without being detected by "guards," simulating a highly sensitive covert operation.

## Problem Statement
- You are given 100 Death Star images on a thumb drive.
- The task is to identify exactly 10 target images based on specific vulnerabilities/patterns.
- After identification and cropping the vulnerabilities, transmit these images from a Raspberry Pi system (the "sender") to a server(the "receiver") for display in a mobile app.
- Transmission **must not use any typical network protocol or wired connection** and **should be transmitted under 10 minutes** .

## Solution Approach
Leveraging a combination of **Li-Fi (Light Fidelity)** for secure, wire-free optical transmission, image processing, machine learning, and secure server integration:

1. **Image Identification & Processing:**
   - Machine learning (TensorFlow, OpenCV) deployed on Raspberry Pi to:
     - Detect targeted Death Star images from the dataset.
     - Highlight and crop vulnerabilities on identified images.
     - Encrypt processed images for secure transmission.

2. **Li-Fi Data Transmission:**
   - Sender Raspberry Pi transmits encrypted images via Li-Fi to a second Raspberry Pi (receiver).
   - No WiFi, Bluetooth, or wired connections were used, ensuring covert communications.

3. **Server Integration & App:**
   - The receiver Raspberry Pi uploads received images to an AWS server.
   - Mobile/web app displays the transmitted images, allowing authenticated users to download the results.

## Technologies Used
- **Machine Learning & Image Processing:** TensorFlow, OpenCV, Python.
- **Hardware:** Raspberry Pi (sender & receiver), Zigbee 3.0 USB Dongle Plus-E, Square 64 LED Board, PhotoTransistor Light Sensor, HT12E Encoder IC, HT12D Decoder IC, Jumper wires, BC547 Transistor,10K Preset, Some Colour LEDs, IR Led/Laser diode, 1M,47K,1K,100, Push Buttons and LM358 Op-Amp IC.
- **Transmission:** Li-Fi (optical communication — DIY setup).
- **Server:** AWS (S3 or EC2 for image storage and retrieval).
- **App:** Mobile/Web app (using Flutter/Dart).
- **Encryption:** AES 256-bits.
- **Team Budget:** $300 (for all hardware and ancillary costs).

## My Contributions
- Developed and trained the machine learning model for image identification and vulnerability detection.
- Built the complete frontend & backend of the mobile application for image display and download.
- Implemented AWS server integration and image storage pipeline.

## Security and Ethics
- All transmissions are encrypted using strong algorithms to prevent interception.
- No prohibited or invasive techniques are used to identify images.
