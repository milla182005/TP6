import aiohttp
import aiofiles
import asyncio
import sys
import os

async def get_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Erreur lors de la récupération de l'URL : {e}")
        sys.exit(1)

async def write_content(content, file):
    try:
        async with aiofiles.open(file, mode="w", encoding="utf-8") as f:
            await f.write(content)
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")
        sys.exit(1)

async def main():
    
    if len(sys.argv) != 2:
        print("Usage: python web_async.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    output_file = "/tmp/web_page"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    print(f"Téléchargement de la page : {url}")
    content = await get_content(url)

    print(f"Écriture du contenu dans le fichier : {output_file}")
    await write_content(content, output_file)

    print("Téléchargement terminé avec succès.")

if __name__ == "__main__":
    asyncio.run(main())
