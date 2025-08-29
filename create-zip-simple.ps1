Write-Host "Creando archivo ZIP para EasyPanel..." -ForegroundColor Green

$zipName = "python-flask-app-easypanel.zip"

if (Test-Path $zipName) {
    Remove-Item $zipName -Force
    Write-Host "Archivo ZIP anterior eliminado." -ForegroundColor Yellow
}

$filesToInclude = @("app.py", "requirements.txt", "Dockerfile", "docker-compose.yml", ".dockerignore", "README.md", "templates")

Compress-Archive -Path $filesToInclude -DestinationPath $zipName -Force

Write-Host "Archivo ZIP creado: $zipName" -ForegroundColor Green
Write-Host "Listo para subir a EasyPanel!" -ForegroundColor Green 