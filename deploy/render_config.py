#!/usr/bin/env python3
"""Renderiza a configuração local sem versionar segredos."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition("=")
        if not separator:
            raise ValueError(f"Linha inválida em {path}: {raw_line!r}")
        values[key.strip()] = value.strip()
    return values


env = load_env(ROOT / ".env")
master_password = env.get("ODOO_MASTER_PASSWORD")
if not master_password:
    raise SystemExit("ODOO_MASTER_PASSWORD não definido em .env")
postgres_user = env.get("POSTGRES_USER")
postgres_password = env.get("POSTGRES_PASSWORD")
if not postgres_user or not postgres_password:
    raise SystemExit("POSTGRES_USER/POSTGRES_PASSWORD não definidos em .env")

template = (ROOT / "deploy" / "odoo.conf").read_text(encoding="utf-8")
target = ROOT / "deploy" / "odoo.runtime.conf"
rendered = (
    template.replace("${ODOO_MASTER_PASSWORD}", master_password)
    .replace("${POSTGRES_USER}", postgres_user)
    .replace("${POSTGRES_PASSWORD}", postgres_password)
)
target.write_text(rendered, encoding="utf-8")
target.chmod(0o644)
print(target)