import pytube
import os
import time
def startMp3():
    yt = pytube.YouTube(str(input("Enter the link: ")))
    print(yt.title)
    check = input("is that your vid? y/n: ").capitalize()
    def download():
        audio = yt.streams.filter(only_audio=True).first()
        Dir = str(input(
            f"*note if you leave it blank the download location will be {os.getcwd()}\nenter the Dir: ")) or "."
        downloadd = audio.download(output_path=Dir)
        base, ext = os.path.splitext(Dir)
        newFile = base + f'{yt.title}.mp3'
        os.rename(downloadd, newFile)

    if check == "Y":
        download()
    elif check == "N":
        startMp3()
    else:
        print("unavailable")
    repeat = input('do you want to download anything eals? y/n: ').capitalize()
    if repeat == 'Y':
        startMp3()
    elif repeat == 'N':
        print("ok HF <3")
        time.sleep(5)
    else:
        print("unavailable")

startMp3()