from talon import Module, Context, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
app: scinoteb.exe
"""

ctx.lists["user.greek_letters"] = {
    # Lowercase
    "alpha": "a",
    "beater": "b",
    "gamma": "g",
    "delta": "d",
    "epsilon": "e",
    "zita": "z",
    "eater": "h",
    "theta": "y",
    "iota": "i",
    "kappa": "k",
    "lambda": "l",
    "mu": "m",
    "new": "n",
    "zee": "x",
    "pie": "p",
    "row": "r",
    "sigma": "s",
    "tau": "t",
    "upsilon": "u",
    "phi": "f",
    "chi": "q",
    "sigh": "c",
    "omega": "w",
    "gamma": "g",
    # Capitals
    "big delta": "D",
    "big lambda": "L",
    "big pie": "P",
    "big sigma": "S",
    "big upsilon": "U",
    "big phi": "F",
    "big sigh": "C",
    "big omega": "W",
}

@ctx.action_class("user")
class Actions:
    def maths_greek_letter(letter: str):
        actions.key(f"ctrl-g {letter}")

    def maths_tex_symbol(symbol: str):
        actions.key("ctrl:down")
        actions.insert(symbol)
        actions.key("ctrl:up")

    def maths_matrix(rows: int, columns: int):
        actions.key("f10")
        actions.sleep("50ms")
        actions.key("i down:8 enter")
        actions.insert(rows)
        actions.key("tab")
        actions.insert(columns)
        actions.key("enter")

    def maths_fraction():
        actions.key("ctrl-f")

    def maths_begin_superscript():
        actions.key("ctrl-h")
    def maths_begin_subscript():
        actions.key("ctrl-l")