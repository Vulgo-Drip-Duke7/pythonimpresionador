@echo off
REM Script para servir o site localmente para testes
REM Usando Python se disponível

echo Iniciando servidor local...
echo O site estará disponível em: http://localhost:8000

REM Tenta Python 3
python -m http.server 8000

REM Se não funcionar, tenta Python 2
if %ERRORLEVEL% NEQ 0 (
    python -m SimpleHTTPServer 8000
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Erro: Python não encontrado!
    echo Por favor, instale Python de: https://www.python.org/downloads/
    pause
)
