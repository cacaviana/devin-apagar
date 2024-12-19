```python
import csv

def calculate_average(column_name, file_name):
    # Inicializar variáveis para combater as somas e contagem de linhas
    total = 0
    count = 0

    # Abrindo o arquivo CSV usando o gerenciador de contexto
    with open(file_name, 'r') as file:
        # Criando o objeto leitor CSV
        csv_reader = csv.DictReader(file)
        
        # Verificando se o nome da coluna fornecido existe no arquivo
        if column_name not in csv_reader.fieldnames:
            raise ValueError(f"Coluna '{column_name}' não encontrada no arquivo CSV.")
        
        # Iterar sobre cada linha no arquivo CSV
        for row in csv_reader:
            # Converter o valor da coluna em float e adicioná-lo ao total
            try:
                total += float(row[column_name])
                count += 1
            except ValueError:
                # Caso o valor não possa ser convertido para float, ignorar esta linha
                continue

    # Calcular a média dividindo o total pela contagem de valores válidos
    if count == 0:
        return 0  # Evitar divisão por zero
    return total / count

# Exemplo de uso do script
file_name = 'dados.csv'
column_name = 'preco'
average = calculate_average(column_name, file_name)
print(f"A média da coluna '{column_name}' é: {average}")
```

Coloque isso em um arquivo `.py` e ajuste o `file_name` e `column_name` conforme necessário para refletir os dados em seu arquivo CSV específico. Este script lê o arquivo CSV, verifica se a coluna existe, processa cada linha, converte as entradas para floats e calcula a média, ignorando valores inválidos.