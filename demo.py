import png, array
from numpy.random import random


matrix = random((12,12))


point = (2, 10) # coordinates of pixel to be painted red

reader = png.Reader(filename='image.png')
w, h, pixels, metadata = reader.read_flat()
pixel_byte_width = 4 if metadata['alpha'] else 3
pixel_position = point[0] + point[1] * w
new_pixel_value = (255, 0, 0, 0) if metadata['alpha'] else (255, 0, 0)
pixels[
  pixel_position * pixel_byte_width :
  (pixel_position + 1) * pixel_byte_width] = array.array('B', new_pixel_value)

output = open('image-with-red-dot.png', 'wb')
writer = png.Writer(w, h, **metadata)
writer.write_array(output, pixels)
output.close()
