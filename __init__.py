from mycroft import MycroftSkill, intent_file_handler


class Mixedspeechled(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mixedspeechled.intent')
    def handle_mixedspeechled(self, message):
        self.speak_dialog('mixedspeechled')


def create_skill():
    return Mixedspeechled()

