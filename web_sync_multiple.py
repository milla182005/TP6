import requests
import sys
import os

def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        
        print(f"Erreur lors de la récupération de l'URL {url}: {e}")
        return None

def write_content(content, file):
    try:
        
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        
        print(f"Erreur lors de l'écriture du fichier {file}: {e}")

def sanitize_filename(url):
    
    sanitized = url.replace("https://", "").replace("http://", "")
    sanitized = sanitized.replace("/", "_")  
    return sanitized

def process_urls(file_path):
    
    try:
        with open(file_path, "r", encoding="utf-16") as file:
            urls = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {file_path}: {e}")
        sys.exit(1)

    for url in urls:
        print(f"Téléchargement de la page : {url}")
        content = get_content(url)
        if content:
            
            output_file = f"/tmp/web_{sanitize_filename(url)}"
            print(f"Écriture du contenu dans le fichier : {output_file}")
            write_content(content, output_file)
            print(f"Téléchargement terminé pour {url}.")
        else:
            print(f"Échec du téléchargement de {url}.")

if __name__ == "__main__":
   
    if len(sys.argv) != 2:
        print("Usage: python web_sync_multiple.py <path_to_file_with_urls>")
        sys.exit(1)

    file_path = sys.argv[1]

    process_urls(file_path)

    print("Tous les téléchargements ont été traités.")
