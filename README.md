# Inicilização do para testar django-signals

# 1 - Excluir pasta 'venv'

      Criar outra utilizando: 
           Windows: python -m venv venv
           Linux: python3 -m venv venv
           
      Ativar 'venv'
           Windows: venv/Scripts/Activate
           Linux: source venv/bin/activate.

# 2 - Bibliotecas fornecidas - 'requirements.txt'
      Para instalar todas de uma só vez, basta digitar no seu terminal: 
      
      Windows: pip install -r requirements.txt
      Linux: python3 install -r requirements.txt
            
 
 # Á seguir, explicação:
 
 # Oque é Django?

      O Django é um framework web full stack open source (código aberto) baseado em Python, gratuito e de alto nível.
      Este framework foi criado com o objetivo de resolver todos os problemas mais comuns do processo de desenvolvimento de aplicações web
      como por exemplo autenticação, rotas, object relational mapper (ORM) e até migrations.
      
 # Oque é Django-signals (sinais)
 
      O Django incluí um “dispachador de sinal” que ajuda ao permitir que aplicações dissociadas sejam notificadas quando uma ação ocorre em qualquer lugar do framework.
      Em resumo, sinais permitem certos remetentes notificar um conjunto de receptores sobre alguma ação que tenha ocorrido.
      Eles são especialmente úteis quando muitas peças de código podem estar interessados nos mesmos eventos.
      O Django fornece um conjunto de sinais embutidos que deixam o código do usuário ser notificado pelo próprio Django sobre certas ações.
      
 # IObserver que o Django-signals usa:
 
      Vamos falar do padrão Observer, na minha opinião é um dos mais interessantes, imagina manter os objetos atualizados quando acorrer algo em um objeto importante.
      E vamos ver ligações leves entre objetos uma boa pratica de programação, então vamos lá.

      Para entendermos o padrão Observer, vamos pensar como funciona uma Editora (Observado) de jornal, eles tem uma lista de clientes (Observadores),
      quando sai uma nova publicação todos os observadores recebem uma copia do jornal, sendo que a qualquer momento um novo cliente(Observador) 
      pode se registrar ou os clientes atuais cancelarem o registro.

      Bom, o padrão Observer é isso, um objeto (Observado) que permite que outros objetos sejam registrados  como observadores ou cancelar o seu registro a qualquer momento da aplicação,
      e ressaltando a ligação leve entre o objeto observado e seus observadores, com isso os objetos podem interagir,
      mas não sabem quase nada um sobre o outro, deixando bem flexível os objetos observadores e observados.

      Pensando em uma aplicação pratica, vamos criar rede de fabricação de automóveis, onde vamos ter duas montadoras (observados) e varias fabricas(observadores)
      e prestadora de serviços(observadores), observe que teremos 2 classes que farão o papel de observador (poderíamos ter “n” classes diferentes), 
      onde os fabricas e prestadoras vão se registrar em uma ou mais montadoras e sempre que a montadora receber um novo pedido os observadores vão receber uma notificação com a quantidade.
      
 # PedroDev | 2023
