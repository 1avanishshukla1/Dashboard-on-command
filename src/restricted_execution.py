import builtins
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ALLOWED_GLOBALS = {
    "__builtins__": {
        "print": print,
        "len": len,
        "range": range,
        "sum": sum,
    },
    "pd": pd,
    "np": np,
    "plt": plt,
}

FORBIDDEN = ["import", "os", "sys", "subprocess", "open", "__"]

def exec(code): #overriding builtin method because feeling lazy to change exec everywhere 😴, not a good practice though. 
    for word in FORBIDDEN:
        if word in code:
            raise ValueError(f"{word} is not allowed.")

    local_vars = {}
    builtins.exec(code, ALLOWED_GLOBALS, local_vars)
    return local_vars


