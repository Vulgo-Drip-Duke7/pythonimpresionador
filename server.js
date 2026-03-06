const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Servir arquivos estáticos do frontend
app.use(express.static(path.join(__dirname)));

// Banco de dados SQLite
const db = new sqlite3.Database('./produtos.db', (err) => {
    if (err) {
        console.error('Erro ao conectar ao banco de dados:', err.message);
    } else {
        console.log('Conectado ao banco de dados SQLite.');
        criarTabelaProdutos();
    }
});

// Criar tabela de produtos
function criarTabelaProdutos() {
    const sql = `
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            marca TEXT,
            tipo TEXT,
            categoria TEXT,
            preco REAL,
            custo REAL,
            observacao TEXT,
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    `;

    db.run(sql, (err) => {
        if (err) {
            console.error('Erro ao criar tabela:', err.message);
        } else {
            console.log('Tabela produtos criada/verificada com sucesso.');
        }
    });
}

// Rotas da API

// GET /api/produtos - Listar todos os produtos
app.get('/api/produtos', (req, res) => {
    const sql = 'SELECT * FROM produtos ORDER BY data_criacao DESC';

    db.all(sql, [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json({ produtos: rows });
    });
});

// POST /api/produtos - Criar novo produto
app.post('/api/produtos', (req, res) => {
    const { codigo, marca, tipo, categoria, preco, custo, observacao } = req.body;

    // Validação básica
    if (!codigo || !marca || !tipo || !categoria) {
        return res.status(400).json({
            error: 'Campos obrigatórios: codigo, marca, tipo, categoria'
        });
    }

    const sql = `
        INSERT INTO produtos (codigo, marca, tipo, categoria, preco, custo, observacao)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    `;

    const params = [codigo, marca, tipo, categoria, preco || 0, custo || 0, observacao || ''];

    db.run(sql, params, function(err) {
        if (err) {
            if (err.message.includes('UNIQUE constraint failed')) {
                res.status(409).json({ error: 'Código do produto já existe' });
            } else {
                res.status(500).json({ error: err.message });
            }
            return;
        }

        res.json({
            message: 'Produto criado com sucesso',
            id: this.lastID,
            produto: {
                id: this.lastID,
                codigo,
                marca,
                tipo,
                categoria,
                preco: preco || 0,
                custo: custo || 0,
                observacao: observacao || '',
                data_criacao: new Date().toISOString()
            }
        });
    });
});

// PUT /api/produtos/:id - Atualizar produto
app.put('/api/produtos/:id', (req, res) => {
    const { id } = req.params;
    const { codigo, marca, tipo, categoria, preco, custo, observacao } = req.body;

    const sql = `
        UPDATE produtos
        SET codigo = ?, marca = ?, tipo = ?, categoria = ?, preco = ?, custo = ?, observacao = ?
        WHERE id = ?
    `;

    const params = [codigo, marca, tipo, categoria, preco || 0, custo || 0, observacao || '', id];

    db.run(sql, params, function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }

        if (this.changes === 0) {
            res.status(404).json({ error: 'Produto não encontrado' });
            return;
        }

        res.json({ message: 'Produto atualizado com sucesso' });
    });
});

// DELETE /api/produtos/:id - Deletar produto
app.delete('/api/produtos/:id', (req, res) => {
    const { id } = req.params;

    const sql = 'DELETE FROM produtos WHERE id = ?';

    db.run(sql, id, function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }

        if (this.changes === 0) {
            res.status(404).json({ error: 'Produto não encontrado' });
            return;
        }

        res.json({ message: 'Produto deletado com sucesso' });
    });
});

// GET /api/produtos/:id - Buscar produto por ID
app.get('/api/produtos/:id', (req, res) => {
    const { id } = req.params;
    const sql = 'SELECT * FROM produtos WHERE id = ?';

    db.get(sql, [id], (err, row) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }

        if (!row) {
            res.status(404).json({ error: 'Produto não encontrado' });
            return;
        }

        res.json({ produto: row });
    });
});

// Rota para servir o frontend
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Tratamento de erros
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Erro interno do servidor' });
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`🚀 Servidor rodando em http://localhost:${PORT}`);
    console.log(`📊 API disponível em http://localhost:${PORT}/api/produtos`);
});

process.on('SIGINT', () => {
    db.close((err) => {
        if (err) {
            console.error('Erro ao fechar banco de dados:', err.message);
        } else {
            console.log('Banco de dados fechado.');
        }
        process.exit(0);
    });
});