import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "custom_addons" / "modern_dark_backend"


class ModernDarkThemeTests(unittest.TestCase):
    def test_module_declares_backend_theme_asset(self):
        manifest_path = MODULE / "__manifest__.py"
        self.assertTrue(manifest_path.exists(), "manifesto do tema ainda não existe")
        manifest = ast.literal_eval(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["depends"], ["web"])
        self.assertIn(
            "modern_dark_backend/static/src/scss/backend.scss",
            manifest["assets"]["web.assets_backend"],
        )

    def test_styles_cover_navigation_workspace_and_controls(self):
        stylesheet = MODULE / "static" / "src" / "scss" / "backend.scss"
        self.assertTrue(stylesheet.exists(), "folha de estilo do tema ainda não existe")
        css = stylesheet.read_text(encoding="utf-8")
        for selector in (".o_main_navbar", ".o_action_manager", ".o_control_panel", ".btn-primary"):
            self.assertIn(selector, css)
        for color in ("#111318", "#1b1e24", "#d7d9df"):
            self.assertIn(color, css)

    def test_runtime_loads_custom_addons_before_upstream(self):
        compose = (ROOT / "compose.yaml").read_text(encoding="utf-8")
        config = (ROOT / "deploy" / "odoo.conf").read_text(encoding="utf-8")
        self.assertIn("./custom_addons:/mnt/custom-addons:ro", compose)
        self.assertIn(
            "addons_path = /mnt/custom-addons,/mnt/extra-addons",
            config,
        )


if __name__ == "__main__":
    unittest.main()
