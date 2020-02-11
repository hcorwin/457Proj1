import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():

    authorizer = DummyAuthorizer()

    authorizer.add_user('user', '123', '/Users/corwi', perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "Why hello there."

    server = FTPServer(("127.0.0.1", 21), handler)

    server.serve_forever()

if __name__ == '__main__':
    main()
