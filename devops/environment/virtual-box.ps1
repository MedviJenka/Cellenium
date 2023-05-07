mkdir "C:\vm-box"


function Create-VMFolders {

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

    # Create the "ubuntu" and "centos" subfolders

    $ubuntuFolder = Join-Path -Path $FolderPath -ChildPath "ubuntu"
    $centosFolder = Join-Path -Path $FolderPath -ChildPath "centos"
    New-Item -ItemType Directory -Path $ubuntuFolder | Out-Null
    New-Item -ItemType Directory -Path $centosFolder | Out-Null
}


function Centos-Setup {

    $boxName = "geerlingguy/centos7"
    cd "C:\vm-box\centos"
    vagrant init $boxName
    vagrant up
    vagrant halt

}


function Ubuntu-Setup {

    $boxName = "ubuntu/bionic64"
    cd "C:\vm-box\ubuntu"
    vagrant init $boxName
    vagrant up
    vagrant halt


}


function Login {

    vagrant ssh 

}



Create-VMFolders -FolderPath "C:\vm-box"
Centos-Setup
Ubuntu-Setup
start VirtualBox.exe
Login