import sys, requests, re

if len(sys.argv) > 2:
    tag = sys.argv[1] 
    link = sys.argv[2]

    response = requests.get(link, headers={'User-Agent': None})
    if response.ok:
        cupons = re.findall('(?:{})(\w*)'.format(tag), response.text)

        for cupom in cupons:
            print(cupom)
else:
    print('Insira os argumentos tag e link como descrito no README!')