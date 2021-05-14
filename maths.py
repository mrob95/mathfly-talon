from talon import Context, Module, actions
from typing import NamedTuple

fractions = {
    "half": "2",
    "halve": "2",
    "third": "3",
    "quarter": "4",
    "fourth": "4",
    "fifth": "5",
    "sixth": "6",
    "seventh": "7",
    "eighth": "8",
    "ninth": "9",
    "tenth": "10",
}

mod = Module()
ctx = Context()

mod.tag("maths")

mod.list("maths_fractions", "Fractions")
ctx.lists["user.maths_fractions"] = {
    **fractions,
    **{f"{k}s": v for k, v in fractions.items()},
}


@mod.action_class
class Actions:
    def maths_greek_letter(letter: str):
        """Insert a greek letter (one of those in the greek_letters list)"""

    def maths_tex_symbol(symbol: str):
        """Insert a TeX symbol (one of those in the tex_symbols list)"""

    def maths_matrix(rows: int, columns: int):
        """Insert a matrix (rows x columns)"""

    def maths_fraction():
        """Begin a fraction"""

    def maths_begin_superscript():
        """Begin superscript"""
    def maths_end_superscript():
        """End superscript"""
        actions.key("right")
    def maths_superscript(exponent: str):
        """Superscript"""
        actions.user.maths_begin_superscript()
        actions.insert(exponent)
        actions.user.maths_end_superscript()

    def maths_begin_subscript():
        """Begin subscript"""
    def maths_end_subscript():
        """End subscript"""
        actions.key("right")
    def maths_subscript(label: str):
        """Subscript"""
        actions.user.maths_begin_subscript()
        actions.insert(label)
        actions.user.maths_end_subscript()
