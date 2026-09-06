from PIL import Image, ImageDraw

input_image = "monalisa.jpg"
val = 40

original = Image.open(input_image).convert("RGB")
width, height = original.size

new_image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(new_image)

for y in range(0, height, val):
    for x in range(0, width, val):
        pixal = original.getpixel((x, y))
        draw.ellipse(
            (x - val // 2, y - val // 2, x + val // 2, y + val // 2),
            fill=pixal
        )
new_image.save("output.jpg")
