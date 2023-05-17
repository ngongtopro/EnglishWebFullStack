from pytube import YouTube


class YtDownloader:

    def __init__(self):
        self.link = input('Parse link: ')
        self.video = None
        self.videos = None
        self.option = None

    def get_video(self):
        yt = YouTube(self.link)
        self.videos = yt.streams
        self.video = list(enumerate(self.videos))
        for i in self.video:
            print(i)

    def choose_option(self):
        self.option = int(input('Option: '))

    def download(self):
        dl_video = self.videos[self.option]
        dl_video.download()
        print('Success')


if __name__ == '__main__':
    youtube = YtDownloader()
    youtube.get_video()
    youtube.choose_option()
    while youtube.option != -1:
        youtube.download()
        print('Choose another option or -1 to exit')
        youtube.choose_option()
    print('Exit')

