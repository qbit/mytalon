from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

mod.apps.element = "app.name: Element"
ctx.matches = r"""
app: element
"""
ctx.tags = ["browser"]

