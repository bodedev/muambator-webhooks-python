# muambator-webhooks-python
Exemplo em Python para receber as notificações webhooks do Muambator.

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

Uma vez que você tenha habilitado as notificações na sua conta do Muambator, quando o sistema detectar mudanças no tracking dos pacotes, será enviado um webhook para o endereço configurado. 

Exemplo de uma requisição recebida pelo sistema:

```sh
(env)ironworld:muambator-webhooks-python ironworld$ python main.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 193-042-188
Código do pacote: RQ108584376MY
País de origem: Malásia
Operagora logística: correios
Número de dias: 23
Número de dias úteis: 15
Nome: Lanterna
Tags: aliexpress,cheap,flashlight
************************************************************
Data/Hora: 20/04/2017 10:27
Local: UNIDADE INTERNACIONAL CURITIBA - CURITIBA/PR
Situação: Recebido/Brasil
************************************************************
Data/Hora: 06/04/2017 13:24
Local: MALASIA Objeto encaminhado
Situação: Em trânsito para Unidade de Tratamento Internacional - BRASIL/BR
************************************************************
Data/Hora: 03/04/2017 18:17
Local: MALASIA
Situação: Objeto postado
127.0.0.1 - - [26/Apr/2017 15:39:49] "POST /webhook HTTP/1.1" 200 -
```