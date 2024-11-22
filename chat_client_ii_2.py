import socket

def main():
    host = "127.0.0.1"
    port = 8888

    try:
        with socket.create_connection((host, port)) as sock:
            print(f"Connecté au serveur {host}:{port}")

            message = "Hello"
            sock.sendall(message.encode())
            print(f"Message envoyé au serveur : {message}")

            response = sock.recv(1024)
            print(f"Réponse reçue du serveur : {response.decode()}")

    except ConnectionRefusedError:
        print("Impossible de se connecter au serveur. Assurez-vous qu'il est démarré.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")