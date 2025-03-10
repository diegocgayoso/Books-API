# Books API with Flask

Uma API simples para gerenciamento de livros, desenvolvida em **Flask** (Python), com operações básicas de CRUD. Ideal para estudos ou como base para projetos mais complexos.

---

## 🚀 Funcionalidades

- **Listar todos os livros** (`GET /books`)
- **Buscar livro por ID** (`GET /books/<id>`)
- **Adicionar novo livro** (`POST /books`)
- **Atualizar livro existente** (`PUT /books/<id>`)
- **Excluir livro** (`DELETE /books/<id>`)

---

## ⚙️ Tecnologias Utilizadas
- **Python** + **Flask** (Framework web)
- **Flask JSONify** (Para respostas em formato JSON)
- Armazenamento em memória (dados voláteis, reiniciam com o servidor).

---

## 📦 Como Usar

### Pré-requisitos
- Python 3.x instalado
- Flask instalado: `pip install flask`

### Executando a API
1. Clone o repositório ou copie o código em `app.py`.
2. No terminal, execute:
   ```bash
   python app.py
