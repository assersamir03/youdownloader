import os
import pytube
import time
def startvid():
    yt = pytube.YouTube(str(input("Enter the video link: ")))
    print("is that your vid?y/n " + yt.title)
    checkk = str(input()).capitalize()

    def downloadvid():
        res = int(input("high RES 1: \nlow RES 2: "))
        if res == 1:
            video = yt.streams.get_highest_resolution()
            Dir = input(
                f"*note if you leave it blank the download location will be {os.getcwd()}\nenter the Dir: ") or "."
            downloadd = video.download(output_path=Dir)
            base, ext = os.path.splitext(downloadd)
            newFile = base + f'_{yt.title}.mp4'
            os.rename(downloadd, newFile)
        elif res == 2:
            video = yt.streams.get_lowest_resolution()
            Dir = input(
                f"*note if you leave it blank the download location will be {os.getcwd()}\nenter the Dir: ") or "."
            downloadd = video.download(output_path=Dir)
            base, ext = os.path.splitext(downloadd)
            newFile = base + f'_{yt.title}.mp4'
            os.rename(downloadd, newFile)
        else:
            print("unavailable")
        repeat = input('do you want to download anything ealse? y/n: ').capitalize()
        if repeat == 'Y':
            startvid()
        elif repeat == 'N':
            print("ok HF <3")
            time.sleep(5)
        else:
            print("fuck you")

    if checkk == "Y":
        downloadvid()
    elif checkk == "N":
        startvid()
    else:
        print("unavailable")
startvid()