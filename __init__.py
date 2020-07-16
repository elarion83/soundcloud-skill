from mycroft import MycroftSkill, intent_file_handler


class Soundcloud(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('soundcloud.intent')
    def handle_soundcloud(self, message):
        self.speak_dialog('soundcloud')
  tracklist = []
        self.vid_url = 'https://soundcloud.com/thoms-12/ebrius'
        self.stream_url = self.get_stream_url(self.vid_url)
        LOG.debug('Found stream URL: on souncdloud')
        LOG.debug('Media title: ' + 'I will enjoy you my bro')

        tracklist.append(self.stream_url)
        self.mediaplayer.add_list(tracklist)
        self.audio_state = 'playing'
        self.speak_dialog('now.playing', {'content': 'some soundcloud music'} )
        wait_while_speaking()
        self.mediaplayer.play()


    def get_stream_url(self, youtube_url):
        abs_url = youtube_url
        LOG.debug('pafy processing: ' + abs_url)
        streams = pafy.new(abs_url)
        LOG.debug('audiostreams found: ' + str(streams.audiostreams));
        bestaudio = streams.getbestaudio()
        LOG.debug('audiostream selected: ' + str(bestaudio));
        return bestaudio.url


def create_skill():
    return Soundcloud()

