from talon import Module, Context

mod = Module()
ctx = Context()

ctx.matches = r"""
app: LyX.exe
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

