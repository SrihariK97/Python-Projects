# Follow the below steps,
#Download the prerequisites using pip -> python, pytube

# 1.Create a folder in desktop Youtube_Videos
# 2.Create a python file download.py (anywhere)
# 3.Write the code in download.py file
# 4.Run the code python download.py
# 5.In Command line it will ask for the youtube link
# 6.Paste the video link and wait for the video to download.
# 7.The video will be downloaded and check the Youtube_Videos folder


from pytube import YouTube

def Download(link):
    SAVE_PATH = r"C:\Users\User\Desktop\Youtube_Videos"
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(SAVE_PATH)
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    print("You can find the downloaded video in : ",SAVE_PATH)

link = input("Enter the YouTube video URL: ")
Download(link)
