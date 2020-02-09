from PIL import  Image
import face_recognition

image_of_bill = face_recognition.load_image_file('simon-cowell.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unkown_image = face_recognition.load_image_file('face.jpg')
unknown_face_encoding = face_recognition.face_encodings(unkown_image)[0]

results = face_recognition.compare_faces([bill_face_encoding], unknown_face_encoding)


if results[0]:
    print('This true')
else:
    print('This false')

def GetFacesLocations(rawimage):
    return face_recognition.face_locations(image)

#3
image = face_recognition.load_image_file('friends.jpg')
face_locations = GetFacesLocations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    pil_image.save(f'tmp/{top}.jpg')
print(face_locations)