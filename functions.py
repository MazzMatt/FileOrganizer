import os,time,shutil

def CheckType(type):
    
    t='other'

    DIRECTORIES = {'html':['.html5','.html','.htm','.xhtml'],
                 'pdf':['.pdf'],
                 'images':['.jpeg','.jpg','.tiff','.gif','.bmp','.png','.bpg','.svg','.heif','.psd','.webp'],
                 'videos':['.avi','.flv','.wmf','.mov','.MP4','.webm','.vob','.mng','.qt','.mpg','.mpeg','.3gp'],
                 'documents':['.oxps','.epub','.pages','.docx','.doc','.fdf','.ods','.odt','.pwi','.xsn','.xps','.dotx','.docm','.dox','.rvg','.rtf','.rtfd','.wpd','.xls','.xlsx','.xlsb','.xlsm','.ppt','.pptx','.csv'],
                 'archives':['.a','.ar','.cpio','.iso','.tar','.gz','.rz','.7z','.dmg','.rar','.xar','.zip'],
                 'audio':['.aac','.aa','dvf','.m4a','.m4b','.m4p','.mp3','.msv','.ogg','.oga','.raw','vox','.wav','.wma'],
                 'plaintext':['.txt','.in','.out'],
                 'xml':['.xml'],
                 'exe':['.exe'],
                 'shell':['.sh']}
    

    for name in DIRECTORIES:
        for i in range(len(DIRECTORIES[name])):
            if type == DIRECTORIES[name][i]:
                t = name
        
    return t

def Loading(choice):

    match choice:
        case 1: alert = 'PRZENOSZENIE'
        case 2: alert = 'KOPIOWANIE'

    t=['⠉','⠹','⠼','⠂','⠋']
    x=0

    print('\n')

    for i in range(50):

        time.sleep(0.1)
        print(f'  {alert} {t[x]}', end='\r')
        x+=1

        if x == 5:
            x=0

    print('                            ', end='\r')


DirNames = [ '__HTML__',
             '__PDF__', 
             '__ZDJĘCIA__', 
             '__FILMY__', 
             '__DOKUMENTY__',
             '__ARCHIWA__',
             '__DŹWIĘKI__',
             '__PLIKI TEKSTOWE__',
             '__PYTHON__',
             '__XML__',
             '__PLIKI EXE__',
             '__PLIKI SHELL__',
             '__INNE__']


def IsFile(path_name, main_path, choice):

    path = path_name

    Files_List = []
    
    for element in os.listdir(path):
        if os.path.isfile(os.path.join(path,element)):
            Files_List.append(element)
        if os.path.isdir(os.path.join(path,element)):
            Files_List.insert(len(Files_List),element)
    


    for file in Files_List:

        if os.path.isfile(os.path.join(path,file)):
            
            filetype = '.'+file.rsplit('.', 1)[1]
            f_name = file.rsplit('.', 1)[0]


            output = CheckType(filetype)

            match output:
                case 'html':           title = DirNames[0]
                case 'pdf':            title = DirNames[1]
                case 'images':         title = DirNames[2]
                case 'videos':         title = DirNames[3]
                case 'documents':      title = DirNames[4]
                case 'archives':       title = DirNames[5]
                case 'audio':          title = DirNames[6]
                case 'plaintext':      title = DirNames[7]
                case 'python':         title = DirNames[8]
                case 'xml':            title = DirNames[9]
                case 'exe':            title = DirNames[10]
                case 'shell':          title = DirNames[11]
                case 'other':          title = DirNames[12]

            NewDirPath = f'{main_path}/{title}'

            try:
                os.mkdir(NewDirPath)
                print(f'📂 Folder {title} pomyślnie utworzony')
                DirNames.append(title)

            except FileExistsError:
                pass
                #print(f'📁 Folder {title} już istnieje')


            # PRZENOSZENIE
            if choice == 1:                
                
                try:
                    shutil.move(f'{path}/{file}', NewDirPath)

                except:
                    x = 0
                    y = 1

                    for name in os.listdir(NewDirPath):
                        if os.path.isfile(os.path.join(NewDirPath, name)):
                            if name == file:
                                x+=1
                            if name == f'{f_name} — kopia ({y}){filetype}':     
                                x+=1
                                y+=1

                    #os.rename(f'{path}/{file}', f'{path}/({x}) {file}')
                    shutil.move(f'{path}/{file}', f'{NewDirPath}/{f_name} — kopia ({y}){filetype}')

                   
            # KOPIOWANIE
            if choice == 2:

                if not os.path.exists(f'{NewDirPath}/{file}'):
                    shutil.copy(f'{path}/{file}', f'{NewDirPath}/{file}')

                else:
                    x = 0
                    y = 1

                    for name in os.listdir(NewDirPath):
                        if os.path.isfile(os.path.join(NewDirPath, name)):
                            if name == file:
                                x+=1
                            if name == f'{f_name} — kopia ({y}){filetype}':      
                                x+=1
                                y+=1

                    shutil.copyfile(f'{path}/{file}', f'{NewDirPath}/{f_name} — kopia ({y}){filetype}')
                    
        
        
        if os.path.isdir(os.path.join(path,file)) and file not in DirNames:
            IsFolder(file, path, main_path, choice)

    
def IsFolder(dir_name, Path, main_path, choice):
    
    new_path = Path
    path=Path+'/'+dir_name

    IsFile(path, main_path, choice)


def RemoveDirs(main_path,choice):

    path = main_path

    if choice == 1:
        
        remove = 3

        while remove > 2 or remove < 1: 
            remove = int(input('\nCzy usunąć wszystkie puste foldery po przeniesionych plikach? \n - TAK (wpisz 1) \n - NIE (wpisz 2)\n\nWybór: '))

        if remove == 1:
            for file in os.listdir(path):

                if os.path.isdir(os.path.join(path,file)):
                    
                    if file not in DirNames:
                        shutil.rmtree(path+'/'+file)


        

def Close():
    
    seconds=9

    while seconds > -1:
        print(f' Zakończenie programu za: {seconds}', end='\r')
        time.sleep(1)
        seconds-=1

