@echo off
echo ============================================
echo CONFIGURACAO GITHUB COM TOKEN
echo ============================================
echo.
echo PASSO 1: Crie um Personal Access Token em:
echo https://github.com/settings/tokens
echo.
echo Selecione: repo (Full control of private repositories)
echo.
echo PASSO 2: Cole seu token abaixo (sem espacos):
echo.
set /p TOKEN="Token: "

echo.
echo PASSO 3: Digite seu usuario do GitHub:
set /p USER="Usuario: "

echo.
echo PASSO 4: Digite o nome do repositorio:
set /p REPO="Repositorio: "

echo.
echo Configurando git...
git config --global credential.helper store
git remote add origin https://%USER%:%TOKEN%@github.com/%USER%/%REPO%.git

echo.
echo Testando conexao...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================
    echo SUCESSO! Repositorio enviado para GitHub
    echo ============================================
    echo.
    echo Agora va para: https://vercel.com
    echo 1. New Project
    echo 2. Import Git Repository
    echo 3. Selecione seu repositorio
    echo 4. Deploy!
    echo.
) else (
    echo.
    echo ERRO! Verifique seu token e tente novamente.
)

pause