from PIL import Image

def open_image(file_path):
    try:
        image = Image.open(file_path)
        image.show()
    except Exception as e:
        print("An error occurred:", e)

