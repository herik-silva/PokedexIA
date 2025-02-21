from core.routes.server import ServerConfig, app
import os

from core.utils.downloader import downloadModelFile

downloadModelFile()

port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(debug=False, host=ServerConfig.HOST.value, port=port)