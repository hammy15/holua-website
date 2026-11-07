from PIL import Image
import numpy as np

# Load image
img = Image.open('logo-holua.png').convert('RGBA')
data = np.array(img)

# The background is very light cream (255, 254, 236-239)
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# Background detection: high R, high G, high B with specific pattern
is_background = (r > 250) & (g > 250) & (b > 230)

# Set alpha to 0 for background pixels
data[:,:,3] = np.where(is_background, 0, 255)

# Save
result = Image.fromarray(data)
result.save('logo-transparent-clean.png')
print("Done - saved logo-transparent-clean.png")
