import sys
import json
import re
from collections import defaultdict
import operator
import unicodedata
import ast

def hw(tweet_file):
    linhas   = tweet_file.readlines() 
    contador = 0   
    totalitens = 0
    freq = {}
    publicacoes = {}
    horas = {}
    for linha in linhas:
        contador = contador + 1
        json_data = ast.literal_eval(linha) 
        post = json_data
        #print post['title']
        #print post['object']['content']
        palavras = post['title'].split()
        publicado = post['published'][0:10]
        hora = post['published'][11:13]
        #print publicado
        #print hora
        if publicado in publicacoes:
            publicacoes[publicado] += 1.0
        else:
            publicacoes[publicado] = 1.0

        if hora in horas:
            horas[hora] += 1.0
        else:
            horas[hora] = 1.0

        for word in palavras:
            totalitens += 1
            word2 = word
            word2 = word2.replace('.', ' ')
            word2 = word2.replace(',', ' ')
            word2 = word2.replace('-', ' ')
            word2 = word2.replace('(', ' ')
            word2 = word2.replace(')', ' ')
            word2 = word2.lower().strip()
            if len(word2) >= 3:
                if word2 in freq:
                   freq[word2] += 1.0
                else:
                   freq[word2] = 1.0

    freq_x = sorted(freq.iteritems(), key=operator.itemgetter(1), reverse=True)
    for word, valor in freq_x:
        print "%s \t\t\t\t\t%.4f"%(word.replace(' ', '%20'),valor )

    publicacoes_o = sorted(publicacoes.iteritems(), key=operator.itemgetter(1), reverse=True)
    for data, valor in publicacoes_o:
        print "%s \t\t\t\t\t%.4f"%(data.replace(' ', '%20'),valor )

    horass_o = sorted(horas.iteritems(), key=operator.itemgetter(0), reverse=False)
    for hora, valor in horass_o:
        print "%s \t\t\t\t\t%.4f"%(hora.replace(' ', '%20'),valor )

    #print "%s \t\t\t%.4f"%('Total de Palavras : ' , totalitens )

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
