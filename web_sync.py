import requests
import sys
import os

def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de l'URL : {e}")
        sys.exit(1)

def write_content(content, file):
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")
        sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    output_file = "/tmp/web_page"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    print(f"Téléchargement de la page : {url}")
    content = get_content(url)

    print(f"Écriture du contenu dans le fichier : {output_file}")
    write_content(content, output_file)

    print("Téléchargement terminé avec succès.")