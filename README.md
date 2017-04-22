# Towebp
Description:
============
Convert the png or jpg in the the Specified directory whose size larger than the Specified(default is 50*1024) to the different quality webp containing 50 75 95 and loseness.
the have two parameter.The first argument is the Specified directory ，the files in this directory will be converted
The Second parameter is the Specified Size(KB) ,and files larger than this size will be converted. 

Usage:
=========
python toWebp.py  dir  size
python toWebp.py ~/source/src/main/res/drawable-xxhdpi/ 50

FAQ:
========
1."/bin/sh: 1: cwebp: not found"
	first method(cp):
		sudo cp cwebp /usr/local/bin/
	second method(download the command line tools cwebp):
		1)download libwebp-0.6.0-linux-x86-32.tar.gz (https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-0.6.0-linux-x86-32.tar.gz)
		2).tar xvzf  libwebp-0.6.0-linux-x86-32.tar.gz
		3).sudo cp libwebp-0.6.0-linux-x86-32/bin/cwebp  /usr/local/bin/
	third method(build the cwebp yourself for linux):
		1).sudo apt-get install libjpeg-dev libpng-dev libtiff-dev libgif-dev
		2).download source,libwebp-0.6.0.tar.gz (https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-0.6.0.tar.gz)
		3).Compiling the source. 
				tar xvzf libwebp-0.6.0.tar.gz
				cd libwebp-0.6.0
				./configure --enable-everything
				make
				sudo make install

Discuss:
========
tanhaiqing89@126.com
 
