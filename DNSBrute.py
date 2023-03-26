import dns.resolver, os
os.system('clear')
#cores
vermelho = '\033[41m'
verde = '\033[42m'
nulo = '\033[0m'
verde1 = '\033[32m'
vermelho1 = '\033[31m'
azul = '\033[0;30;34m'
rosa = '\033[0;30;35m'
amarelo = '\033[31m'
#banner e by

print(f"""{verde1}╭━━━╮╭━╮╱╭╮╭━━━╮{nulo}   {vermelho1}╭━━╮╱╭━━━╮╭╮╱╭╮╭━━━━╮╭━━━╮{nulo}
{verde1}╰╮╭╮┃┃┃╰╮┃┃┃╭━╮┃{nulo}   {vermelho1}┃╭╮┃╱┃╭━╮┃┃┃╱┃┃┃╭╮╭╮┃┃╭━━╯{nulo}
{verde1}╱┃┃┃┃┃╭╮╰╯┃┃╰━━╮{nulo}   {vermelho1}┃╰╯╰╮┃╰━╯┃┃┃╱┃┃╰╯┃┃╰╯┃╰━━╮{nulo}
{verde1}╱┃┃┃┃┃┃╰╮┃┃╰━━╮┃{nulo}   {vermelho1}┃╭━╮┃┃╭╮╭╯┃┃╱┃┃╱╱┃┃╱╱┃╭━━╯{nulo}
{verde1}╭╯╰╯┃┃┃╱┃┃┃┃╰━╯┃{nulo}   {vermelho1}┃╰━╯┃┃┃┃╰╮┃╰━╯┃╱╱┃┃╱╱┃╰━━╮{nulo}
{verde1}╰━━━╯╰╯╱╰━╯╰━━━╯{nulo}   {vermelho1}╰━━━╯╰╯╰━╯╰━━━╯╱╱╰╯╱╱╰━━━╯{nulo}""")
#menu
escolha = -1

while escolha < 1 or escolha > 2:
    escolha = int(input(f"""
{amarelo}[{nulo}{rosa} 1 {nulo}{amarelo}]{nulo} {amarelo}={nulo} {verde1}DnsBrute{nulo}
{amarelo}[{nulo}{rosa} 2 {nulo}{amarelo}]{nulo} {amarelo}={nulo} {vermelho1}exit{nulo}
\033[0;30;34m┌──(DNS㉿BRUTE!)-[~]
└─>\033[0;30;0m """))
    print(''' ''')
#escolha
if escolha == 1:
    os.system('clear')
    print(f"""{verde1}╭━━━╮╭━╮╱╭╮╭━━━╮{nulo}   {vermelho1}╭━━╮╱╭━━━╮╭╮╱╭╮╭━━━━╮╭━━━╮{nulo}
{verde1}╰╮╭╮┃┃┃╰╮┃┃┃╭━╮┃{nulo}   {vermelho1}┃╭╮┃╱┃╭━╮┃┃┃╱┃┃┃╭╮╭╮┃┃╭━━╯{nulo}
{verde1}╱┃┃┃┃┃╭╮╰╯┃┃╰━━╮{nulo}   {vermelho1}┃╰╯╰╮┃╰━╯┃┃┃╱┃┃╰╯┃┃╰╯┃╰━━╮{nulo}
{verde1}╱┃┃┃┃┃┃╰╮┃┃╰━━╮┃{nulo}   {vermelho1}┃╭━╮┃┃╭╮╭╯┃┃╱┃┃╱╱┃┃╱╱┃╭━━╯{nulo}
{verde1}╭╯╰╯┃┃┃╱┃┃┃┃╰━╯┃{nulo}   {vermelho1}┃╰━╯┃┃┃┃╰╮┃╰━╯┃╱╱┃┃╱╱┃╰━━╮{nulo}
{verde1}╰━━━╯╰╯╱╰━╯╰━━━╯{nulo}   {vermelho1}╰━━━╯╰╯╰━╯╰━━━╯╱╱╰╯╱╱╰━━━╯{nulo}
(exemplo site: youtube.com)""")
    res = dns.resolver.Resolver()
    alvo = input('''\033[0;30;34m┌──(DNS㉿BRUTE!)-[~]
└─>\033[0;30;0m ''')

    Arquivo = open("lista.txt", "r")
    subs = Arquivo.read().splitlines()

    for subs in subs:
        try:
            sub_alvo = subs + "." + alvo
            Resultado = res.resolve(sub_alvo, "A")
            for ip in Resultado:
                print(f'{verde}', sub_alvo, "--> ", f'{ip} ON{nulo}')
                input('Press enter...')
        except:
            print(f'{vermelho}', sub_alvo, f'OFF!{nulo}')
elif escolha == 2:
    print(f'{vermelho1}Saindo...{nulo}')
    exit()

else:
    print('Erro. Tente novamente.')