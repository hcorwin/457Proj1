import ftplib


def upload(ftp, filename):
    ftp.storlines("STOR " + filename, open(filename))


def download(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
    except:
        print("Error, unable to download")


def listall(ftp):
    ftp.retrlines('LIST')


def disconnect(ftp):
    ftp.quit()


def connect(ftp):
    ftp = ftplib.FTP("127.0.0.1")
    ftp.login("user", "123")
