mode=$1

if [ "$mode" = "help" ]; then
    echo "Executa a instalação das dependências e inicia o servidor"
    echo "Exemplo de uso: sh setup.sh gunicorn"
    echo "Parametros:"
    echo "- install: instala as dependências do projeto"
    echo "- gunicorn: executado no modo de produção utilizando gunicorn"
    echo "Por padrão é executado python main.py"
    exit 1
fi

if [ "$mode" = "install"]; then
    pip install --no-cache -r requirements.txt
    exit 1
fi

if [ "$mode" = "prod" ]; then
    gunicorn -w 4 -b 0.0.0.0:5000 main:app
    exit 1
fi

python main.py