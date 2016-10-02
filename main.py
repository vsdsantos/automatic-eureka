import requests
import random

# Generates a question and a response based on a given word
# TODO recognition of gender | tell a little small talk introduction
def gen(word):
    resp = raw_input("Conhece o(a) %s? (S/N) " % word)
    if resp in ['S', 's']:
        print ':('
    elif resp in ['N', 'n']:
        print "Que " + find_expr(word)

# Match an given word to an expression which rhymes
# TODO map person names to things names (dictionary API? http://www.dicionario-aberto.net/estaticos/api.html )
def find_expr(word):
    URI = 'http://dicionario-aberto.net'
    r = requests.get(URI + "/search-json?suffix=%s&like=%s" % (word[-4:], word))
    l = r.json()['list']
    random.shuffle(l)
    return 'encheu seu cu de ' + l[0]

# x = raw_input('Digite um nome: ')
# gen(x)
gen('Aguinaldo')
