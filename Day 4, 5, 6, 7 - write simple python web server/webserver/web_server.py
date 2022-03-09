""" simple web server """

import time
from http.server import HTTPServer

from server import Server


def main():
    HOST = "localhost"
    PORT = 8080
    httpd = HTTPServer((HOST, PORT), Server)
    print(f'{time.asctime()} Server Start on http://{HOST}:{PORT}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStoping webserver...')
    httpd.server_close()
    print(f'{time.asctime()} webserver is stopped.')


if __name__ == "__main__":
    main()
