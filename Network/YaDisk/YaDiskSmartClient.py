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

    # Create subfolders if dst contains not exsisted subfolders
    def smart_upload(self, src: str, dst: str):
        try:
            self.upload(src, dst)
        except Exception as e:
            # If conflict
            if int(str(e).split('.')[0]) != 409:
                raise e
            
            folders = []
            if dst.split('/'):
                folders = dst.split('/')
            elif dst.split('\\'):
                folders = dst.split('\\')

            folders = list(filter(None, folders))[:-1]

            dst_dir = ''
            for folder in folders:
                dst_dir += f'{folder}/'

            dst_dir = dst_dir[:-1]

            self.mkdirs_from_path(dst_dir)
            self.upload(src, dst)