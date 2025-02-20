from core.routes.server import ServerConfig, app
import os

from core.utils.downloader import downloadModelFile

downloadModelFile()

if __name__ == '__main__':
    app.run(debug=True, host=ServerConfig.HOST.value, port=ServerConfig.PORT.value)