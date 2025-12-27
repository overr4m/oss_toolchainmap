"""MkDocs render"""

from typing import Any, Dict, List

from scripts.table_data import (
    build_table_data,
    load_table_data,
    load_yaml_absolute,
)
from scripts.table_render import render_table


def define_env(env: Any) -> None:
    """MkDocs plugin"""
    table_config: List[Dict[str, Any]] = (
        env.conf.get("extra", {}).get("tools_table", [])
    )

    @env.macro
    def tools_table() -> str:
        """Render YAML"""
        data: Dict[str, Any] = load_table_data(env, table_config)
        return render_table(data)

    @env.macro
    def generate_html_table_from_config() -> str:
        """Build table data"""
        table_data: Dict[str, Any] = build_table_data(env, table_config)
        return render_table(table_data)

    @env.macro
    def load_yaml(file_path: str) -> Any:
        """YAML"""
        return load_yaml_absolute(env, file_path)
