"""Sube imágenes a la carpeta del proyecto en Google Drive.

Uso:
    python tools/drive_sync.py <subcarpeta/ruta> archivo1.png [archivo2.png ...]

La ruta se crea dentro de la carpeta raíz del proyecto (DRIVE_ROOT). Si ya
existe un archivo con el mismo nombre en esa subcarpeta, se reemplaza su
contenido. Necesita GOOGLE_DRIVE_TOKEN_JSON en el entorno.
"""

import json
import mimetypes
import os
import pathlib
import sys
import urllib.parse
import urllib.request
import uuid

DRIVE_ROOT = os.environ.get("ULTIMO_VAGON_DRIVE_ROOT", "15r7vIdVliV0BZuFz8Lm13amwKVpM8z3s")
API = "https://www.googleapis.com/drive/v3/files"
UPLOAD = "https://www.googleapis.com/upload/drive/v3/files"


def token():
    t = json.loads(os.environ["GOOGLE_DRIVE_TOKEN_JSON"])
    data = urllib.parse.urlencode({
        "client_id": t["client_id"], "client_secret": t["client_secret"],
        "refresh_token": t["refresh_token"], "grant_type": "refresh_token",
    }).encode()
    return json.load(urllib.request.urlopen(t["token_uri"], data))["access_token"]


def call(tok, url, method="GET", body=None, headers=None):
    req = urllib.request.Request(url, data=body, method=method,
                                 headers={"Authorization": f"Bearer {tok}", **(headers or {})})
    return json.load(urllib.request.urlopen(req))


def find(tok, name, parent, folder=False):
    q = f"name = '{name}' and '{parent}' in parents and trashed = false"
    if folder:
        q += " and mimeType = 'application/vnd.google-apps.folder'"
    r = call(tok, f"{API}?" + urllib.parse.urlencode({"q": q, "fields": "files(id)"}))
    return r["files"][0]["id"] if r["files"] else None


def ensure_path(tok, path):
    parent = DRIVE_ROOT
    for part in [p for p in path.split("/") if p]:
        fid = find(tok, part, parent, folder=True)
        if not fid:
            meta = json.dumps({"name": part, "mimeType": "application/vnd.google-apps.folder",
                               "parents": [parent]}).encode()
            fid = call(tok, API, "POST", meta, {"Content-Type": "application/json"})["id"]
        parent = fid
    return parent


def upload(tok, folder, path):
    path = pathlib.Path(path)
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    existing = find(tok, path.name, folder)
    boundary = uuid.uuid4().hex
    meta = {"name": path.name} if existing else {"name": path.name, "parents": [folder]}
    body = (f"--{boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n"
            f"{json.dumps(meta)}\r\n--{boundary}\r\nContent-Type: {mime}\r\n\r\n").encode()
    body += path.read_bytes() + f"\r\n--{boundary}--".encode()
    url = f"{UPLOAD}/{existing}?uploadType=multipart" if existing else f"{UPLOAD}?uploadType=multipart"
    r = call(tok, url + "&fields=id,webViewLink", "PATCH" if existing else "POST", body,
             {"Content-Type": f"multipart/related; boundary={boundary}"})
    return r["webViewLink"]


def main():
    sub, files = sys.argv[1], sys.argv[2:]
    tok = token()
    folder = ensure_path(tok, sub)
    print("carpeta", f"https://drive.google.com/drive/folders/{folder}")
    for f in files:
        print(pathlib.Path(f).name, upload(tok, folder, f))


if __name__ == "__main__":
    main()
