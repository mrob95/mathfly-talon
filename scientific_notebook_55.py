from talon import *

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
