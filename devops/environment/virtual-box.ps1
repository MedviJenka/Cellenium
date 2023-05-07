mkdir "C:\vm-box"


function CreateVMFolders {

    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, ValueFromPipeline = $true, ValueFromPipelineByPropertyName = $true)]
        [ValidateNotNullOrEmpty()]
        [ValidateScript({
            if (-not (Test-Path $_ -PathType Container)) {
                throw "The path '$_' does not exist or is not a valid directory."
            }
            $true
        })]
        [string]$FolderPath
    )

    $ubuntuFolder = Join-Path -Path $FolderPath -ChildPath "ubuntu"
    $centosFolder = Join-Path -Path $FolderPath -ChildPath "centos"
    New-Item -ItemType Directory -Path $ubuntuFolder | Out-Null
    New-Item -ItemType Directory -Path $centosFolder | Out-Null
}


function CentosSetup {

    $boxName = "geerlingguy/centos7"
    Set-Location "C:\vm-box\centos"
    vagrant init $boxName
    vagrant up
    vagrant halt

}


function UbuntuSetup {

    $boxName = "ubuntu/bionic64"
    Set-Location "C:\vm-box\ubuntu"
    vagrant init $boxName
    vagrant up
    vagrant halt


}


function Login {

    vagrant ssh 

}



CreateVMFolders -FolderPath "C:\vm-box"
CentosSetup
UbuntuSetup
Start-Process VirtualBox.exe
Login