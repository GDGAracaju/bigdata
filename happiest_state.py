#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import re
import operator

def hw(sent_file, tweet_file):
    linhas = tweet_file.readlines()
    dicionario = sent_file.readlines()
    dic = {}
    for linhadic in dicionario:
        sentiment, score = linhadic.split('\t')
        dic[re.compile(r"\b%s\b" % sentiment)] = int(score)	

    estados = {}
    for linha in linhas:
        #decoded = json.loads(linha, object_hook=_decode_dict)
        decoded = json.loads(linha)
        pontos = 0.0
        if 'text' in decoded:
            coordenadas = []
            estado = ""
            temCordenadas = 0
            if 'coordinates' in decoded:
                cord = decoded[u'coordinates']
                if cord <> None:
                    #print cord

                    #posicao = [u'type'[u'Point'[u'coordinates']]]
                    tipo = cord[u'type']
                    if tipo == 'Point':
                        coordenadas = cord[u'coordinates']
                        lati, longi = coordenadas
                        #print lati
                        #print longi

                user = decoded[u'user']
                user_id = user[u'id']
                user_name = user[u'name']
                screen_name = user[u'screen_name']
                #print user_id
                #print user_name.encode('utf-8')
                #print screen_name.encode('utf-8')
                #print

            # Pegar do Campo PLACE
            if 'place' in decoded:
                localizacao = decoded[u'place']
                if localizacao <> None:
                    pais = localizacao[u'country']
                    pais_codigo = localizacao[u'country_code']
                    pais_completo = localizacao[u'full_name']
                    #
                    if pais_codigo == "US" or pais_codigo == "BR":
                        #print pais_completo.encode('utf-8')
                        estado = pais_completo.encode('utf-8')[-4:]
                        if estado[:1] == ',':
                            estado = estado.encode('utf-8')[-2:]
                            if estado <> 'US':
                                #print localizacao
                                #print pais_completo.encode('utf-8')
                                #print estado                       
                                temCordenadas = 1

            if temCordenadas == 0:
                estado = 'ND'
                temCordenadas = 1

            if temCordenadas == 1:
                frase = decoded[u'text'].lower()
                print frase.encode('utf-8')
                ponto = 0.0
                for sent, score in dic.items():
                    count = len(sent.findall(frase))
                    palavra1 = sent.pattern[2:][:-2]
                
                    if count > 0:
                        ponto += count*score
                        print ponto

                #estados[estado] = ponto
                if estado in estados:
                   estados[estado] += ponto
                else:
                   estados[estado] = ponto

    estados_x = sorted(estados.iteritems(), key=operator.itemgetter(1), reverse=True)
    contador = 1
    for esta, pont in estados_x:        
        print "%s "%(esta.replace(' ', '%20').encode('utf-8')) + ' ' + str(pont)
        contador += 1


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file , tweet_file)

if __name__ == '__main__':
    main()
