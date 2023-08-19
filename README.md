# File-vault
A face recognition desktop app created in python to protect your private files and directories by generating a user's face id and if matches it'll open the file.

## Dependencies for usage:
  1. Python 3.0 or plus.
  2. face_recognition library from python.org and all its dependencies
  3. import PIL to open the image.

## Instructions for usage:
 
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
   After step 1 is over , now open the OpenImg.py file and add the file path of an image that you want to
   hide. And run the file.  

### **Step 3:**  
   Now run the lock.py file and the camera window pops up and if it matches the file opens or else it'll throw access     denied message.
   
> &#9432; Note:
>  If you find find any errors while importing any packages, kindly downgrade your python interpreter version.
  
