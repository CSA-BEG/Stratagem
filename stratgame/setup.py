import sys
from cx_Freeze import setup, Executable

build_exe_options = {"include_files" : ["desert.png","desert2.png","cursor1.png","redb.png","blub.png","rk.png","rc.png","mov.png","redc.png","bluc.png","atk.png","bld.png","bc.png","rs.png","reds.png","redg.png","rm.png","selector.png","unit.png","cursor2.png","unitss.png","meh.png","unitsg.png","ui1.png","arrd.png","arrl.png","arru.png","arrr.png","bk.png","bm.png","bs.png","blug.png","blus.png","redu.png","bluu.png","file.png","pchu.wav","win1.png","win2.png","cursor3.png","desert.png","bgm.wav","blep.wav","ham.wav"]}

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },
}

# ...

setup(options = options,
      # ...
)

setup(
    name = "Stratagem",
    version = "1.0",
    description = "A pygame strategy game.",
    executables = [Executable("tk.py"),Executable("Strategy.py")])