from ftplib import FTP

ftp_server = "192.168.201.63"
ftp_port = 21
ftp_user = "alumno"
ftp_password = "ciud4d"

ftp = FTP()
ftp.connect(ftp_server, ftp_port)
ftp.login(ftp_user, ftp_password)

ftp.dir()

archivo = "calendario.pdf"
with open(archivo, 'wb') as file:
    ftp.retrbinary('RETR ' + archivo, file.write)

ftp.quit()