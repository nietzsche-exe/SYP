from ftplib import FTP

ftp_server = "ftp.osuosl.org"
ftp_user = "anonymous"
ftp_password = "anonymous"  

archivo_local = "C:\Users\alumno-215\visual - workspace\icegif-162.gif"
directorio_remoto = "dir/"

ftp = FTP()
ftp.connect(ftp_server)
ftp.login(ftp_user, ftp_password)

directory_path = "pub/ubuntu/dists/xenial"
ftp.cwd(directory_path)

ftp.dir()

archivo = "Release.gpg"
with open(archivo, 'wb') as file:
    ftp.retrbinary('RETR ' + archivo, file.write)
    
    
nombre_archivo_remoto = "nombre_en_el_servidor.txt"
with open(archivo_local, 'rb') as archivo:
    ftp.storbinary(f"STOR {nombre_archivo_remoto}", archivo)

ftp.quit()