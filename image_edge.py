from images import Image

def detect_edges(image, edge_threshold=30):
    def to_grayscale(pixel):
        return sum(pixel) // 3  

    edged_image = image.clone()
    img_width, img_height = image.getWidth(), image.getHeight()

    for y in range(1, img_height - 1):
        for x in range(1, img_width - 1):
            current_pixel = to_grayscale(image.getPixel(x, y))
            right_pixel = to_grayscale(image.getPixel(x + 1, y))
            below_pixel = to_grayscale(image.getPixel(x, y + 1))

            edge_strength = abs(current_pixel - right_pixel) + abs(current_pixel - below_pixel)

            new_pixel_color = (255, 255, 255) if edge_strength > edge_threshold else (0, 0, 0)
            edged_image.setPixel(x, y, new_pixel_color)

    edged_image.draw()
    return edged_image

image_path = input("Enter image path: ")
input_image = Image(image_path)
output_image = detect_edges(input_image, edge_threshold=30)
