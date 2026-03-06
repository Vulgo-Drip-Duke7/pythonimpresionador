@echo off
echo ============================================
echo SISTEMA PYTHON POWERUP - INICIAR BACKEND
echo ============================================
echo.
echo Este script inicia o backend Python/Flask
echo com banco de dados SQLite integrado.
echo.
echo URLs de acesso:
echo - Frontend: http://localhost:3001
echo - Sistema Produtos: http://localhost:3001/produtos
echo - API: http://localhost:3001/api/produtos
echo.
echo Pressione Ctrl+C para parar o servidor
echo.
python app.py
pause