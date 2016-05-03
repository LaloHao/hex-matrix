C:\Python27\python.exe code2hex.py "%1" > "%~n1.tmp"
C:\Python27\python.exe checksum.py "%~n1.tmp" > "%~n1.hex"
rm "%~n1.tmp"