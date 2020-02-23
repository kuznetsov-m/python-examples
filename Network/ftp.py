#для подключения можно использовать как ip так и domain

import ftplib

file = 'test.txt'
ftpAddress = 'example.com'
ftpAddress = 'xxx.xxx.xxx.xxx'
ftpUid = 'X'
ftpPass = 'X'

ftp = ftplib.FTP(ftpAddress)
ftp.login(ftpUid, ftpPass)
ftp.cwd('/test')
try:
	ftp.storbinary('STOR ' + file, open(file, 'rb')) 
	print('STORing File now...')
	ftp.quit()
	print('File transfered')
except:
	print('fail')
	
#https://stackoverflow.com/questions/10647045/ftp-deletefilename-from-ftplib-error
#ftp.rmd("/Public/test/hello/will_i_be_deleted/")
#rmd is for removing directories, deleteis for removing files.