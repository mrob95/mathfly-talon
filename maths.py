from talon import Context, Module, actions
from dataclasses import dataclass
from typing import NamedTuple, Optional, Tuple

mod = Module()
ctx = Context()

mod.tag("maths")

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

mod.list("maths_fractions", "Fractions")
ctx.lists["user.maths_fractions"] = {
    **fractions,
    **{f"{k}s": v for k, v in fractions.items()},
}

mod.list("maths_common_powers", "Common powers e.g. squared, cubed")
ctx.lists["user.maths_common_powers"] = {
    "inverse": "-1",
    "squared": "2",
    "cubed": "3",
}

@mod.capture(rule="<user.letter> | {user.greek_letters}")
def maths_variable(m) -> str:
    "A single variable"
    return getattr(m, "letter", None) or getattr(m, "greek_letters", None)

@dataclass
class MathsFraction():
    num: str
    denom: Optional[str]

@mod.capture(rule="<number> [{user.maths_fractions}]")
def maths_fraction(m) -> MathsFraction:
    "A fraction, or just a number if the second element is None"
    return MathsFraction(m.number, getattr(m, "maths_fractions", None))

@dataclass
class MathsItem():
    number: Optional[MathsFraction]
    variable: Optional[str]
    end_power: Optional[str]

@mod.capture(
    rule="(<user.maths_fraction> | <user.maths_variable> | <user.maths_fraction> <user.maths_variable>)"
         "[{user.maths_common_powers}]"
)
def maths_item(m) -> MathsItem:
    """A single 'item', for example 'one half plex squared'"""
    maths_fraction = getattr(m, "maths_fraction", None)
    variable = getattr(m, "maths_variable", None)
    end_power = getattr(m, "maths_common_powers", None)
    return MathsItem(maths_fraction, variable, end_power)


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


    def maths_insert_fraction(fraction: MathsFraction):
        """"""
        if fraction.denom is None:
            actions.insert(fraction.num)
        else:
            actions.user.maths_fraction()
            actions.insert(fraction.num)
            actions.key("down")
            actions.insert(fraction.denom)
            actions.key("right")


    def maths_insert_item(item: MathsItem):
        """"""
        print(f'item = {item}')
        if item.number:
            actions.user.maths_insert_fraction(item.number)
        if item.variable:
            actions.insert(item.variable)

        if item.end_power:
            actions.user.maths_superscript(item.end_power)