# Sistema Comercial Faculdade — Odoo 19 Community

Implantação local com Docker Compose, PostgreSQL 16 e Odoo 19 Community.

## Iniciar

1. Copie `.env.example` para `.env` e troque todas as senhas.
2. Gere a configuração local: `python3 deploy/render_config.py`.
3. Suba o banco: `docker compose up -d db`.
4. Inicialize a base na primeira execução:
   `docker compose run --rm odoo --config=/etc/odoo/odoo.conf -d sistema_comercial_faculdade -i base,crm,sale_management,purchase,stock,account --without-demo --stop-after-init`.
5. Suba o Odoo: `docker compose up -d odoo`.
6. Acesse `http://127.0.0.1:8069`.

O módulo `modern_dark_backend` aplica o tema Modern Graphite Light, com
navegação grafite e área de trabalho clara para preservar contraste e legibilidade.

O arquivo `.env` é ignorado pelo Git e não deve ser versionado. O túnel rápido da Cloudflare é temporário: sua URL muda quando o processo é reiniciado.

## Parar

`docker compose down`

Para remover também banco e arquivos persistidos: `docker compose down -v`.

## Origem

Código-base: Odoo Community 19.0, licenciado sob LGPL-3. Consulte `LICENSE` e `COPYRIGHT`.
