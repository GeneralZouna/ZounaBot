import os
__all__ = []
for Lib in os.listdir("./Commands"):
    if Lib.endswith(".py"):
        if Lib != "__init__.py" and Lib != " ":
            #print(Lib)
            __all__.append(Lib.replace(".py",""))
