import requests 
import tkinter as tk

def main():
    print(download_audio(url=url_audio_entry))



# video_url = input()
# 'https://www.youtube.com/watch?v=xVKGXgHDMvQ'
# def download_video(url = ''):
#     try:
#         response = requests.get(url=url)
#         with open('new_video.mp4','wb') as video:
#             video.write(response.content)
#     except Exception as ex:
#         return 'Check the url-address please'

window = tk.Tk()

window.title('window download')
window.geometry('400x200')
window['bg'] = 'lightgray'
url_audio_page = tk.Label(text='url address for audio',font='Consolas 10 bold')
url_audio_page.grid(column=0, row=2)
url_video_page = tk.Label(text='url address for video',font='Consolas 10 bold')
url_video_page.grid(column=0, row=5)

url_audio_entry = tk.Entry()
url_audio_entry.grid()
url_video_entry = tk.Entry()
url_video_entry.grid()

url_audio_page_text = url_audio_entry.grid(column =1,row =2)
url_video_page_text = url_video_entry.grid(column =1,row =5)

btn1 = tk.Button(window, text="download",background='lightgreen', command=lambda: download_audio(url_audio_entry.get()))  
btn1.grid(column=2, row=2) 
btn2 = tk.Button(window, text="download",background='lightblue', command=lambda: lib(url_video_entry.get()))  
btn2.grid(column=2, row=5)

window.mainloop()

def download_audio(url = ''):
    try:
        response = requests.get(url=url_audio_entry)
        with open('new_song.mp3','wb') as audio:
            audio.write(response.content)
    except Exception as ex:
        return 'Check the url-address please'

if __name__=='__main__':
    main()