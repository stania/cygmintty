cmt: CygMinTty
==============

'cmt' runs bash login shell with mintty without cmd window. And it contains some trick to use cmt in Windows Explorer. And if Visual Studio is installed in your system, runs "vsvars32.bat" before it launches bash.

Usage in Windows Explorer
-------------------------

### Prerequisite 

Following lines in ~/.bashrc 

	if [ -n "$STARTDIR" ]; then
		cd "$STARTDIR"
	fi

### Usage 

Place cmt.exe in a directory which is in the PATH. 

In Windows Explorer, press `alt`+`d`to move focus to location bar, and type `cmt` then press `Enter`. Then mintty and bash will run on directory in where you were in Windows Explorer. 


Internals
---------

Under construction.

