#!/bin/sh

tar -cf aster-wallpaper.tar.gz aster-wallpaper/

makepkg -s --sign

rm -r aster-wallpaper.tar.gz
rm -r pkg/ src/ 
