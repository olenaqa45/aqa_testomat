import json


def get_cookies(storage_state_path: str) -> list[dict]:
    with open(storage_state_path) as f:
        return json.load(f)["cookies"]


def get_cookie(storage_state_path: str, name: str) -> dict | None:
    for cookie in get_cookies(storage_state_path):
        if cookie["name"] == name:
            return cookie
    return None


def remove_cookie(storage_state_path: str, name: str) -> str:
    """Remove a cookie and return path to a temp file with modified state."""
    import tempfile

    with open(storage_state_path) as f:
        data = json.load(f)
    data["cookies"] = [c for c in data["cookies"] if c["name"] != name]
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    json.dump(data, tmp)
    tmp.close()
    return tmp.name
