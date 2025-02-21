import docker
# import streamlit
import paramiko
import getpass

username = input('What is your username? ')
dockerHost = input('What is the docker host IP? ')
password = getpass.getpass("Enter your SSH password: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(dockerHost, username=username, password=password)

    transport = ssh.get_transport()
    local_port = 23750
    remote_socket = "/var/run/docker.sock"
    local_forward = transport.open_channel("direct-tcpip", ("127.0.0.1", 2375), ("", 0))
    client = docker.DockerClient(base_url=f"tcp://127.0.0.1:{local_port}")

    print("\nContainers on the remote host:")
    for container in client.containers.list(all=True):
        print(f"{container.name} - {container.status}")
    client.close()
    ssh.close()

except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except Exception as e:
    print(f"Error: {e}")
finally:
    ssh.close()