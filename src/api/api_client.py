import httpx


class ApiClient:
    def __init__(self, base_url: str, api_token: str):
        self._client = httpx.Client(base_url=base_url, timeout=30)
        self._jwt = self._login(api_token)

    def _login(self, api_token: str) -> str:
        response = self._client.post("/api/login", json={"api_token": api_token})
        response.raise_for_status()
        return response.json()["jwt"]

    def get(self, path: str, **kwargs) -> httpx.Response:
        return self._client.get(path, headers=self._auth_headers, **kwargs)

    def post(self, path: str, **kwargs) -> httpx.Response:
        return self._client.post(path, headers=self._auth_headers, **kwargs)

    def put(self, path: str, **kwargs) -> httpx.Response:
        return self._client.put(path, headers=self._auth_headers, **kwargs)

    def delete(self, path: str, **kwargs) -> httpx.Response:
        return self._client.delete(path, headers=self._auth_headers, **kwargs)

    @property
    def _auth_headers(self) -> dict:
        return {"Authorization": f"Bearer {self._jwt}"}

    def close(self):
        self._client.close()
