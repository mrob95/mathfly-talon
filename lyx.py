from talon import Module, Context, actions, app

mod = Module()
ctx = Context()

ctx.matches = r"""
app: lyx
app: LyX.exe
app: LyX2.3.exe
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

MODIFIER = "ctrl" if app.platform == "mac" else "alt"

@mod.action_class
class Actions:
    def lyx_control_sequence(type: str, keys: str):
        """Press a sequence of keys prefixed with a lyx control chord (ctrl-{type} on mac, alt-{type} otherwise)"""
        actions.key(f"{MODIFIER}-{type} {keys}")


@ctx.action_class("user")
class Actions:
    def maths_greek_letter(letter: str):
        actions.insert(f"\\{letter} ")

    def maths_tex_symbol(symbol: str):
        actions.insert(f"\\{symbol} ")

    def maths_matrix(rows: int, columns: int):
        actions.user.lyx_control_sequence("m", "[")
        actions.user.maths_tex_symbol("array")
        for _ in range(rows-1):
            actions.user.lyx_control_sequence("m", "w i")
        for _ in range(columns-1):
            actions.user.lyx_control_sequence("m", "c i")

    def maths_fraction():
        actions.user.lyx_control_sequence("m", "f")

    def maths_begin_superscript():
        actions.key("^")
    def maths_begin_subscript():
        actions.key("_")
