from talon import app, actions

def disable_on_start():
    actions.speech.disable()
    actions.speech.set_microphone('None')

app.register("launch", disable_on_start)

app.notify(title="Talon startup complete!",
           subtitle="Speech and MIC are disabled.\nHappy hacking!",
           sound=True)
