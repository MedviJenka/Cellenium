try {
    $command = @("validate", "fmt", "plan")
    foreach($command in $commands) {
        Write-Host "running terraform command"
        terraform $command
    }
}
catch {
    # Exception handling code
    Write-Host "one of the commands above did not execute: $($_.Exception.Message)"
    # Additional error handling or logging
}
finally {
    # Optional finally block
    Write-Host "This code always executes, regardless of exceptions."
    $command = @("init", "apply")
    foreach($command in $commands) {
        Write-Host "running terraform command"
        terraform $command
    }
}
