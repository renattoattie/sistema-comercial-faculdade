#!/usr/bin/env bash
set -euo pipefail
exec cloudflared tunnel --no-autoupdate --url http://127.0.0.1:8069
