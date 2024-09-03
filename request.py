import requests

def check_http_verbs(url):
    verbs = ['GET', 'POST', 'PUT', 'DELETE']
    results = {}

    for verb in verbs:
        try:
            response = requests.request(verb, url)
            results[verb] = response.status_code
        except requests.exceptions.RequestException as e:
            results[verb] = str(e)

    return results

if __name__ == "__main__":
    url = input("Inserisci l'URL da controllare: ")
    results = check_http_verbs(url)
    
    for verb, status in results.items():
        print(f"{verb}: {status}")
