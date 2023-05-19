tamanho_arquivo = float(input("Digite o tamanho do arquivo para download em MB: "))
velocidade_internet = float(input("Digite a velocidade do link de Internet em Mbps: "))

# Conversão de MB para Mbps
tamanho_arquivo_bits = tamanho_arquivo * 8 * 1024 * 1024

# Cálculo do tempo de download em segundos
tempo_download_segundos = tamanho_arquivo_bits / (velocidade_internet * 1024 * 1024)

# Conversão de segundos para minutos
tempo_download_minutos = tempo_download_segundos / 60

print("O tempo aproximado de download é de", tempo_download_minutos, "minutos.")
