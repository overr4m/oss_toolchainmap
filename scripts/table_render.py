from typing import Any, Dict, List

def _chunk_tools(tools: List[Dict[str, Any]], size: int = 5) -> List[List[Dict[str, Any]]]:
    """Разбить список инструментов на чанки фиксированного размера."""
    return [tools[i : i + size] for i in range(0, len(tools), size)]

def render_table(data: Dict[str, Any]) -> str:
    """Построить HTML-таблицу по структуре data['table']."""
    html: List[str] = ['<table border="1" style="border-collapse: collapse;">']
    html.append(
        """<thead>
                <tr>
                    <th>Разделение</th>
                    <th>Тип</th>
                    <th>Класс</th>
                    <th colspan="5">Проприетарное ПО</th>  
                    <th colspan="5">Свободное ПО</th>
                </tr>
            </thead>"""
    )
    html.append("<tbody>")

    for division in data.get("table", []):
        div_name = division.get("division", "")
        has_types = "type" in division

        # Разделы без вложенных типов/классов
        if not has_types:
            ps_tools = division.get("PS_tools", []) or []
            oss_tools = division.get("OSS_tools", []) or []

            ps_chunks = _chunk_tools(ps_tools, 5)
            oss_chunks = _chunk_tools(oss_tools, 5)
            max_rows = max(len(ps_chunks), len(oss_chunks), 1)

            for i in range(max_rows):
                html.append("<tr>")

                if i == 0:
                    html.append(f'<td rowspan="{max_rows}" colspan="3">{div_name}</td>')

                ps_tools_row = ps_chunks[i] if i < len(ps_chunks) else []
                for tool in ps_tools_row:
                    html.append(f'<td>{tool.get("name", "")}</td>')
                if len(ps_tools_row) < 5:
                    html.append(f'<td colspan="{5 - len(ps_tools_row)}"></td>')

                oss_tools_row = oss_chunks[i] if i < len(oss_chunks) else []
                for tool in oss_tools_row:
                    html.append(f'<td>{tool.get("name", "")}</td>')
                if len(oss_tools_row) < 5:
                    html.append(f'<td colspan="{5 - len(oss_tools_row)}"></td>')

                html.append("</tr>")

        # Разделы с type/class
        else:
            type_rows: List[Dict[str, Any]] = []

            for tool_type in division.get("type", []):
                type_name = tool_type.get("name", "")
                for cls in tool_type.get("class", []):
                    class_name = cls.get("name", "")

                    ps_tools = cls.get("PS_tools", []) or []
                    oss_tools = cls.get("OSS_tools", []) or []

                    ps_chunks = _chunk_tools(ps_tools, 5)
                    oss_chunks = _chunk_tools(oss_tools, 5)
                    max_rows = max(len(ps_chunks), len(oss_chunks), 1)

                    for i in range(max_rows):
                        type_rows.append(
                            {
                                "type_name": type_name,
                                "class_name": class_name,
                                "ps_tools": ps_chunks[i] if i < len(ps_chunks) else [],
                                "oss_tools": oss_chunks[i] if i < len(oss_chunks) else [],
                            }
                        )

            for i, row in enumerate(type_rows):
                html.append("<tr>")

                if i == 0:
                    html.append(f'<td rowspan="{len(type_rows)}">{div_name}</td>')

                if i == 0 or row["type_name"] != type_rows[i - 1]["type_name"]:
                    type_rowspan = sum(1 for r in type_rows if r["type_name"] == row["type_name"])
                    html.append(f'<td rowspan="{type_rowspan}">{row["type_name"]}</td>')

                if i == 0 or row["class_name"] != type_rows[i - 1]["class_name"]:
                    class_rowspan = sum(1 for r in type_rows if r["class_name"] == row["class_name"])
                    html.append(f'<td rowspan="{class_rowspan}">{row["class_name"]}</td>')

                ps_tools_row = row["ps_tools"]
                for tool in ps_tools_row:
                    html.append(f'<td>{tool.get("name", "")}</td>')
                if len(ps_tools_row) < 5:
                    html.append(f'<td colspan="{5 - len(ps_tools_row)}"></td>')

                oss_tools_row = row["oss_tools"]
                for tool in oss_tools_row:
                    html.append(f'<td>{tool.get("name", "")}</td>')
                if len(oss_tools_row) < 5:
                    html.append(f'<td colspan="{5 - len(oss_tools_row)}"></td>')

                html.append("</tr>")

    html.append("</tbody></table>")
    return "\n".join(html)
