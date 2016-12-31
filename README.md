# game

This is an in-development game (think alpha or pre-alpha) where you start with very little on an astronimical body and the goal is to eventually terraform it.

# Installation

*Dependencies required to run:*
  - [python 2.7](https://www.python.org/downloads)
  - [pygame for py2.7 and pygame-sdl4 (32-bit)](http://www.pygame.org/wiki/GettingStarted) 
    - [Windows Direct Download](http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)
	- [Mac Direct Download](http://pygame.org/ftp/pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg)
	- [Linux and BSD installation information](http://www.pygame.org/download.shtml)

  

**Installation via Python pip on Generic Linux:**
```
git clone https://github.com/Master-Foo/game.git
cd game
sudo pip install -r ./requirements.txt
```

**Installation via Python pip on Ubuntu Linux:**
```
pip install pygame numpy matplotlib opensimplex sklearn scipy
git clone https://github.com/Master-Foo/game.git
cd game
```

**Installation via Python pip on Windows:**
 - [scipy for py2.7 Windows Direct Download](http://sourceforge.net/projects/scipy/files/scipy/0.16.1/scipy-0.16.1-win32-superpack-python2.7.exe/download)
```
pip install pygame numpy matplotlib opensimplex sklearn
git clone https://github.com/Master-Foo/game.git
cd game
```

**Run the game:**
```
python demo.py
```