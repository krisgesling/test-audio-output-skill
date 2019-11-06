from mycroft import MycroftSkill, intent_file_handler


class TestAudioOutput(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('output.audio.test.intent')
    def handle_output_audio_test(self, message):
        self.speak_dialog('output.audio.test')


def create_skill():
    return TestAudioOutput()

