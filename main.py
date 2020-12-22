import youtube_dlc
from audioclipextractor import AudioClipExtractor
from PyQt5 import QtWidgets
import Output
import sys
import os
import datetime

ffmpegpath = "ffmpeg.exe"
sys.stdout = open("test.txt", "w", 1)
open("test.txt", "w").truncate(0)



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
            print("{} # Downloading Youtube video {}".format(datetime.datetime.now(),url))
            ydl.download([url])
            print("{} # Downloading Youtube video {} complete".format(datetime.datetime.now(),url))
            self.textBrowser_Output.setPlainText("{} wurde heruntergeladen".format(file))
            print("{} # Downloading Metadata {}".format(datetime.datetime.now(), url))
            video_info = (ydl.extract_info(url))['id']
            print("{} # Downloading Metadata {} complete".format(datetime.datetime.now(), url))
            for x in os.listdir(os.curdir):
                if str(video_info)+".mp3" in x:
                    videokeep = x
            print("{} # Checking altarnative arguments".format(datetime.datetime.now()))
            if start and end:
                print("{} # Cutting video {} from {} to {}".format(datetime.datetime.now(),url,start,end))
                ext = AudioClipExtractor(str(videokeep), ffmpegpath)
                specs = str(start) + " " + str(end)
                ext.extract_clips(specs)
                print("{} # Cutting video {} from {} to {} complete".format(datetime.datetime.now(),url, start, end))
                try:
                    print("{} # Renaming file to {}".format(datetime.datetime.now(),file))
                    os.rename('clip1.mp3',str(file)+".mp3")
                    print("{} # Renaming file to {} complete".format(datetime.datetime.now(),file))
                    self.textBrowser_Output.setPlainText("{} wurde in clip geschnitten".format(file))
                except:
                    print("{} # Output file {} already exists".format(datetime.datetime.now(),file))
                    self.textBrowser_Output.setPlainText("{} existiert bereits".format(file))
            else:
                try:
                    print("{} # Renaming file to {}".format(datetime.datetime.now(),file))
                    os.rename(videokeep, str(file)+".mp3")
                    print("{} # Renaming file to {} complete".format(datetime.datetime.now(),file))
                except:
                    print("{} # Output file {} already exists".format(datetime.datetime.now(),file))

        if self.checkBox_deletevid.isChecked():
            try:
                os.remove(videokeep)
            except:
                pass




def main():
    app = QtWidgets.QApplication(sys.argv)
    form = youtubeDownloader()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
