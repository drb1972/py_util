# py_util

zw.py: import utility library

untrs.py: Unterse local file. If SEQ it will be opened in VScode
   -f local tersed file name - Full path if not in the same dir
   - t type seq or pds
   python untrs.py -f C:\Users\dr891415\Downloads\FILE.N.Q1.TRS -t seq

trs.py: Terse remote file and download to .\out\<pds-name> 
   -f remote file name
   python trs.py -f prod001.lib.rexx