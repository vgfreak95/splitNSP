# splitNSP

As some have become aware, it's been found out that the official Nintendo SDK contains a PowerShell script for splitting NSP files into 4GiB chunks so that they can be installed from FAT32 filesystems. Seeing as the official script cannot be shared, I re-wrote it in Python3 (which makes it useable on more than just Windows) as well as added in an additional feature. 

To run it you'll need Python3 installed. Once installed, call the script from Terminal or Command Prompt with the following:

```python3 splitNSP.py filename.nsp```

By default this will make a copy of the NSP and split it up into parts. Once created, you'll need to open the folder's properties and check the Archive flag. This is easily done on Windows, I'm still working on a way to do it for macOS since file flags aren't saved when copying to FAT32. 

You can also activate quick mode with this command:

```python3 splitNSP.py -q filename.nsp```

This will not make a copy of the NSP and instead will split the original. This is useful if you're running low on space as it only requires that you have 4GiB of temporary space to run it. It's also much faster. 

Once the folder is made and the archive flag is set copy it to your SD card (sdmc:/tinfoil/nsp/ if using tinfoil) and install it like any other NSP. 

If you have any issues feel free to submit an issue and I'll try my best to work it out. 

# splitGUI

An extension of the splitNSP module that creates a quick and easy gui instead of having to activate the console.

To select a file, press the ```Browse NSP``` button. You can tell it was selected if the path shows up right next to it.

Once the file has been selected, you have to press ```Split File``` button to confirm your action. The program should excecute the splitCopy function and you will be good to go. HOWEVER YOU STILL NEED TO ARCHIVE YOUR FOLDER OTHERWISE IT WILL NOT BE RECOGNIZED BY GOLDLEAF OR TINFOIL.

Keep in mind the only working mode of the splitCopy command exists, I have yet to get to the splitQuick command.
