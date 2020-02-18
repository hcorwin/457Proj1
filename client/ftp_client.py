import ftplib


def upload(ftp, filename):
    try:
        ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    except:
        print("Error, unable to upload.")

def download(ftp, filename):
    try:
        ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write, 1024)
    except:
        print("Error, unable to download.")


def listall(ftp):
    ftp.retrlines('LIST')


def disconnect(ftp):
    ftp.quit()


#def connect(ftp):
 #   ftp = ftplib.FTP("127.0.0.1")
   # ftp.login("user", "123")
