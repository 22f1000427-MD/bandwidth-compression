
from PIL import Image, ImageDraw

# Create a blank transparent image (500x500)
img = Image.new("RGBA", (500, 500), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw rectangles (manually extracted from visual observation)
draw.rectangle([10, 400, 110, 500], fill=(0, 0, 255, 153))   # Blue rectangle
draw.rectangle([380, 400, 480, 500], fill=(0, 128, 0, 153))  # Green rectangle
draw.rectangle([380, 480, 480, 580], fill=(255, 0, 0, 153))  # Red rectangle

# Save reconstructed image
img.save("/mnt/data/reconstructed_image.png")
