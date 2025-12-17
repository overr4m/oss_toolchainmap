import os
import yaml
from typing import Any, Dict, List


def load_table_data(env, table_config: List[Dict[str, Any]]) -> Dict[str, Any]:
    return build_table_data(env, table_config)


def get_root_dir(env) -> str:
    return os.path.dirname(env.conf["config_file_path"])


def load_yaml_absolute(env, rel_path: str) -> Any:
    root_dir = get_root_dir(env)
    full_path = os.path.join(root_dir, rel_path)
    with open(full_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _normalize_tools(raw: Any) -> List[Dict[str, Any]]:
    if isinstance(raw, dict):
        tools = raw.get("Tools")
        if isinstance(tools, list):
            return tools
    if isinstance(raw, list):
        return raw
    return []


def build_table_data(env, table_config: List[Dict[str, Any]]) -> Dict[str, Any]:
    data: Dict[str, Any] = {"table": []}

    for division in table_config:
        div_copy: Dict[str, Any] = dict(division)

        if "type" in div_copy:
            new_types: List[Dict[str, Any]] = []

            for tool_type in div_copy["type"]:
                type_copy: Dict[str, Any] = dict(tool_type)
                new_classes: List[Dict[str, Any]] = []

                for cls in tool_type.get("class", []):
                    cls_copy: Dict[str, Any] = dict(cls)

                    if "OSS_tools" in cls_copy:
                        oss_raw = load_yaml_absolute(env, cls_copy["OSS_tools"])
                        cls_copy["OSS_tools"] = _normalize_tools(oss_raw)

                    if "PS_tools" in cls_copy:
                        ps_raw = load_yaml_absolute(env, cls_copy["PS_tools"])
                        cls_copy["PS_tools"] = _normalize_tools(ps_raw)

                    new_classes.append(cls_copy)

                type_copy["class"] = new_classes
                new_types.append(type_copy)

            div_copy["type"] = new_types

        else:
            if "OSS_tools" in div_copy:
                oss_raw = load_yaml_absolute(env, div_copy["OSS_tools"])
                div_copy["OSS_tools"] = _normalize_tools(oss_raw)

            if "PS_tools" in div_copy:
                ps_raw = load_yaml_absolute(env, div_copy["PS_tools"])
                div_copy["PS_tools"] = _normalize_tools(ps_raw)

        data["table"].append(div_copy)

    return data
