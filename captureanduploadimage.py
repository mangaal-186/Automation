import cv2
import time
import dropbox
import random
def take_snapshot():
    number=random.randint(0,100)
    #initializing cv2
    VideoCapture=cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera on is on
        ret,frame=VideoCapture.read()
        img_name='img'+str(number)+'.png'
        cv2.imwrite (img_name,frame)
        start_time = time.time
        #cv2.imwrite()method is used to save an image to any storage device 
     
        result= False


    return img_name

    print('snapshot taken')
        #releases the camera 
    VideoCapture.release()
        #closes all the windows that might be opened while the process is on 
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.A-VFaphILHNnxcB_CjFXTCeGwE2sQPerkJ8W_W7R2PdESuGHwIcGGKlYNm73PM7ZznDCQnbNIc7hQ8mCpmDySNDR_FhNpgPlUqZs3khSJLE9GQtd7bW91YRXra14mhuYWWvSg9E "
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time)>=5):
            name=take_snapshot()
            upload_file(name)
    
main()



