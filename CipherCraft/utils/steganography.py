# utils/steganography.py

from PIL import Image
import os

# Encode secret message into an image
def encode_image(image_path, secret_message):
    """Encode secret message into an image"""
    # Open image
    image = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    
    if len(binary_message) > image.width * image.height:
        raise ValueError("Message is too large to hide in this image.")
    
    pixels = image.load()
    index = 0
    for row in range(image.height):
        for col in range(image.width):
            pixel = list(pixels[col, row])  # Get RGB values
            if index < len(binary_message):
                pixel[0] = int(format(pixel[0], '08b')[:-1] + binary_message[index], 2)  # Modify Red channel (LSB)
                index += 1
            pixels[col, row] = tuple(pixel)
            if index >= len(binary_message):
                break
        if index >= len(binary_message):
            break
    
    # Save image with encoded message
    output_path = os.path.splitext(image_path)[0] + "_encoded.png"
    image.save(output_path)
    return output_path

# Decode secret message from an image
def decode_image(image_path):
    """Decode secret message from an image"""
    image = Image.open(image_path)
    binary_message = ''
    
    pixels = image.load()
    for row in range(image.height):
        for col in range(image.width):
            pixel = list(pixels[col, row])  # Get RGB values
            binary_message += format(pixel[0], '08b')[-1]  # Extract LSB of the Red channel
            if len(binary_message) % 8 == 0 and binary_message[-8:] == '00000000':  # End of message marker (null byte)
                break
        else:
            continue
        break
    
    # Convert binary message to string
    decoded_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message)-8, 8))
    return decoded_message
