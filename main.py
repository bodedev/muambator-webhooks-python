# -*- coding: utf-8 -*-


from flask import Flask, request


app = Flask(__name__)
POST_METHOD = "POST"


@app.route('/webhook', methods=[POST_METHOD])
def webhook_handler():
    pacotes = request.get_json()
    for codigo_pacote, informacoes in pacotes.items():
        print(u"Código do pacote: %s" % codigo_pacote)
        print(u"País de origem: %s" % informacoes["pais_origem"])
        print(u"Operagora logística: %s" % informacoes["carrier"])
        print(u"Número de dias: %d" % informacoes["numero_dias"])
        print(u"Número de dias úteis: %d" % informacoes["numero_dias_uteis"])
        print(u"Nome: %s" % informacoes["nome"])
        if informacoes["tags"]:
            print("Tags: %s" % ",".join(informacoes["tags"]))
        for atualizacao in informacoes["ultimas_mudancas"]:
            print(60 * "*")
            print(u"Data/Hora: %s" % atualizacao["datahora"])
            print(u"Local: %s" % atualizacao["local"])
            print(u"Situação: %s" % atualizacao["situacao"])
    return "OK"


if __name__ == "__main__":
    # Inicia a execução do Flask
    app.run(host='0.0.0.0', debug=True)
