# System Python PowerUp - Login

Página de login para o Sistema Python PowerUp.

## Funcionalidades

- Validação de formulário em tempo real
- Design responsivo
- Suporte a múltiplos idiomas (PT-BR)
- Integração com Google Tag Manager

## Deploy no Vercel

### Passo 1: Preparar o repositório Git
```bash
git init
git add .
git commit -m "Initial commit"
```

### Passo 2: Conectar com Vercel

**Opção 1: Via CLI**
```bash
npm i -g vercel
vercel
```

**Opção 2: Via Dashboard**
1. Acesse [vercel.com](https://vercel.com)
2. Clique em "New Project"
3. Conecte seu repositório do GitHub
4. Clique em "Deploy"

### Configuração Automática

O arquivo `vercel.json` já está configurado com:
- Cache de 1 hora para os assets
- Suporte a rotas
- Otimizações de performance

## Arquivos Inclusos

- `index.html` - Página principal de login
- `assets/` - CSS, JS e imagens
- `vercel.json` - Configuração do Vercel

## Notas de Segurança

⚠️ Esta é uma página de login estática. Para produção:
- Implemente autenticação no backend
- Use HTTPS (Vercel faz automaticamente)
- Configure CORS apropriadamente
- Valide dados no servidor

## Suporte

Para melhor desempenho online, certifique-se que:
- Todos os assets carregam corretamente
- Scripts externos (WebFont, GTM) estão acessíveis
- O design está responsivo em todos os dispositivos
