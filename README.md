# File-vault
A face recognition desktop app created in python to protect your private files and directories by generating a user's face id and if matches it'll open the file.

## Dependencies for usage:
  1. Python 3.0 or plus.
  2. face_recognition library from python.org and all its dependencies
  3. import PIL to open the image.

## &#9432; Instructions for usage:
 
 ### **Step 1:**
  First user need to add their photo in the face_db which is considered as the dataset in this project.
  Import all necessary packages using the command :-
  ```
  pip install face-recognition
  pip install opencv-python
  pip install pillow
  ```
  Run the api.py file and this file starts encoding the image that you saved in the face_db folder and creates a
  encode.pickle file in the face_db folder.
  > &#9432; Note:
  > Don't run the api.py file after it encoded the photo.
  
 ### **Step 2:**
   After step 1 is over , now open the OpenImg.py file check if any errors occur by giving a file path of an image in 
   the commented set of codes and   if it runs successfully undo all your changes and comment the lines that were     
   commented before.    

### **Step 3:**  
   Now open the lock.py file and pass the file path of the image as an argument to the function 
   `d.open_image(image_path)`.Now run the file and the camera window pops up and if it matches the file opens or else 
   it'll throw access denied message.
   
> &#9432; Note:
>  If you find find any errors while importing any packages, kindly downgrade your python interpreter version.
  
