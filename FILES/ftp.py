import ftplib
ftp_server_url = 'ftp.hosteurope.de'
download_dir = '/mirror/ftp.kernel.org/pub/linux/kernel/tools/perf/v4.19.0'
download_file_name = 'perf-4.19.0.tar.gz'

def ftp_file_download(path, username, email):
  ftp_client = ftplib.FTP(path, username, email)
  ftp_client.cwd(download_dir)
  print("File list at %s:"%path)
  files = ftp_client.dir()
  print(files)
  file_handler = open(download_file_name, 'wb')
  ftp_client.retrbinary("RETR perf-4.19.0.tar.gz", file_handler.write)
  file_handler.close()
  ftp_client.quit()

if __name__ == '__main__':
  ftp_file_download(ftp_server_url, 'anonymous', email = "try@gmail.com")
  

