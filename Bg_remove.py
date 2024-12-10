from rembg import remove
from PIL import Image
import io
'''Change this code I was working with multiple file so I looped you can remove it if you only want to
remove background of one file'''

for i in range(4,8):
    input_path = f'un/slider{i}.webp'
    output_path = f'rm/slider{i}.webp'

    # Open the image
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()

    # Remove background
    output_data = remove(input_data)

    # Save the output image
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)
