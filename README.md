# DJI RoboMaster EP Core Project

This repository contains an old and incomplete code from a university project. Unfortunately, the full code is missing, and I couldn't locate it anywhere.

## Project Overview

This project involved programming a modified DJI RoboMaster EP Core using a Python API. The main objectives were:

1. **Person Following**: The robot was designed to follow a person wearing a warning vest. Due to the challenges in recognizing a person from the back, we relied on the vest's color for tracking. By applying specific filters, we could reliably detect the color, and based on the height of the vest in the camera's view, determine the distance to the person.

2. **Tooling Bits Detection**: We used a similar color-based approach to locate tooling bits painted in distinct colors. The robot needed to accurately approach these bits and collect them using an electromagnet. This required precise positioning directly in front of the bits for successful collection and sorting.

Despite the limitations of DJI's API and several internal functions not working correctly, the project was successful. Below is an image of the modified RoboMaster. 

![RoboMaster Modification](link-to-image) 

*Note: I was responsible for all coding and some CAD parts. My team handled the construction, presentations, and other tasks.*

 
