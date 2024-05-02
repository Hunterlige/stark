def extract_patch(image, box):
    x1, y1, x2, y2 = box
    return image.crop((x1, y1, x2, y2))
