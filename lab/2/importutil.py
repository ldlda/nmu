"ass"

# do not tamper
import importlib.util
from pathlib import Path
from sys import modules

# oho


def why_so_ass(file: Path | str, name: str, namesys: str = None):
    """register file as module on sys.modules.
    namesys is the one have dots in it its ok"""
    # import importlib
    if namesys is None:
        namesys = name
    if not file.is_file():
        raise FileNotFoundError("where bro pointing to")
    file = file.resolve(True)
    spec = importlib.util.spec_from_file_location(name=name, location=file)

    mod = importlib.util.module_from_spec(spec)
    modules[namesys] = mod  # !!
    spec.loader.exec_module(mod)
    ## this line right here
    ## why do i need it to exec EVER WHY no i dont WHYYYYY
    # if i do from tutorial import bungee_jumper in tutorial2.ipynb it dont do that # oh it does