# Manual ZIP reconstruction

**Release:** Archivo 21 Project Scaffold `0.1.0-alpha.1`  
**Expected filename:** `archivo21-project-scaffold-0.1.0-alpha.1.zip`  
**Expected SHA-256:** `f34eb9aae666bbd5f961c602f6e7c882a628931d9935dee9ba355c8002f60bc8`

The exact inspected ZIP is stored as eight Base64 text segments in `data/`.

## Linux/macOS

```sh
cat data/zip.part*.b64 | base64 --decode > archivo21-project-scaffold-0.1.0-alpha.1.zip
sha256sum archivo21-project-scaffold-0.1.0-alpha.1.zip
```

## Windows PowerShell

```powershell
$base64 = (Get-ChildItem data\zip.part*.b64 | Sort-Object Name | ForEach-Object { Get-Content $_ -Raw }) -join ''
[IO.File]::WriteAllBytes('archivo21-project-scaffold-0.1.0-alpha.1.zip', [Convert]::FromBase64String($base64))
(Get-FileHash 'archivo21-project-scaffold-0.1.0-alpha.1.zip' -Algorithm SHA256).Hash.ToLower()
```

Do not use the file unless the digest matches the expected SHA-256 above.
