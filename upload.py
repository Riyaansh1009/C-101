import dropbox
from dropbox.files import WriteMode 
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(),fileTo,mode= WriteMode('overwrite'))

def main():
    access_token = 'sl.Ayz4zV_tPxpZI8xpKnyyTF6UuDY2KUU66xIaqGPtSVcAQiJcuFrba2rvTzua7ge7X-EVxmYC7ZhMKk9ZdrrIgEFTcYDs9NoWSpX-9u7pp37erh2gdqdYwjJVXimepQFg74HUPus'
    x = TransferData(access_token)
    fileFrom = 'notes.txt'
    fileTo = '/dummy/notes.txt'

    # fileFrom = input("Enter file path to transfer to dropbox")
    # fileTo = input("Enter file path to transfer to what folder in dropbox?")

    x.upload(fileFrom,fileTo)
    print("File has been moved to dropbox")

main()





        


        
