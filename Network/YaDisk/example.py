from YaDiskClient.YaDiskClient import YaDisk

login = ''
password = ''

disk = YaDisk(login, password)

print(disk.ls('/'))
disk.upload('example.py', 'example.py')