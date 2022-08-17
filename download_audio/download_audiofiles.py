import requests 

audio_url = 'https://musify.club/track/dl/4645538/hooverphonic-mad-about-you.mp3'
def download_audio(url = ''):
    try:
        response = requests.get(url=url)
        with open('new_song.mp3','wb') as audio:
            audio.write(response.content)
    except Exception as ex:
        return 'Check the url-address please'

video_url = 'https://www.youtube.com/watch?v=xVKGXgHDMvQ'
def download_video(url = ''):
    try:
        response = requests.get(url=url)
        with open('new_video.mp4','wb') as video:
            video.write(response.content)
    except Exception as ex:
        return 'Check the url-address please'

def main():
    print(download_audio(url=audio_url))
    print(download_video(url=video_url))

if __name__=='__main__':
    main()
