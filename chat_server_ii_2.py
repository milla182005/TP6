import asyncio

async def handle_packet(reader, writer):
    client_address = writer.get_extra_info("peername")
    print(f"Nouvelle connexion de {client_address[0]}:{client_address[1]}")

    try:
        data = await reader.read(1024)
        message = data.decode().strip()
        print(f"Message reçu de {client_address[0]}:{client_address[1]}: {message}")

        response = f"Hello {client_address[0]}:{client_address[1]}"
        writer.write(response.encode())
        await writer.drain()

        print(f"Réponse envoyée à {client_address[0]}:{client_address[1]}")

    except Exception as e:
        print(f"Erreur avec {client_address[0]}:{client_address[1]}: {e}")

    finally:
        print(f"Connexion fermée avec {client_address[0]}:{client_address[1]}")
        writer.close()
        await writer.wait_closed()

async def main():
    host = "127.0.0.1"
    port = 8888

    print(f"Serveur en cours de démarrage sur {host}:{port}...")

    server = await asyncio.start_server(handle_packet, host, port)

    addr = server.sockets[0].getsockname()
    print(f"Serveur démarré sur {addr[0]}:{addr[1]}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())

