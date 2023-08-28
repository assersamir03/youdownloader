import pytube
import os
chosenFunc=int(input("what do you want to download \nsingle MP3 '1' \nA vid '2' "))

if chosenFunc==1:
    def startMp3():
        yt = pytube.YouTube(str(input("Enter the link: ")))
        print((yt.title))
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
            print("fuck you")
        repeat = input('do you want to download anything ealse? y/n: ').capitalize()
        if repeat == 'Y':
            startMp3()
        elif repeat == 'N':
            print("ok HF <3")
        else:
            print("fuck you")


    startMp3()
elif chosenFunc==2:
    def startvid():
        yt=pytube.YouTube(str(input("Enter the video link: ")))
        print("is that your vid?y/n "+yt.title)
        check=str(input()).capitalize()

        def downloadvid():
            res=int(input("high 1: \nlow 2: "))
            if res==1:
                video = yt.streams.get_highest_resolution()
                Dir = input(
                    f"*note if you leave it blank the download location will be {os.getcwd()}\nenter the Dir: ") or "."
                downloadd = video.download(output_path=Dir)
                base, ext = os.path.splitext(downloadd)
                newFile = base + f'_{yt.title}.mp4'
                os.rename(downloadd, newFile)
            elif res==2:
                video = yt.streams.get_lowest_resolution()
                Dir = input(
                    f"*note if you leave it blank the download location will be {os.getcwd()}\nenter the Dir: ") or "."
                downloadd = video.download(output_path=Dir)
                base, ext = os.path.splitext(downloadd)
                newFile = base + f'_{yt.title}.mp4'
                os.rename(downloadd, newFile)
            else:
                print("goodbye")
            repeat = input('do you want to download anything ealse? y/n: ').capitalize()
            if repeat == 'Y':
                startvid()
            elif repeat == 'N':
                print("ok HF <3")
            else:
                print("fuck you")
        if check == "Y":
            downloadvid()
        elif check == "N":
            startvid()
        else:
            print("go away")

    startvid()
else:
    print("currnetly unavilable")