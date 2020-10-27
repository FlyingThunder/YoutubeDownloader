import youtube_dlc
from audioclipextractor import AudioClipExtractor
from PyQt5 import QtWidgets
import Output
import sys
import os

ffmpegpath = "C:/Users/laure/PycharmProjects/YoutubeDownloader/ffmpeg.exe"

class youtubeDownloader(QtWidgets.QMainWindow, Output.Ui_MainWindow):
    def __init__(self, parent=None):
        super(youtubeDownloader, self).__init__(parent)
        self.setupUi(self)
        self.button_download.clicked.connect(lambda: self.add_youtubeaudio(url=self.textbox_url.toPlainText(), start=self.textbox_start.toPlainText(), end=self.textbox_end.toPlainText(), file=self.textbox_filename.toPlainText()))

    def add_youtubeaudio(self, url, start=None, end=None, file=None):
        ydl_opts = {

            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            video_info = (ydl.extract_info(url))['id']
            for x in os.listdir(os.curdir):
                print(x)
                if str(video_info)+".mp3" in x:
                    videokeep = x
            if start and end:
                ext = AudioClipExtractor(str(videokeep), ffmpegpath)
                specs = str(start) + " " + str(end)
                ext.extract_clips(specs)
                os.rename('clip1.mp3',str(file)+".mp3")
            else:
                os.rename(videokeep, str(file)+".mp3")

        if self.checkBox_deletevid.isChecked():
            try:
                os.remove(videokeep)
            except:
                pass

        self.textBrowser_Output.setPlainText("{} wurde heruntergeladen".format(file))


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = youtubeDownloader()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()