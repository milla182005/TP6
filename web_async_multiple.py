import aiohttp
import asyncio
import sys
import os
import time
import aiofiles

async def get_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Erreur lors de la récupération de l'URL {url}: {e}")
        return None

async def write_content(content, file):
    try:
        async with aiofiles.open(file, "w", encoding="utf-16") as f:
            await f.write(content)
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier {file}: {e}")

def sanitize_filename(url):
    sanitized = url.replace("https://", "").replace("http://", "")
    sanitized = sanitized.replace("/", "_")  
    return sanitized

async def process_urls(file_path):
    try:
        with open(file_path, "r", encoding="utf-16") as file:
            urls = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {file_path}: {e}")
        sys.exit(1)

    tasks = []
    for url in urls:
        print(f"Téléchargement de la page : {url}")
        content = await get_content(url)
        if content:
           
            output_file = f"/tmp/web_{sanitize_filename(url)}"
            tasks.append(write_content(content, output_file))
        else:
            print(f"Échec du téléchargement de {url}.")
    
    await asyncio.gather(*tasks)

def main():
    if len(sys.argv) != 2:
        print("Usage: python web_async_multiple.py <path_to_file_with_urls>")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()

    asyncio.run(process_urls(file_path))

    end_time = time.time()
    print(f"Tous les téléchargements ont été traités en {end_time - start_time:.2f} secondes.")

if __name__ == "__main__":
    main()
