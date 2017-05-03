# Muambator - Webhooks (Python)
Exemplo em Python para receber as notificações webhooks do [Muambator](http://www.muambator.com.br).

## Como instalar?

Nosso time indica que você utilize o virtualenv para evitar qualquer conflito com outras versões de sofwtare instalado no seu computador.

- Uma vez que o virtualenv já esteja instalado no seu computador, faça:
- Clone/download do repositório
- Via terminal/console, acesse a pasta onde foi feito o clone/download do repositório
- Ao acessar a pasta, execute:

```sh
# crie um novo ambiente para isolar a execução do código
virtualenv env
# ative o ambiente criado
source env/bin/activate
# instale as dependências
pip install -r requirements.txt
# execute o código
python main.py
```

## Como funciona?

Uma vez que você tenha habilitado as notificações na sua conta do [Muambator](http://www.muambator.com.br), quando o sistema detectar mudanças no tracking dos pacotes, será enviado um webhook para o endereço configurado. 

Exemplo do JSON de uma requisição recebida pelo sistema:

```json
{
  "PN691281769BR": {
    "pais_origem": "Brasil",
    "sigla_pais_origem": "br",
    "ultimo_tracking": {
      "map": "Porto Alegre, RS, Brasil",
      "datahora": "08/04/2017 11:49",
      "local": "CEE CENTRO - Porto Alegre/RS",
      "situacao": "Entrega Efetuada",
      "icone": "green"
    },
    "tags": [],
    "extraviado_ou_devolvido": false,
    "tributado": false,
    "ultimas_mudancas": [
      {
        "map": "Sao Paulo, SP, Brasil",
        "datahora": "31/03/2017 12:54",
        "local": "CTE SAUDE - Sao Paulo/SP Objeto encaminhado",
        "situacao": "Em tr\u00e2nsito para CTE PORTO ALEGRE - PORTO ALEGRE/RS",
        "icone": "orange"
      },
      {
        "map": "Sao Paulo, SP, Brasil",
        "datahora": "31/03/2017 10:21",
        "local": "AGF ADOLFO PINHEIRO - Sao Paulo/SP Objeto encaminhado",
        "situacao": "Em tr\u00e2nsito para CTE SAUDE - Sao Paulo/SP",
        "icone": "orange"
      },
      {
        "map": "Sao Paulo, SP, Brasil",
        "datahora": "30/03/2017 17:29",
        "local": "AGF ADOLFO PINHEIRO - Sao Paulo/SP",
        "situacao": "Objeto postado",
        "icone": "yellow"
      }
    ],
    "entregue": true,
    "arquivado": false,
    "icone": "",
    "numero_dias": 9,
    "marcado_como_entregue": false,
    "carrier": "correios",
    "nome": "",
    "codigo": "PN691281769BR",
    "numero_dias_uteis": 6
  }
}
```

## Tá, e como eu faço pra testar?

Já dizia o Chapolim Colorado:

> "Calma, calma, não priemos cânico." 

Nós já sabemos que você já fica tenso esperando seus pacotinhos, imagina esperando um pacote atualizar pra você receber uma notificação. Foi por isso que nós inventamos o super hiper mega boga "webhook personaltificator tester Muambator". Esse sistema é responsável por gerar mensagens para você testar sua  implementação. Como funciona? 

Uma vez que você tenha o webhook ativado na sua conta do Muambator, basta você acessar os detalhes de um pacote e depois clicar no pequeno ícone do sino. Esse clique irá gerar um webhook de testes baseado nos dados do pacote escolhido para você testar o seu sistema.

## Beleza! Mas e se meu computador não estiver "exposto" na Internet (leia-se, atrás de um NAT), o que posso fazer?

Você pode expor seu computador através de algum dos seguintes serviços apresentados abaixo:

- [ngrok](https://ngrok.com/)
- [localtunnel](https://localtunnel.github.io/www/)
- [portmap.io](https://portmap.io/)
- [pagekite](https://pagekite.net/)
- [openport](https://openport.io/)
- ​

## Beleza, vamos usar essa entronha. Há limites diários de notificações?

Não.

## Há! Mas se meu servidor está sempre muito ocupado e não está recebendo as mensagens?

Galera, processamos centenas de milhares de pacotes a cada 30 minutos em todo Muambator. Para evitar mais atrasos, temos um timeout de 5 segundos para cada tentativa de enviar uma notificação webhook.

## Quais são os IPs que irão apresentar a notificação?

Depende do dia. Nossa infra-estrutura é composta de diversas máquinas espalhadas ao redor do mundo para ajudar na árdua tarefa de procurar atualizações. Como alocamos diversas máquinas dinamicamente, não podemos garantir quais serão esses IPs.

## Eu to cheio de dúvida. Também tenho um monte de sugestões ou ideias novas para melhorar a plataforma. #comofaz?

Faz o seguinte, traz uma cerveja aqui no escritório numa tarde que a gente conversa pessoalmente. Combinado? Mas caso você seja um burocrata, ou esteja a algumas milhas de distância, por favor, registre o seu [contato](http://www.muambator.com.br/contato/).
