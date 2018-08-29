import pandas as pd 
import sys
import os.path

MAX_ROWS = 1000

pd.set_option('display.max_rows', MAX_ROWS)

#verifica se foi passado o argumento
try:
    filename = sys.argv[1]
except:
    print("filename required")
    sys.exit()

#verifica se o arquivo existe
if (os.path.exists(filename) == False): 
	print("filename required")
	sys.exit()


try:
    max_price = int(sys.argv[2])
except:
    max_price = 100


DELIMITER = ';'

#le o arquivo CSV
ceps = pd.read_csv(filename, DELIMITER)

SUBSET = ['AbsoluteMoneyCost']

#remove linhas com valores invalidos na coluna AbsoluteMoneyCost
ceps = ceps.dropna(subset = ['AbsoluteMoneyCost'], axis = 0)

#converte a coluna  AbsoluteMoneyCost para tipo float
ceps['AbsoluteMoneyCost'] = ceps['AbsoluteMoneyCost'].apply(lambda s: float(s.replace(',','.')))

#filtra valores de AbsoluteMoneyCost maiores que 100
filtrados_100 = ceps[ceps['AbsoluteMoneyCost'] > max_price]

print(filtrados_100[['ZipCodeStart','ZipCodeEnd','AbsoluteMoneyCost']])