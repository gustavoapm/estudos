
def calculate_checksum(data):
    soma=sum(data)
    r=[(soma<<24)%256,(soma<<16)%256,(soma<<8)%256,soma%256]
    print("Teste")
    print(r)
    return r

def check_checksum(data):
    soma=sum(data[0:-5])
    r=[(soma<<24)%256,(soma<<16)%256,(soma<<8)%256,soma%256]
    if data[-5]==r[0] and data[-4]==r[1] and data[-3]==r[2] and data[-2]==r[3] :
        return 1
    return 0



dados = [10, 20, 30, 40, 50]

# Calcula o checksum dos dados
checksum_calculado = calculate_checksum(dados)

# Adiciona o checksum calculado aos dados
dados_com_checksum = dados + checksum_calculado

# Imprime os dados com o checksum
print("Dados com checksum:", dados_com_checksum)

# Verifica se o checksum está correto
resultado_verificacao = check_checksum(dados_com_checksum)

# Imprime o resultado da verificação
if resultado_verificacao:
    print("Checksum correto! Os dados são válidos.")
else:
    print("Checksum incorreto! Os dados podem estar corrompidos.")