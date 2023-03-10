from typing import Any, Dict


def get_option_value(req: Dict[str, Any], option: str):
    inputs = list(req.get("data").get("options"))
    for input in inputs:
        if input.get("name") == option:
            return input.get("value")
