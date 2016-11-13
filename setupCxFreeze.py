
import sys
from cx_Freeze import setup, Executable
import cx_Freeze

if len(sys.argv) == 1:
    sys.argv.append("build")

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","pygame"], "excludes": ["tkinter"],
                     "include_files":['asteroid.png', 'asteroidICO.png','Background.png',
                     'spaceship.png','laserShoot.png','life.png', 'YouWin.png','gameOver.png',
                     'spaceShipRed.png','chiptuneMusic.wav', 'lose.wav','success.wav',
                     'Nonserif.ttf']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "space game",
        version = "0.1",
        description = "My game!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("game.py", base=base)])
