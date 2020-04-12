from YaDiskClient.YaDiskClient import YaDisk, YaDiskException

class YaDiskSmart(YaDisk):
    def mkdirs_from_path(self, path: str):
        # Characters not allowed in file and folder names
        errorSimbols = ['\\', '/', ':', '*', '?', '\"', '<', '>', '|']
        folders = []

        if '\\' in path:
            #folder\subfolder\subsubfolder
            folders = path.split('\\')
        elif '/' in path:
            #folder/subfolder/subsubfolder
            folders = path.split('/')
        else:
            #folder
            folders.append(path)

        # Remove empty strings from folders
        folders = list(filter(None, folders))

        # Parse result path
        print(folders)

        if not folders:
            raise YaDiskException(400, f'Incorrect path: {path}')

        # Check not allowed characters in path
        for folder in folders:
            for simbol in errorSimbols:
                if simbol in folder:
                    raise YaDiskException(400, f'Incorrect folder name {folder} in path: {path}')

        print(f'Path \"{path}\" is correct')

        path = ''
        for folder in folders:
            path += f'/{folder}'

            #Проверить существует ли папка?
            try:    
                self.ls(path)
                print(f'Already exist path: {path}')

            except Exception as e:
                self.mkdir(path)