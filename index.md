## Apresentação Inicial

Grupo 2 - Rafael da Rocha Ferreira, Gabriel Vasconcelos Martins
email de contato: rarafa245@gmail.com

Apresentaremos agora os elementos básicos para manutenção e revisão do código
**Link do repositório**: https://github.com/rarafa245/InfoColetorWeb

### Informações de Coleta

```markdown
  User-agent: Group2bot
  Allow: /                # Allow Everything 
  Disallow: /private/     # Disallow this directory
```

```markdown

  - Nome de Identificação do Coletor: Group2bot

  O coletor projeto atua penas em paginas publicas. Alem disso, a referencia para coletas apresentadas
  ao coletor vem a partir do código fonte das paginas web.
  
  - Para obter o código fonte, basta entrar em uma pagina web, clicar com o botão direito do mouse e selecionar
  a opção fonte da pagina de exibição. Irá aparecer a tradução em HTML da pagina desejada, basta copiar o link https
  (ou http) da pagina desejada (ex: https://www.treinaweb.com.br/blog/criando-paginas-para-repositorios-com-o-github-pages/)
  e aplica-lo no coletor. Tal metodo de aplicação será apresentado logo a baixo
  
  A coleta de paginas nao teve um alvo propriamente dito, foram feitas verias coletas de paginas diferentes e aleatorias com
  o unico objetivo de verificar o processo de coleta e a conscistência do coletor. Alem disso, tais coletas nao foram salvas, apenas
  printadas para o usuario, já que não foi requerido um sistema de logger ou armazenamento.

```


### Funcionamento Básico de Inicialização e Testes

Será mostrado como fazer inicialização do código

```markdown
Ao abrir o arquivo run.py, teremos o seguinte código:

    scheduler = Scheduler(str_usr_agent="Group2bot",
                                int_page_limit=14,
                                int_depth_limit=6,
                                arr_urls_seeds=[])
    fetcher = PageFetcher(scheduler)

    fetcher.insertURLs()
    fetcher.run()
    
    
o objeto scheduler ditará qual será o limite de paginas desejadas (profundidade 1) no argumento int_page_limit
e qual será a profundidade suportada em int_depth_limit


Abrindo o arquivo **page_fetcher.py** teremos a função **insertURLs** que é o local de agregação das urls desejadas.
Nela, ao se fazer a inserção de uma nova url, deve-se adiciona-la a funcao e adicionar a variavel no vetor **arr_urls**

Lembre-se que, apos fazer certa alteração, é necessário a alteração do objeto scheduler (codigo acima)
```

Será mostrado como fazer inicialização dos testes
```markdown
  Os testes se encontram na pasta testes e sao importado no arquivo runTestes.py
  Basta apenas rodar o arquivo runTestes.py que os testes serão realizados
```
