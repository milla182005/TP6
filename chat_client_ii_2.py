import socket

def main():
    host = "10.1.1.2"  
    port = 8889        

    try:
       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((host, port))
        print(f"Connecté au serveur {host}:{port}")

        message = "Hello"
        s.sendall(message.encode())
        print(f"Message envoyé au serveur : {message}")

        response = s.recv(1024)  
        print(f"Réponse reçue du serveur : {response.decode()}")

    except ConnectionRefusedError:
        print("Impossible de se connecter au serveur. Assurez-vous qu'il est démarré.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        
        s.close()

if __name__ == "__main__":
    main()
