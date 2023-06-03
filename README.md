# Image Watermark Adder

## Introduction
The Image Watermark Adder is a Python script that allows users to add a watermark to an image. It provides a graphical user interface (GUI) for uploading an image, adding a watermark, and saving the watermarked image.

## Features
- Open and display an image file from the local computer.
- Resize the displayed image while maintaining the aspect ratio.
- Add a watermark to the image.
- Position the watermark in the center of the image.
- Save the watermarked image to a user-specified location.
- Automatically generate a default filename for the watermarked image.
- Clear the displayed image and buttons after saving.

## Usage
1. Run the script in a Python environment.
2. Click the "Choose File" button to select an image from your computer.
3. The selected image will be displayed in the window.
4. Click the "Add watermark" button to add a watermark to the image.
5. The watermarked image will replace the original image.
6. Click the "Save" button to save the watermarked image.
7. A file dialog will open, allowing you to choose the save location and filename.
8. By default, the filename will be "original_filename_watermarked.jpg".
9. After saving, the displayed image and buttons will be cleared.
10. You can repeat the process to add a watermark to another image.

## Dependencies
The following dependencies are required to run the script:
- Python (version 3.6 or higher)
- PIL (Python Imaging Library)
- tkinter (Python interface to the Tk GUI toolkit)
