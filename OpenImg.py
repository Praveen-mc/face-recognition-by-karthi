from PIL import Image

def open_image(file_path):
    try:
        image = Image.open(file_path)
        image.show()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    image_path = "C:\\Users\\LENOVO\\Desktop\\sample\\face-recognition-vault\\have a good day project.png"  # Replace with the actual path to your image file
    open_image(image_path)
