from images import Image

def blur(image, blur_radius):

    def compute_average_color(pixel_list):
        red, green, blue = zip(*pixel_list)
        return sum(red) // len(pixel_list), sum(green) // len(pixel_list), sum(blue) // len(pixel_list)

    blurred_image = image.clone()
    img_width, img_height = image.getWidth(), image.getHeight()

    for y in range(blur_radius, img_height - blur_radius):
        for x in range(blur_radius, img_width - blur_radius):
            surrounding_pixels = [
                image.getPixel(x_offset, y_offset)
                for x_offset in range(x - blur_radius, x + blur_radius + 1)
                for y_offset in range(y - blur_radius, y + blur_radius + 1)
            ]
            new_pixel_value = compute_average_color(surrounding_pixels)
            blurred_image.setPixel(x, y, new_pixel_value)

    blurred_image.draw()
    return blurred_image

image_path = input("Enter image path: ")
original_image = Image(image_path)
blurred_result = blur(original_image, blur_radius=3)
