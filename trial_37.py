from pytube import YouTube
import os


def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path
def progress_Check(stream, chunk, bytes_remaining):
    # Gets the percentage of the file that has been downloaded.
    percent = (100 * (file_size - bytes_remaining)) / file_size
    print("{:00.0f}% downloaded".format(percent))

link = input("Enter your youtube url: ")
yt = YouTube(link, on_progress_callback=progress_Check)
videos = yt.streams
print()
print(yt.title)
print()
n = {}



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

dn_video.download(file_path())

print("Downloaded successfully")