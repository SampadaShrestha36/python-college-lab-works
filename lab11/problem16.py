# Demonstrate Renaming, Moving, Copying, and Removing operations of Files in python with or without shutil package.

import shutil
import os

shutil.move("poem.txt","poem3.txt")
shutil.copy("poem.txt","poem4.txt")
os.remove("poem.txt")