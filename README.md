# 🚀 Sistema Python PowerUp - Backend Completo

Sistema completo de gerenciamento de produtos com **backend Python/Flask** e **frontend responsivo**.

## ✨ Funcionalidades

- ✅ **API RESTful** completa para produtos
- ✅ **Banco de dados SQLite** integrado
- ✅ **Frontend responsivo** com validação
- ✅ **CRUD completo**: Criar, Ler, Atualizar, Deletar produtos
- ✅ **Interface moderna** com design profissional
- ✅ **Deploy no Vercel** configurado

## 🛠️ Tecnologias

- **Backend**: Python + Flask + SQLite
- **Frontend**: HTML5 + CSS3 + JavaScript (ES6)
- **Banco**: SQLite3 (persistente)
- **Deploy**: Vercel + GitHub

## 🚀 Como Usar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o Sistema
```bash
python app.py
```

### 3. Acessar no Navegador
- **Página Inicial**: http://localhost:3001
- **Sistema de Produtos**: http://localhost:3001/produtos
- **API JSON**: http://localhost:3001/api/produtos

## 📊 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/produtos` | Lista todos os produtos |
| POST | `/api/produtos` | Cria novo produto |
| GET | `/api/produtos/:id` | Busca produto por ID |
| PUT | `/api/produtos/:id` | Atualiza produto |
| DELETE | `/api/produtos/:id` | Deleta produto |
| GET | `/api/stats` | Estatísticas dos produtos |

### Exemplo de Produto JSON:
```json
{
  "codigo": "PROD001",
  "marca": "Marca Exemplo",
  "tipo": "Eletrônico",
  "categoria": "Computadores",
  "preco": 2999.99,
  "custo": 1999.99,
  "observacao": "Produto em promoção"
}
```

## 🗄️ Banco de Dados

O sistema usa **SQLite** automaticamente:
- Arquivo: `produtos.db`
- Criado automaticamente na primeira execução
- Dados persistem entre reinicializações

### Estrutura da Tabela:
```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE NOT NULL,
    marca TEXT NOT NULL,
    tipo TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL DEFAULT 0,
    custo REAL DEFAULT 0,
    observacao TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🎨 Interface do Usuário

### Página de Produtos (`/produtos`)
- **Formulário de cadastro** com validação
- **Tabela responsiva** com todos os produtos
- **Ações**: Editar e Excluir produtos
- **Mensagens de status** em tempo real
- **Design moderno** com gradientes e animações

### Funcionalidades da Interface:
- ✅ Validação de campos obrigatórios
- ✅ Prevenção de códigos duplicados
- ✅ Formatação automática de preços
- ✅ Confirmação antes de excluir
- ✅ Feedback visual de loading
- ✅ Interface totalmente responsiva

## 🚀 Deploy no Vercel

### Passo 1: Preparar para Deploy
```bash
# Instalar dependências
pip install -r requirements.txt

# Testar localmente
python app.py
```

### Passo 2: Configurar Vercel
1. Vá para [vercel.com](https://vercel.com)
2. "New Project"
3. Conecte seu repositório GitHub `pythonimpresionador`
4. **Configurações automáticas** (Vercel detectará automaticamente):
   - **Framework**: Python
   - **Root Directory**: `./`
   - **Build Command**: Automático
   - **Output Directory**: Automático

### Passo 3: Deploy
- Clique em "Deploy"
- Aguarde o build (cerca de 2-3 minutos)
- ✅ **Site online!**

### Arquivos de Configuração
- `vercel.json` - Configuração do Vercel
- `api/index.py` - API Python para Vercel
- `api/requirements.txt` - Dependências Python

## 📁 Estrutura do Projeto

```
python-powerup/
├── app.py                 # Servidor Flask principal
├── requirements.txt       # Dependências Python
├── vercel.json           # Configuração Vercel
├── templates/            # Templates HTML
│   ├── index.html        # Página inicial
│   └── produtos.html     # Sistema de produtos
├── assets/               # CSS, JS, imagens
├── produtos.db          # Banco SQLite (criado automaticamente)
└── README.md            # Esta documentação
```

## 🔧 Desenvolvimento

### Adicionar Novos Campos
1. Modifique a tabela no `app.py` (função `init_db`)
2. Atualize o HTML em `templates/produtos.html`
3. Ajuste o JavaScript para os novos campos

### Personalizar Estilos
- Edite o CSS inline em `templates/produtos.html`
- Ou crie arquivos CSS separados na pasta `assets/`

## 🐛 Troubleshooting

### Erro: "Porta já em uso"
```bash
# Mata processos na porta 3001
netstat -ano | findstr :3001
taskkill /PID <PID> /F
```

### Erro: "Módulo não encontrado"
```bash
pip install flask flask-cors
```

### Banco não cria tabelas
- Delete `produtos.db`
- Reinicie o servidor

## 📈 Melhorias Futuras

- [ ] Autenticação de usuários
- [ ] Upload de imagens de produtos
- [ ] Relatórios e gráficos
- [ ] API de categorias separada
- [ ] Backup automático do banco
- [ ] Interface mobile nativa

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique os logs do terminal
2. Teste a API diretamente: `curl http://localhost:3001/api/produtos`
3. Abra uma issue no repositório

---

**🎉 Sistema pronto para uso profissional!**
- Configure CORS apropriadamente
- Valide dados no servidor
