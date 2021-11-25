import cv2
import dropbox
def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        print(ret)
        cv2.imwrite("newpicture.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)



#take_snapshot()#how to take photos








def send_to_dropbox(nameOfFile):
    access_token = 'jZJ0mZ32y00AAAAAAAAAAQwRJ7srQk2SFrWaR2UufO6HvgVhx_saD4kpF7nTeb8q'
    transferData = TransferData(access_token)

    file_from = nameOfFile
    file_to = '/test_dropbox/'+nameOfFile # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

n= True
while(n):
    if __name__ == '__main__':
        send_to_dropbox(input("name of file: "))
    y=input("would you like to continue y/n?: ")
    if(y=="y"):
        n=True
    else:
        n= False