"""Модуль CLI:

- build_search_ сборка JSON-индекса инструментов из YAML.
- export_tools_pdf: экспорт HTML‑таблицы инструментов в PDF.
- table_ подготовка данных таблицы для MkDocs.
- table_render: рендер HTML‑таблицы инструментов.
"""

from __future__ import annotations

import sys

from .build_search_data import main as build_search_index
from .export_tools_pdf import main as export_tools_pdf
from .table_data import build_table_data, load_table_data
from .table_render import render_table, render_tools_html

__all__ = [
    "build_search_index",
    "export_tools_pdf",
    "build_table_data",
    "load_table_data",
    "render_table",
    "render_tools_html",
]


def main() -> None:
    """CLI‑роутер"""

    commands = {
        "build-search": build_search_index,
        "export-pdf": export_tools_pdf,
    }

    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help"}:
        available = ", ".join(commands)
        print(
            f"Использование: python -m scripts <команда>\n"
            f"Доступные команды: {available}"
        )
        raise SystemExit(0)

    cmd = sys.argv[1]
    if cmd not in commands:
        available = ", ".join(commands)
        print(
            "Неизвестная команда: "
            f"{cmd}\nДоступные команды: {available}"
        )

        raise SystemExit(1)

    commands[cmd]()


if __name__ == "__main__":
    main()
