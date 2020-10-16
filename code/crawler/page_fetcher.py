from bs4 import BeautifulSoup
from threading import Thread
import requests
from urllib.parse import urlparse,urljoin
import time
from typing import List

class PageFetcher(Thread):
    def __init__(self, obj_scheduler):
        self.obj_scheduler = obj_scheduler


    def request_url(self,obj_url) -> bytes:
        '''
            requisita informações de uma devida url e retorna o conteudo
            em binário
            :parram - obj_url : Tupla com informações referentes a url apresentada 
                                (scheme, netloc, path, query)
            :return - informação em bytes caso conteudo html, None caso não html
        '''
        
        url = obj_url.geturl()
        req = requests.get(url, auth=(self.obj_scheduler.str_usr_agent, ''))

        if 'text/html' in req.headers["content-type"]:
            return bytes(req.text, 'utf-8')
        else:
            return None
        

    def discover_links(self,obj_url,int_depth,bin_str_content) -> List:
        '''
            Extrai tags de uma string binaria html (usando BeautifulSoup)
            :parram - obj_url: Tupla com informações referentes a url apresentada 
                                (scheme, netloc, path, query)
                    - int_depth: Profundidade do Objeto de URL inserido
                    - bin_str_content: String binaria html
            :return - lista contendo tuplas com objetos URL e sua profundidade 
        '''
        
        obj_new_url = ''
        int_new_depth = 0
        elements = []
        count = 1

        soup = BeautifulSoup(bin_str_content, 'html.parser')
        anchor_tags = soup.select("a")                              # Selecionando tags <a> da string binária html

        if anchor_tags:
            # Caso sejam captadas tags <a> na string binaria html

            for tag in anchor_tags:

                # Retirada da url da tag <a>
                val1 = str(tag).split('>')
                if 'href=' not in val1[0]:
                    continue
                val2 = val1[0].split('href=')
                val3 = val2[1].split('"')

                url = val3[1]
                # print(url)
                # print()
                
                if count <= int_depth:
                    # Caso ainda nao tenha percorrido toda a profundidade
                    # da url inserida como argumento

                    if obj_url.geturl() not in url:
                        # Caso a url capturada não tenha a inicial da url
                        # inserida como argumento

                        new_url = obj_url.geturl() + '/' + url
                        obj_new_url = urlparse(new_url)
                        int_new_depth = int_depth + 1

                    else:
                        # Caso a url esteja formatada corretamente

                        obj_new_url = urlparse(url)
                        int_new_depth = int_depth + 1
                else:
                    # Caso a profundidade ja tenha sido
                    # toda percorrida

                    obj_new_url = urlparse(url)
                    int_new_depth = 0

                elements.append((obj_new_url,int_new_depth))
                count += 1
        
        return elements
            
            

    def crawl_new_url(self):
        '''
            Reutiliza os dois metodos anteriores para se fazer a coleta e a extração das paginas
            :parram - None
            :return - objeto com as urls e links parceados
        '''

        new_url = self.obj_scheduler.get_next_url()
        print(new_url)
        if (new_url[0]):
            # Caso haja resgate de URL valida, verifique se pode fazer fetch
                can_fetch = self.obj_scheduler.can_fetch_page(new_url[0])
                print(can_fetch)

                if (can_fetch):
                    # Caso possa fazer coleta, faça
                    request = self.request_url(new_url[0])

                    if (request):
                        # Caso haja boa requisição, capture os links
                        self.obj_scheduler.count_fetched_page()
                        elements = self.discover_links(new_url[0], new_url[1], request)
                        print(elements)
                        print()
                        return elements

        self.obj_scheduler.count_fetched_page()
        return None


    def run(self) -> List:
        '''
            Roda as seguintes URLs e retorna seus links extraidos
            :parram - None
            :return - lista com links extraidos
        '''

        urlDummy = (urlparse("https://pt.wikipedia.org/wiki/Programa_Olá_Mundo"), 1)
        urlTerra = (urlparse("https://www.terra.com.br"), 1)
        urlUOL1 = (urlparse("http://www.uol.com.br/"), 1)
        urlBOL = (urlparse("https://www.bol.uol.com.br"), 1)
        url3 = (urlparse("https://guilhermemuller.com.br/ead/html-css-na-pratica/montando-base-website"), 1)
        url4 = (urlparse("https://sig.cefetmg.br/sigaa/verTelaLogin.do"), 1)
        url5 = (urlparse("https://www.terra.com.br/esportes/lance/neto-sobre-covid-10x-pior-que-entrada-dura-de-zagueiro,f03e78d95420ebb68ca80f3a4920fd3fzik654oj.html"), 2)

        arr_urls = [urlDummy,url3,urlTerra,urlUOL1,urlBOL,url4,url5]

        [self.obj_scheduler.add_new_page(*url) for url in arr_urls]

        url_links = []

        while not self.obj_scheduler.has_finished_crawl():
            information = self.crawl_new_url()
            time.sleep(2)
            url_links.append(information)  
        
        return url_links
