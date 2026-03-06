@echo off
echo ============================================
echo TESTE DA API - SISTEMA PYTHON POWERUP
echo ============================================
echo.

REM Testa se o servidor está rodando
curl -s http://localhost:3001/api/produtos >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ ERRO: Servidor nao esta rodando!
    echo.
    echo Execute primeiro: python app.py
    echo Ou duplo clique em: iniciar_backend.bat
    pause
    exit /b 1
)

echo ✅ Servidor esta rodando!
echo.
echo Testando API...
echo.

echo 📊 GET /api/produtos (Listar produtos):
curl -s http://localhost:3001/api/produtos | jq . 2>nul || curl -s http://localhost:3001/api/produtos
echo.
echo.

echo ➕ POST /api/produtos (Criar produto):
curl -s -X POST http://localhost:3001/api/produtos ^
  -H "Content-Type: application/json" ^
  -d "{\"codigo\":\"TEST001\",\"marca\":\"Marca Teste\",\"tipo\":\"Tipo Teste\",\"categoria\":\"Categoria Teste\",\"preco\":99.99,\"custo\":49.99,\"observacao\":\"Produto de teste\"}" | jq . 2>nul || echo "Produto criado (sem jq para formatar)"
echo.
echo.

echo 📊 GET /api/produtos (Verificar se foi criado):
curl -s http://localhost:3001/api/produtos | jq . 2>nul || curl -s http://localhost:3001/api/produtos
echo.
echo.

echo 🎯 GET /api/stats (Estatisticas):
curl -s http://localhost:3001/api/stats | jq . 2>nul || curl -s http://localhost:3001/api/stats
echo.
echo.

echo ✅ Testes concluídos!
echo.
echo 🌐 Acesse no navegador:
echo - http://localhost:3001 (Página inicial)
echo - http://localhost:3001/produtos (Sistema completo)
echo.
pause