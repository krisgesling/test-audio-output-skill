from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.audio import wait_while_speaking
from mycroft.util import play_wav, play_mp3, play_ogg
from os.path import dirname, join, realpath


class TestAudioOutput(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.audio_dir = dirname(realpath(__file__))

    @intent_handler(IntentBuilder('wav.output.test').require('wav')
                    .require('test').require('output'))
    def handle_wav_output_test(self, message):
        self.speak_dialog('playing', {'type': 'wav'})
        wait_while_speaking()
        play_wav(join(self.audio_dir, 'audio_test.wav'))

    @intent_handler(IntentBuilder('mp3.output.test').require('mp3')
                    .require('test').require('output'))
    def handle_mp3_output_test(self, message):
        self.speak_dialog('playing', {'type': 'mp3'})
        wait_while_speaking()
        play_mp3(join(self.audio_dir, 'audio_test.mp3'))

    @intent_handler(IntentBuilder('ogg.output.test').require('ogg')
                    .require('test').require('output'))
    def handle_ogg_output_test(self, message):
        self.speak_dialog('playing', {'type': 'ogg'})
        wait_while_speaking()
        play_ogg(join(self.audio_dir, 'audio_test.ogg'))


def create_skill():
    return TestAudioOutput()
