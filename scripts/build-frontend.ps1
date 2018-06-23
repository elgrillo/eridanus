$SCRIPTS_HOME = Get-Location
$PROJECT_HOME = (Get-Item $SCRIPTS_HOME).Parent.FullName
$FRONTEND_HOME = "$PROJECT_HOME/frontend"
$BACKEND_STATIC_HOME = "$PROJECT_HOME/backend/static/app"

Write-Output "Project root dir: $PROJECT_HOME"
Write-Output "Build frontend angular app located at: $FRONTEND_HOME"
Write-Output "Front-end app will be deployed at: $BACKEND_STATIC_HOME"

Set-Location $FRONTEND_HOME
ng build -prod --base-href /app/ --deploy-url $BACKEND_STATIC_HOME
Set-Location $SCRIPTS_HOME

Write-Output "DONE"