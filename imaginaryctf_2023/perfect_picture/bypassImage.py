from PIL import Image

# Create an image with the required dimensions (690x420)
bypass_image = Image.new('RGBA', (690, 420), (255, 255, 255, 255))

# Set the required pixels to bypass the checks
bypass_image.putpixel((412, 309), (52, 146, 235, 123))
bypass_image.putpixel((12, 209), (42, 16, 125, 231))
bypass_image.putpixel((264, 143), (122, 136, 25, 213))

# Save the bypass image
bypass_image.save('bypass_image.png')

# Set metadata using ExifTool
import subprocess

metadata_commands = [
    'exiftool', '-PNG:Description=jctf{not_the_flag}',
    '-PNG:Title=kool_pic', '-PNG:Author=anon', 'bypass_image.png'
]

subprocess.run(metadata_commands)

print("Bypass image created and metadata set.")
