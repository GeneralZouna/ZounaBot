import os
__all__ = []
for Lib in os.listdir("./Commands"):
    if Lib.endswith(".py"):
        if Lib != "__init__.py" and Lib != " ":
            __all__.append(Lib.rstrip('.py'))
