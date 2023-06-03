import os
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename  # Allows user to open a file.
from tkinter.ttk import *


def save_image():
    """
    Lets the user save the watermarked image to a file.
    :return: None
    """
    global current_image, image_path, watermark_added, save_button, add_watermark

    if current_image and image_path:
        # Get the current image from the Label widget.
        image_tk = current_image.image

        # Convert the PhotoImage object to a PIL Image object.
        image = ImageTk.getimage(image_tk)

        # Convert the image to RGB mode if it has an alpha channel.
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # Extract the original filename without the extension.
        original_filename = os.path.splitext(os.path.basename(image_path))[0]

        # Prompt the user to choose the save location and filename.
        default_filename = original_filename + "_watermarked"
        save_path = asksaveasfilename(defaultextension=".jpg",
                                      initialfile=default_filename,
                                      filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
                                      )

        if save_path:
            # Save the image with the user-specified filename and location.
            image.save(save_path)

            # Clear the displayed image.
            current_image.destroy()
            current_image = None

            # Destroy the "Add watermark" and "Save" buttons.
            add_watermark.destroy()
            add_watermark = None
            save_button.destroy()
            save_button = None

            # Reset the watermark_added flag.
            watermark_added = False

            # Clear the image_path.
            image_path = None


def add_water_mark():
    """
    Adds a watermark to the displayed image.
    :return: None
    """
    global current_image, watermark_added, save_button

    if current_image and not watermark_added:
        # Get the current image from the Label widget.
        image_tk = current_image.image

        # Convert the PhotoImage object to a PIL Image object.
        image = ImageTk.getimage(image_tk)

        # Create a copy of the image to apply the watermark.
        watermarked_image = image.copy()

        # Open the watermark image.
        watermark = PIL.Image.open("watermark.png")

        # Calculate the maximum dimensions for the watermark.
        max_width, max_height = 300, 300

        # Resize the watermark image while maintaining the aspect ratio.
        watermark.thumbnail((max_width, max_height))

        # Calculate the watermark position.
        watermark_width, watermark_height = watermark.size
        image_width, image_height = image.size

        # Calculate the centered position for the watermark.
        watermark_position = ((image_width - watermark_width) // 2, (image_height - watermark_height) // 2)

        # Paste the watermark onto the image.
        watermarked_image.paste(watermark, watermark_position, mask=watermark)

        # Convert the watermarked image back to a PhotoImage object.
        watermarked_image_tk = ImageTk.PhotoImage(watermarked_image)

        # Update the image in the Label widget.
        current_image.configure(image=watermarked_image_tk)
        current_image.image = watermarked_image_tk

        # Set the watermark_added flag to True
        watermark_added = True


def open_file():
    """
    Lets the user open a file from local pc.
    :return: None
    """
    file_path = askopenfilename(filetypes=[('Image Files', '*.jpg *.jpeg *.png *.avif')])
    global current_image, add_watermark, watermark_added, image_path, save_button
    if file_path:
        with open(file_path, 'rb') as file:
            try:
                image = PIL.Image.open(file)

                # Calculate the dimensions while maintaining the aspect ratio
                width, height = image.size
                if width > height:
                    new_width = 300
                    new_height = int((height / width) * new_width)
                else:
                    new_height = 300
                    new_width = int((width / height) * new_height)

                # Resize the image
                image = image.resize((new_width, new_height))

                # Convert the image to a PhotoImage object
                image_tk = ImageTk.PhotoImage(image)

                # Create a Label widget to display the image
                if current_image:
                    # If there is a previously displayed image, destroy it.
                    current_image.destroy()

                current_image = Label(window, image=image_tk)
                current_image.pack()

                # Keep a reference to the image to prevent it from being garbage collected.
                current_image.image = image_tk

                # Reset the watermark flag.
                watermark_added = False

                # Get the image path.
                image_path = file_path

                # Create the "Add watermark" button.
                add_watermark = Button(window, text="Add watermark", command=add_water_mark)
                add_watermark.pack()

                # Create the "Save" button.
                save_button = Button(window, text="Save", command=save_image)
                save_button.pack()

            except Exception as e:
                print(e)


# Window initialization.
FONT = ("Arial", 10, "bold")
window = Tk()
window.title("Image water mark adder")
window.geometry('600x600')

# Global variables.
current_image = None  # Keep track of current image.
watermark_added = False  # Keep track if watermark has been added.
image_path = None  # Keep the image path.
save_button = None
add_watermark = None

# Label
image_label = Label(window, text='Upload Image', font=FONT)
image_label.pack()

# Choose Image Button
image_button = Button(window, text='Choose File', command=open_file)
image_button.pack(pady=25)

if __name__ == "__main__":
    window.mainloop()
