$commands = @("init", "fmt", "plan", "apply")
foreach ($command in $commands) {
    Write-Host "executing: $command"
    terraform $command
}
