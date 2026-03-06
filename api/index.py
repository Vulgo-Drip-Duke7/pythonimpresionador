from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime
import os

app = Flask(__name__,
            static_folder='../assets',
            template_folder='../templates')
CORS(app)

# Configuração do banco de dados
DATABASE = os.path.join(os.path.dirname(__file__), '../produtos.db')

def get_db():
    """Conecta ao banco de dados SQLite"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa o banco de dados"""
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE NOT NULL,
                marca TEXT NOT NULL,
                tipo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL DEFAULT 0,
                custo REAL DEFAULT 0,
                observacao TEXT,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# Inicializar banco de dados
init_db()

@app.route('/')
def index():
    """Serve a página principal"""
    return render_template('index.html')

@app.route('/produtos')
def produtos_page():
    """Serve a página de produtos"""
    return render_template('produtos.html')

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    """Lista todos os produtos"""
    try:
        with get_db() as conn:
            produtos = conn.execute('SELECT * FROM produtos ORDER BY data_criacao DESC').fetchall()

        produtos_list = []
        for produto in produtos:
            produtos_list.append({
                'id': produto['id'],
                'codigo': produto['codigo'],
                'marca': produto['marca'],
                'tipo': produto['tipo'],
                'categoria': produto['categoria'],
                'preco': produto['preco'],
                'custo': produto['custo'],
                'observacao': produto['observacao'],
                'data_criacao': produto['data_criacao']
            })

        return jsonify({'produtos': produtos_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/produtos', methods=['POST'])
def create_produto():
    """Cria um novo produto"""
    try:
        data = request.get_json()

        # Validação
        required_fields = ['codigo', 'marca', 'tipo', 'categoria']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({'error': f'Campo obrigatório: {field}'}), 400

        with get_db() as conn:
            cursor = conn.execute('''
                INSERT INTO produtos (codigo, marca, tipo, categoria, preco, custo, observacao)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['codigo'].strip(),
                data['marca'].strip(),
                data['tipo'].strip(),
                data['categoria'].strip(),
                float(data.get('preco', 0)),
                float(data.get('custo', 0)),
                data.get('observacao', '').strip()
            ))

            produto_id = cursor.lastrowid
            conn.commit()

        return jsonify({
            'message': 'Produto criado com sucesso',
            'id': produto_id
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Código do produto já existe'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/produtos/<int:id>', methods=['GET'])
def get_produto(id):
    """Busca um produto por ID"""
    try:
        with get_db() as conn:
            produto = conn.execute('SELECT * FROM produtos WHERE id = ?', (id,)).fetchone()

        if not produto:
            return jsonify({'error': 'Produto não encontrado'}), 404

        return jsonify({
            'produto': {
                'id': produto['id'],
                'codigo': produto['codigo'],
                'marca': produto['marca'],
                'tipo': produto['tipo'],
                'categoria': produto['categoria'],
                'preco': produto['preco'],
                'custo': produto['custo'],
                'observacao': produto['observacao'],
                'data_criacao': produto['data_criacao']
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    """Atualiza um produto"""
    try:
        data = request.get_json()

        # Verificar se produto existe
        with get_db() as conn:
            existing = conn.execute('SELECT id FROM produtos WHERE id = ?', (id,)).fetchone()
            if not existing:
                return jsonify({'error': 'Produto não encontrado'}), 404

            # Atualizar
            conn.execute('''
                UPDATE produtos
                SET codigo = ?, marca = ?, tipo = ?, categoria = ?, preco = ?, custo = ?, observacao = ?
                WHERE id = ?
            ''', (
                data.get('codigo', '').strip(),
                data.get('marca', '').strip(),
                data.get('tipo', '').strip(),
                data.get('categoria', '').strip(),
                float(data.get('preco', 0)),
                float(data.get('custo', 0)),
                data.get('observacao', '').strip(),
                id
            ))
            conn.commit()

        return jsonify({'message': 'Produto atualizado com sucesso'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Código do produto já existe'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    """Deleta um produto"""
    try:
        with get_db() as conn:
            cursor = conn.execute('DELETE FROM produtos WHERE id = ?', (id,))
            if cursor.rowcount == 0:
                return jsonify({'error': 'Produto não encontrado'}), 404
            conn.commit()

        return jsonify({'message': 'Produto deletado com sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Estatísticas dos produtos"""
    try:
        with get_db() as conn:
            stats = conn.execute('''
                SELECT
                    COUNT(*) as total_produtos,
                    AVG(preco) as preco_medio,
                    SUM(preco) as valor_total_estoque,
                    COUNT(DISTINCT categoria) as total_categorias
                FROM produtos
            ''').fetchone()

        return jsonify({
            'total_produtos': stats['total_produtos'],
            'preco_medio': round(stats['preco_medio'] or 0, 2),
            'valor_total_estoque': round(stats['valor_total_estoque'] or 0, 2),
            'total_categorias': stats['total_categorias']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Para Vercel - função handler
def handler(event, context):
    return app(event, context)