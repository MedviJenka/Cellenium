set-location -path "C:\Users\evgenyp\Cellenium\devops\ubuntu\"

# aws configure

$commands = @('fmt', 'validate', 'plan', 'init', 'apply')
foreach($command in $commands) {
    write-host "executing terraform $command"
    terraform $command
}
