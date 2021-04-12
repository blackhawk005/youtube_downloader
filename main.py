from pytube import YouTube
from pytube.cli import on_progress
import os
from tqdm import tqdm
import time

n = {}

def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path
def progress_Check(stream, chunk, bytes_remaining):
    # Gets the percentage of the file that has been downloaded.
    percent = (100 * (file_size - bytes_remaining)) / file_size
    print("{:00.0f}% downloaded".format(percent))


link = input("Enter youtube url: ")
yt = YouTube(link)
videos = yt.streams
print()
print(yt.title)
print()




video = list(enumerate(videos))

for i in range(len(videos)):
    x = str(videos[i])[19:]
    y = x.split()
    for j in range(len(y)):
        z = y[j].split('=')
        if z[0]=='mime_type':
            z_1 = z[1].split('/')
            n[z[0]] = z_1[1]
        elif z[0] == 'type':
            new_var = z[1].rstrip(z[1][-1])
            n[z[0]] = new_var
        else:
            n[z[0]] = z[1]
    # print(n)
    print(str(i+1) + ")" , ' Format: '+ "\"" + n['mime_type'] + ', resolution:', n['res'] + ', fps:', n['fps'] + ', type:', n['type'] )

# print(n)
print("Enter the desired option to download the format")
dn_option = int(input("Enter the option: "))

dn_video = videos[dn_option-1]
file_size = dn_video.filesize
# dn_video.download(file_path())

# def download():
#     dn_video.download(file_path())
#     print("Downloaded successfully")
#
# t1 = threading.Thread(target=download)
# t1.start()
#
for i in tqdm(range(int(20))):
    dn_video.download(file_path())
    time.sleep(0.5)

print("Downloaded successfully")

