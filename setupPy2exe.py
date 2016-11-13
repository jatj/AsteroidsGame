from distutils.core import setup
import pygame
from pygame import mixer
from pygame import font
import py2exe
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")

setup( options = {"py2exe": {"compressed": 1, "optimize": 2, "ascii": 1,
                             "bundle_files": 3,
                             "packages":['pygame'],
"excludes": ["OpenGL.GL", "Numeric", "copyreg", "itertools.imap", "numpy", "pkg_resources", "queue", "winreg", "pygame.SRCALPHA", "pygame.sdlmain_osx",'AppKit', 'Carbon', 'Carbon.Files', 'Foundation', 'OpenGL.GLU', 'RandomArray', '_scproxy', '_sysconfigdata', 'dummy.Process', 'opencv', 'psyco', 'test.__main__', 'test.event_test', 'test.test_utils', 'test.test_utils.async_sub', 'test.test_utils.run_tests', 'test.test_utils.test_runner', 'test.test_utils.unittest_patch', 'urllib.parse', 'vidcap', 'win32api', 'win32file', 'win32pipe']
                             }},
       zipfile = None,

       data_files = ['asteroid.png', 'asteroidICO.png','Background.png',
                     'spaceship.png','laserShoot.png','life.png', 'YouWin.png','gameOver.png',
                     'spaceShipRed.png','chiptuneMusic.wav', 'lose.wav','success.wav',
                     'Nonserif.ttf'],
       
       #Your py-file can use windows or console
       windows = [{"script": 'game.py'}])

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
       if os.path.basename(pathname).lower() in ["sdl_ttf.dll"]:
               return 0
       return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL
