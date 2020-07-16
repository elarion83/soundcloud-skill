from mycroft import MycroftSkill, intent_file_handler


class Soundcloud(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('soundcloud.intent')
    def handle_soundcloud(self, message):
        self.speak_dialog('soundcloud')


def create_skill():
    return Soundcloud()

