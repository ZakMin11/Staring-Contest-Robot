# Staring Contest Robot

A fun interactive robot that uses computer vision to track faces and fires a Nerf gun when it detects the player blinking.

## Overview

This project combines Python-based face tracking with Arduino-controlled Nerf gun automation. The system watches the player's face through a webcam and waits for them to blink. When a blink is detected, it triggers the Arduino to activate the Nerf gun mechanism.

## Features

- Real-time face and eye tracking
- Blink detection
- Automated Nerf gun firing mechanism
- Serial communication between Python and Arduino
- Live video feed with detection visualization

## Hardware Requirements

- Webcam
- Arduino board (configured for /dev/cu.usbmodem1411)
- Nerf gun with servo/motor modification
- USB cable for Arduino connection
- Basic electronic components (LEDs, resistors, etc.)

## Software Requirements

- Python 3.x
- OpenCV (cv2)
- pyserial
- Arduino IDE
- Required Cascade Classifiers:
  - haarcascade_frontalface.xml
  - haarcascade_eye.xml

## Installation

1. Clone this repository
2. Install Python dependencies:
```bash
pip install opencv-python
pip install pyserial
pip install numpy
```
3. Download the required Haar cascade files
4. Upload the Arduino sketch to your board
5. Connect the Nerf gun mechanism to the specified Arduino pins

## File Structure

- `faceTracker.py`: Main Python script for face tracking and serial communication
- `sketch_aug19a.ino`: Arduino sketch for controlling the Nerf gun mechanism

## Wiring

Arduino pin configuration:
- Pin 7: Output control
- Pin 8: Output control
- Pin 5: PWM output for servo/motor control

## Usage

1. Connect the Arduino to your computer
2. Run the Python script:
```bash
python faceTracker.py
```
3. Enter commands via the input prompt ('q' to quit)
4. Face the camera and try not to blink!
5. If you blink, the system will detect it and trigger the Nerf gun

## How It Works

### Python Script (`faceTracker.py`)
- Initializes webcam and loads cascade classifiers
- Performs real-time face and eye detection
- Monitors for blinks (absence of eye detection while face is detected)
- Sends serial commands to Arduino when a blink is detected

### Arduino Sketch (`sketch_aug19a.ino`)
- Receives serial commands from Python
- Controls the Nerf gun firing mechanism using digital and PWM outputs
- Alternates between states with 1-second delays

## Customization

You can modify:
- Detection sensitivity in the `detectMultiScale` parameters
- Blink detection timing
- Serial communication port and baud rate
- Arduino pin configurations
- Firing mechanism timing and power

## Safety Considerations

- Always use appropriate Nerf darts
- Keep a safe distance from the device
- Never point at face or eyes
- Supervise children when using the system

## Future Improvements

Potential enhancements:
- Multiple player support
- Score tracking
- Adjustable difficulty levels
- Mobile app control
- Different game modes

## Authors

Zak Mineiko

## Acknowledgments

- OpenCV community
- Arduino community
- Haar Cascade developers
