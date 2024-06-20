from pytube import YouTube

try :
    link = input("link : ")
    yt = YouTube(link)
    print(yt.title)
    yt.streams.first().download('./')
    print("done")
except:
    print("erreur")


