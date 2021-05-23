import getpass
import paramiko

HOSTNAME = "localhost"
PORT = 22


def sftp_download(username, paswword, hostname=HOSTNAME, port=PORT):
    ssh_transport = paramiko.Transport(hostname, port)
    ssh_transport.connect(username=username, password=paswword)
    sftp_session = paramiko.SFTPClient.from_transport(ssh_transport)
    file_path = input("Enter filepath: ")
    target = file_path.split("/")[-1]
    sftp_session.get(file_path, target)
    print("File downloaded !!: %s" % file_path)
    sftp_session.close()


if __name__ == "__main__":
    hostname = input("Enter the target hostname: ")
    port = input("Enter the target port: ")
    username = input("Enter username: ")
    password = getpass.getpass(prompt="Enter password: ")
    sftp_download(username, password, hostname, int(port))

# http://ftp.hosteurope.de//mirror/ftp.kernel.org/pub/linux/kernel/tools/perf/v4.19.0