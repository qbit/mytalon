from talon import app, actions

def disable_on_start():
    actions.speech.disable()

app.register("launch", disable_on_start)

app.notify(title="Talon startup complete!",
           subtitle="Speech is disabled.\nHappy hacking!",
           sound=True)
