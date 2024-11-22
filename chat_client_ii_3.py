import asyncio
from aioconsole import ainput

async def handle_user_input(writer):
    while True:
        try:
            message = await ainput("Vous: ")
            writer.write(message.encode() + b"\n")
            await writer.drain()
        except Exception as e:
            print(f"Erreur lors de l'envoi : {e}")
            break

async def handle_server_messages(reader):
    while True:
        try:
            data = await reader.read(1024)
            if not data:
                print("Connexion au serveur perdue.")
                break
            print(f"Serveur: {data.decode().strip()}")
        except Exception as e:
            print(f"Erreur lors de la réception : {e}")
            break

async def main():
    server_host = "10.1.1.2"  
    server_port = 8889

    print(f"Tentative de connexion au serveur {server_host}:{server_port}...")
    try:
        reader, writer = await asyncio.open_connection(server_host, server_port)
        print("Connecté au serveur.")
        
        await asyncio.gather(
            handle_user_input(writer),
            handle_server_messages(reader),
        )
    except ConnectionRefusedError:
        print("Impossible de se connecter au serveur. Vérifiez qu'il est en cours d'exécution.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nClient arrêté.")
