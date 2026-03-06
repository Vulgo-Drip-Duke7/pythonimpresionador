# System Python PowerUp - Login

Página de login para o Sistema Python PowerUp.

## 🚀 Deploy no Vercel (Método Fácil)

### Passo 1: Criar Personal Access Token
1. Vá para [github.com/settings/tokens](https://github.com/settings/tokens)
2. Clique em "Generate new token (classic)"
3. Nome: `vercel-deploy`
4. Selecione: `repo` (Full control of private repositories)
5. Clique em "Generate token"
6. **COPIE O TOKEN IMEDIATAMENTE** (não poderá ver novamente!)

### Passo 2: Executar Setup Automático
1. **Duplo clique** no arquivo `setup_github.bat`
2. Cole seu **Personal Access Token**
3. Digite seu **usuário do GitHub**
4. Digite o nome do repositório (ex: `python-powerup-login`)

### Passo 3: Deploy no Vercel
1. Acesse [vercel.com](https://vercel.com)
2. Clique "New Project"
3. Conecte seu GitHub (já estará logado)
4. Selecione o repositório criado
5. Clique "Deploy" 🚀

## 📁 Arquivos Inclusos

- `index.html` - Página principal de login
- `assets/` - CSS, JS e imagens
- `vercel.json` - Configuração do Vercel
- `setup_github.bat` - Script de configuração automática

## 🧪 Teste Local

Para testar antes do deploy:
```bash
# Duplo clique em serve.bat
# OU execute:
python -m http.server 8000
```

Site ficará disponível em: http://localhost:8000

## ⚠️ Notas de Segurança

Esta é uma página de login estática. Para produção:
- Implemente autenticação no backend
- Use HTTPS (Vercel faz automaticamente)
- Configure CORS apropriadamente
- Valide dados no servidor
