# First, install the pillow library if you haven't already:
# pip install pillow

from PIL import Image

def display_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Display the image using the system's default viewer
        img.show()
        print("Image displayed successfully!")
        
    except FileNotFoundError:
        print(f"Error: The file at {image_path} could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'radha_krishna.jpg' with the actual path to your downloaded image
display_image("radha_krishna.jpg")
