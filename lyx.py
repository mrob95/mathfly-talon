from talon import Module, Context, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
app: lyx
app: LyX.exe
app: LyX for Windows
"""

ctx.lists["user.greek_letters"] = {
    # Lowercase
    "alpha": "alpha",
    "beater": "beta",
    "gamma": "gamma",
    "delta": "delta",
    "epsilon": "varepsilon",
    "zita": "zeta",
    "eater": "eta",
    "theta": "theta",
    "iota": "iota",
    "kappa": "kappa",
    "lambda": "lambda",
    "mu": "mu",
    "new": "nu",
    "zee": "xi",
    "pie": "pi",
    "row": "rho",
    "sigma": "sigma",
    "tau": "tau",
    "upsilon": "upsilon",
    "phi": "phi",
    "chi": "chi",
    "sigh": "psi",
    "omega": "omega",
    # Capitals
    "big gamma": "Gamma",
    "big delta": "Delta",
    "big theta": "Theta",
    "big lambda": "Lambda",
    "big zee": "Xi",
    "big pie": "Pi",
    "big sigma": "Sigma",
    "big upsilon": "Upsilon",
    "big phi": "Phi",
    "big sigh": "Psi",
    "big omega": "Omega",
}

@ctx.action_class("user")
class Actions:
    def maths_greek_letter(letter: str):
        actions.insert(f"\\{letter} ")

    def maths_tex_symbol(symbol: str):
        actions.insert(f"\\{symbol} ")

    def maths_matrix(rows: int, columns: int):
        actions.key("alt-m [")
        actions.user.maths_tex_symbol("array")
        for _ in range(rows-1):
            actions.key("alt-m w i")
        for _ in range(columns-1):
            actions.key("alt-m c i")

    def maths_fraction():
        actions.key("alt-m f")

    def maths_begin_superscript():
        actions.key("^")
    def maths_begin_subscript():
        actions.key("_")
