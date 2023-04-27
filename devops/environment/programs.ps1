$packages = 'virtualbox', 'vagrant', 'awscli', 'sublimetext3.app'


if (Test-Path -Path "$env:ProgramData\Chocolatey") {
    foreach ($packageName in $packages) {
        choco install $packageName -y
    }
}

else {
  # InstallChoco
    Set-ExecutionPolicy Bypass -Scope Process -Force;
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
    Invoke-Expression((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

  # DoYourPackageInstallStuff
    foreach ($packageName in $packages) {
        choco install $packageName -y
    }
}
