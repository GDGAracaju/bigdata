import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    #tipo = record[0]
    #print record   
    titulo = record["title"]
    palavras = record['title'].split()
    for palavra in palavras:
        #mr.emit_intermediate(palavra, record)
        mr.emit_intermediate(palavra, 0)
        #for palavra2 in palavras:
        #    mr.emit_intermediate(palavra + palavra2, 0)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        total += 1
            
    posts = []
    posts.append([key,total])
    #for valor in list_of_values:
    #    #posts.append(valor["title"])
    #    #posts.append(valor)
    #    posts.append(total)
        
    mr.emit(posts)
    

#    mr.emit((key, total))
    
#    order = list_of_values[0]
#    juncao=[]
#    #for i in range(len(list_of_values)):
#    i = 1
#    while i < len(list_of_values):
#        juncao = []
#        #print order        
#        if i > 0:
#            for x in order:
#                juncao.append(x)
#
#            line_item = list_of_values[i]
#            for x in line_item:
#                juncao.append(x)
#
#            mr.emit(juncao)
#
#        i = i + 1
    

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

