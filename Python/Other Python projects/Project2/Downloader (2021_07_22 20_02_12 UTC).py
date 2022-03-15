from pytube import YouTube

i2 = "Y"
while i2.upper() == 'Y':
    i2 = input("Do you want to download a Video [Y]es or [N]o:")
    if i2.upper() == "Y":
        link = input("Enter Link Here:")

        yt = YouTube(link)

        i = 1

        all_videos = yt.streams
        for x in all_videos:
            print(str(i) + "  " + str(x))
            i += 1

        video_number = int(input("Which Video Would you like to download?"))
        video_download = all_videos[video_number - 1]

        path = input("Where would you like to download the video? (Give Proper Path):")

        video_download.download(path)

        print("Your Video is Downloaded")

    elif i2.upper() == 'N':
        print("Ok")

    else:
        print("Please Type in Y or N")
        i2 = input("Do you want to download a Video [Y]es or [N]o:")
