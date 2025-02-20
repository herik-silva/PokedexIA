# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /code

# Copie o arquivo requirements.txt para o container
COPY requirements.txt .

# Instale as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie o restante dos arquivos para o container
COPY . .

# Comando para rodar sua aplicação (exemplo)
CMD ["python", "main.py"]