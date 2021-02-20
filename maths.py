from talon import Context, Module

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