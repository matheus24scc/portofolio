# portofolio

Portfólio pessoal de **Matheus Gabriel Schveitzer** — Web Designer & Desenvolvedor Front-End.
Repositório estático (HTML5, CSS3 e JavaScript puro) sem build system nem dependências.

## Conteúdo

Site de portfólio em `portfolio-web-designer/` que apresenta três projetos de
design/desenvolvimento front-end, cada um como um conjunto independente de
HTML/CSS/JS:

| Projeto | Pasta | Descrição |
| --- | --- | --- |
| Portfólio principal | `portfolio-web-designer/` | Landing page com seções Início, Sobre, Projetos e Contato (scroll suave via `script.js`). |
| TechStore | `portfolio-web-designer/techstore/` | Redesign conceitual de e-commerce de eletrônicos (`techstore_index.html` + `techstore_produtos.html`). |
| Café Aconchego | `portfolio-web-designer/cafe/` | Site institucional one-page para cafeteria. |
| Appoint | `portfolio-web-designer/appoint/` | Landing page para app de agendamentos. |

## Estrutura

```
portofolio/
├── README.md
└── portfolio-web-designer/
    ├── index.html              # landing do portfólio
    ├── style.css
    ├── script.js               # scroll suave para âncoras
    ├── appoint/                # projeto Appoint
    ├── cafe/                   # projeto Café Aconchego
    └── techstore/              # projeto TechStore (+ assets/img)
```

## Como visualizar

Não há etapa de build. Basta abrir o arquivo desejado no navegador, por exemplo:

```bash
# direto no navegador
xdg-open portfolio-web-designer/index.html

# ou servir localmente (opcional)
python3 -m http.server -d portfolio-web-designer 8000
# acesse http://localhost:8000/index.html
```

## Stack

- HTML5 semântico
- CSS3 (layout responsivo por pasta de projeto)
- JavaScript puro (sem frameworks/bundlers)

## Observações

- As imagens de capa dos cards em `index.html` usam o serviço externo
  `via.placeholder.com`. Esse serviço já apresentou instabilidade; para uso
  em produção, recomenda-se trocar por imagens locais em `assets/`.
- Nenhum segredo, chave de API ou dado sensível é versionado neste repositório.

## Licença

Veja [LICENSE](LICENSE).
