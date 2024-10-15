import paramiko

def upload_csv_to_sftp(csv_data: str, sftp_host: str, sftp_port: int, sftp_username: str, 
                       sftp_password: str, sftp_remote_path: str):
    """
    Upload CSV data to an SFTP server.
    :param csv_data: The CSV data as a string.
    :param sftp_host: The SFTP server hostname.
    :param sftp_port: The port number of the SFTP server.
    :param sftp_username: The username for the SFTP server.
    :param sftp_password: The password for the SFTP server.
    :param sftp_remote_path: The remote file path where the CSV will be uploaded.
    """
    try:
        # Establish SFTP connection
        transport = paramiko.Transport((sftp_host, sftp_port))
        transport.connect(username=sftp_username, password=sftp_password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload CSV file
        with sftp.open(sftp_remote_path, 'w') as file:
            file.write(csv_data)

        print(f"Successfully uploaded CSV to {sftp_remote_path}")
    except paramiko.SSHException as ssh_exception:
        print(f"Failed to connect or authenticate with the SFTP server: {ssh_exception}")
        raise
    except Exception as e:
        print(f"Failed to upload CSV to SFTP: {e}")
        raise
    finally:
        # Close the SFTP connection
        if 'sftp' in locals():
            sftp.close()
        if 'transport' in locals():
            transport.close()