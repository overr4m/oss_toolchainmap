from typing import Any, Dict, List

from .table_data import (
    load_table_data,
    build_table_data,
)
from .table_render import (
    render_tools_html,
)
from .export_tools_pdf import (
    main as export_tools_pdf,
)
from .build_search_data import (
    main as build_search_data,
    load_tools_from_file,
)

__all__ = [
    "load_table_data",
    "build_table_data",
    "render_tools_html",
    "export_tools_pdf",
    "build_search_data",
    "load_tools_from_file",
    "build_and_render_tools_table",
]

TableData = Dict[str, Any]


def build_and_render_tools_table(env: Any) -> str:
    """
    Построить данные таблицы по конфигурации MkDocs и вернуть HTML-фрагмент.
    """
    table_config: List[Dict[str, Any]] = env.conf.get("extra", {}).get(
        "table_config", []
    )
    _ = build_table_data(env, table_config)
    return render_tools_html()
