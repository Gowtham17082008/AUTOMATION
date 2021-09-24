import os
import dropbox

class transferData:
    def __init__(self,accestoken):
        self.accestoken=accestoken

    def uploadfile(self,filesfrom,filesto):
        dbx=dropbox.Dropbox(self.accestoken)
        f=open(filesfrom,'rb')
        dbx.files_upload(f.read(),filesto)
    
def main():
    Mytoken="sl.A48ROL5g27kkt3WEQPRxBI9nL7vmXFWCwcqynctXue2FhLMrU-JRAFaDO2tqLYisydy_jtPgg6yQnCZ24oHbEod8PiGkfZaUpOcaN7yhmwWxBa_6V_RlgJjUGEoSKEVw6UMJNVs"
    mytransforedata=transferData(Mytoken)
    filefrom=input("Enter.path of the file to transfore")
    fileto=input("Enter the path of the dropbox")

    mytransforedata.uploadfile(filefrom,fileto)
    print("file is move ")
main()
