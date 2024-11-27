import os, time
from functions import *

print('PROGRAM SORTUJĄCY PLIKI WEDŁUG ICH TYPU')

#-----------------------------------------------------------------

pre_path = input('\n💻 Wklej ścieżkę folderu, którego pliki chcesz posortować: \n\n')
x = '\ '
path = pre_path.replace(x.strip(),'/')
main_path = path 
choice = 3

while choice > 2 or choice < 1: 
    choice = int(input('\n 📑 Chcesz PRZENIEŚĆ pliki (wpisz liczbę 1)\n 📃 Chcesz SKOPIOWAĆ pliki (wpisz liczbę 2) \n\nWybór: '))

#-----------------------------------------------------------------

Loading(choice)

IsFile(path, main_path, choice)

#usuwanie pustych folderów 
RemoveDirs(main_path, choice)

time.sleep(1)
print('\n\n✅ Sortowanie plików w folderze zakończone\n')

Close()
        
        
        

        


