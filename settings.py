from talon import app, actions

def disable_speech_on_start():
    actions.speech.disable()

app.register("ready", disable_speech_on_start)
