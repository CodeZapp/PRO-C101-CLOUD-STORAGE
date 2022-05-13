import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    
    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):

            for fileName in files:

                localPath = os.path.join(root, fileName)

                relativePath = os.path.realpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)

                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode = WriteMode('overwrite'))

def main():
    accessToken = 'sl.BHhUaAhzHKdSg5dwgj9znxJGKVnqEQ5AKi1FbfS_C9ROzGwVJ8JI6_7o045XHTz-sNTfaek-Q8naEXDTi0ss7wfIStXkWeA2l7WfcEeWKuj9UovSMC7W24Gn-l0SObC0msBotsG4aHNz'
    TransferData = TransferData(accessToken)

    fileFrom = str(input("Enter the folder path to transfer :- "))
    fileTo = input("Enter the full path to upload to dropbox :- ")

    TransferData.uploadFile(fileFrom, fileTo)
    print("File has been moved !!!")

main()