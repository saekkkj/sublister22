import requests
from bs4 import BeautifulSoup

def scanner_subdiretorios(url):
    try:
        
        resposta = requests.get(url)
        
        
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
   
        links = soup.find_all('a')
        
        
        diretorios = []
        
       
        for link in links:
            href = link.get('href')
            if href.endswith('/'): 
                diretorios.append(href)
        
    
        for diretorio in diretorios:
            print(diretorio)
        
       
        return len(diretorios)
    except:
        
        return 0

url = input('Digite a URL do site: ') 
resultado = scanner_subdiretorios(url)
print('Número de diretórios encontrados:', resultado)
input("Clique Enter para fechar o sublister")