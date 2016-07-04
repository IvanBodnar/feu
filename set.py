import sys
from cx_Freeze import setup, Executable
import requests.certs

build_exe_options = {"include_files":[(requests.certs.where(), 'cacert.pem')]}
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

setup(
    name='Prueba',
    version='0.1',
    description='Prueba',
    options={"build_exe": build_exe_options},
    executables=[Executable('feu_main.pyw', base=base)]
)