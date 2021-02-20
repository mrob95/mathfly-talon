from talon import *
from typing import Tuple

mod = Module()
ctx = Context()

current_page = 1
lines_per_page = 20
extra_padding = 50
current_view = "Start"

lyx_help_text = """LyX help

To get started, use the 'new file' command
to create a new file, then use the 'math mode'
command to start inserting mathematics.

Try the following sequence:

integral plex squared equals one third plex cubed

For a full list of available commands, click
the buttons below.

To modify or add commands, see the following files:
- lyx.py
- lyx.talon
- tex_maths.py
"""

sn55_help_text = """Scientific Notebook 5.5 help

To get started, use the 'body maths' command
to start inserting mathematics.

Try the following sequence:

integral plex squared equals one third plex cubed

For a full list of available commands, click
the buttons below.

To modify or add commands, see the following files:
- scientific_notebook_55.py
- scientific_notebook_55.talon
- tex_maths.py
"""

def draw_multiline_text(gui: imgui.GUI, text: str):
    for line in text.split("\n"):
        gui.text(line)

def draw_page_buttons(gui: imgui.GUI, total_items: int):
    global current_page
    num_pages = (total_items // lines_per_page) + 1
    gui.text(f"| {current_view} - Page {current_page} / {num_pages} {' '*extra_padding} |")
    if gui.button("Next page") and current_page < num_pages:
        current_page += 1
    if gui.button("Previous page") and current_page > 1:
        current_page -= 1

def get_bounds_of_items_shown(total_items: int) -> Tuple[int, int]:
    start = lines_per_page * (current_page - 1)
    end = lines_per_page * (current_page)
    if end >= total_items:
        end = total_items - 1
    return start, end

def draw_view_picker(gui: imgui.GUI):
    global current_view
    global current_page
    for view in ("Symbols", "Greek letters", "Other"):
        if gui.button(view):
            current_page = 1
            current_view = view


@imgui.open(y=0, software=app.platform == "linux")
def gui_maths_help(gui: imgui.GUI):
    maths_contexts = [context for context in registry.active_contexts() if "user.maths" in context.tags]
    if not maths_contexts:
        gui.text("Maths context not currently focused")
        return
    context = maths_contexts[0]

    if current_view == "Start":
        if "lyx" in str(context):
            draw_multiline_text(gui, lyx_help_text)
        elif "scientific_notebook" in str(context):
            draw_multiline_text(gui, sn55_help_text)

    else:
        items = []
        if current_view == "Symbols":
            items = list(registry.lists["user.tex_symbols"][0].keys())
            items = sorted(items)

        elif current_view == "Greek letters":
            greek_letters = list(registry.lists["user.greek_letters"][0].keys())
            items = [f"greek {g}" for g in greek_letters]

        elif current_view == "Other":
            items = [c.rule.rule for c in context.commands.values()]

        draw_page_buttons(gui, len(items))
        gui.text("")

        start, end = get_bounds_of_items_shown(len(items))
        for i in range(start, end):
            gui.text(items[i])
        gui.text("")

    draw_view_picker(gui)
    if gui.button("Close"):
        gui_maths_help.hide()


@mod.action_class
class Actions:
    def maths_help_show():
        """Show help dialogue"""
        gui_maths_help.show()

    def maths_help_hide():
        """Hide help dialogue"""
        gui_maths_help.hide()
