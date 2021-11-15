from PIL import Image, ImageOps, ImageFilter, ImageDraw
import math

def getRGB(RGBint):
    return int((RGBint << 21) + (RGBint << 10) + RGBint * (math.pi*math.pi))


w, h = 569, 438
bitmap = Image.new("RGB", (w * 2, h * 2), "black")

cX, cY = -0.750357820200574, 0.047756163825227
px = bitmap.load()

for i in range(w * 2):
    for j in range(h * 2):

        zx = (i - w) / w
        zy = (j - h) / h
        c = w
        while c != 0 and zx * zx + zy * zy < 4:
            aux = zx * zx - zy * zy + cX
            zy = 2.0 * zx * zy + cY
            zx = aux
            c = c - 1

        px[i, j] = getRGB(c)

bitmap.save('mig.png')

im1 = Image.open('logo_hack.png').resize((w * 2, h * 2)).filter(ImageFilter.EDGE_ENHANCE_MORE).filter(ImageFilter.SMOOTH)
im = Image.composite(ImageOps.invert(bitmap), ImageOps.invert(Image.composite(ImageOps.invert(bitmap), Image.new("RGB", (w * 2, h * 2), "black"), Image.new("L", im1.size, 40))), im1)

draw = ImageDraw.Draw(im)
draw.rectangle((0, 0, (w * 2, h * 2)), width=42, outline='black')
draw.rectangle((0, 0, (w * 2, h * 2)), width=27, outline='white')
result = ImageOps.invert(im).filter(ImageFilter.EDGE_ENHANCE_MORE).filter(ImageFilter.SMOOTH).save('result.png')
