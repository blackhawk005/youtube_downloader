from pytube import YouTube
import os


def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path

n = {}

def link_entry(link):
    yt = YouTube(link)
    videos = yt.streams
    print(yt.title)
    return videos



videos = link_entry("https://youtu.be/4R9DJxjmSCk")

video = list(enumerate(videos))
print(video)
def selections(n):
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
        new_v = str(i+1) + ")" + ' Format: '+ "\"" + n['mime_type'] + ' resolution:', n['res'] + ' fps:', n['fps'] + ' type:', n['type']
        print(new_v)



selections(n)
print(n)
print("Enter the desired option to download the format")
dn_option = int(input("Enter the option: "))

def downloads(dn_options):
    dn_video = videos[dn_option-1]
    file_size = dn_video.filesize

    dn_video.download(file_path())
    return file_size



filesize = downloads(dn_option)

print("Downloaded successfully")