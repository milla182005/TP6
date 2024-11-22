import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Un client s'est connecté depuis {addr}")

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                print(f"Le client {addr} s'est déconnecté.")
                break

            message = data.decode()
            print(f"Message reçu de {addr} : {message}")

            print(f"Message reçu de {addr[0]}:{addr[1]} : {message}")

            response = f"Message reçu: {message}"
            writer.write(response.encode())
            await writer.drain()

    except asyncio.CancelledError:
        print(f"Connexion avec le client {addr} annulée.")
    finally:
        print(f"Fermeture de la connexion avec {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server_host = '10.1.1.2'  
    server_port = 8889        

    server = await asyncio.start_server(
        handle_client, server_host, server_port
    )
    addr = server.sockets[0].getsockname()
    print(f"Serveur en écoute sur {addr}")

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
