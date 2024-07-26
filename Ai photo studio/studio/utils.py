import random
import string
from io import BytesIO
from django.core.files import File
from PIL import Image
from deepface import DeepFace

def getEventKey():
    # generations numbers 0-9 and alphas A-Z a-z
    alphabets = list(string.ascii_letters)
    numerics = list(string.digits)

    # gettings random 3 chars and 4numbrs for id
    letters = [random.choice(alphabets) for x in range(3)]
    numbers = [random.choice(numerics) for i in range(4)]

    #genrating of id
    id = letters+numbers
    random.shuffle(id)
    id = ','.join(id)
    id = id.replace(',','')
    return str(id) 


def compressImage(image):
    #creating a bytesio 
    im_io = BytesIO()

    #opening a image 
    img = Image.open(image)
    
    #convert it into RGB 
    img = img.convert('RGB')

    #saving this into bytesio
    img = img.save(im_io , 'JPEG' , optimize=True , quality=30)

    #creating django object for ORM
    comp_img = File(im_io , name=image.name)

    return comp_img




#compare two faces using deepface model


def compareFaces(target_img , input_img):
    model = "ArcFace"

    target_image = target_img
    Scaning_image = input_img

    Verfiying = DeepFace.verify(target_image, Scaning_image, model)

    #print(Verfiying["verified"])

    if Verfiying["verified"]:
        print("They are same")
        return True
    else:
        print("They are diffrent")
        return False


    