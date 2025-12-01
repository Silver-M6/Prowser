# Prowser is an opensource Browser written in python
<br>
Prowser is an open source browser in python thats designed for old PCs

-------------
halp, how to build??
-------------
<!-- TO DO: make wiki -->
On Linux
<br>
Setup:
<hr>
Debian/Ubuntu:

```
$ sudo apt install upx python3
```
Arch Linux:
```
$ sudo pacman -S upx python3
```
<br>

Setup:
```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install PyQt5 PyQtWebEngine
(venv) $ pip install pyinstaller
```
Build:
```
(venv) $ pyinstaller --onedir --windowed \
    --collect-submodules PyQt5.QtCore \
    --collect-submodules PyQt5.QtWidgets \
    --collect-submodules PyQt5.QtWebEngineWidgets \
    browser/Prowser.py
```
```
If you want compression:
```
```
(venv) $ pyinstaller --onedir --windowed --upx-dir=/usr/bin \
    --collect-submodules PyQt5.QtCore \
    --collect-submodules PyQt5.QtWidgets \
    --collect-submodules PyQt5.QtWebEngineWidgets \
    browser/Prowser.py
```
Wait for it to build, then do
```
(venv) $ source ~/.bashrc 
```
To return to the terminal
```
$ cd dist/Prowser
$ ./Prowser
```
To execute it

<br>

------------
# Screenshots:
<img width="1407" height="900" alt="image" src="https://github.com/user-attachments/assets/da776b71-4344-4a15-a0d8-627565f40a44" />

------------
# On Windows (NOT TESTED) :
<br>

Setup: [Python3](https://www.python.org/downloads/windows/)

<br>

Follow the linux steps at the top

<br>

(except for source ~/.bashrc, and $ ./Prowser)
