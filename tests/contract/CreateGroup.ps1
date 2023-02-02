﻿Install-Module -Name AzureAD -Scope CurrentUser
Connect-AzureAD
Install-Module ActiveDirectory
Get-Module ActiveDirectory


$groupName1 = "@STNGGroup1"
$groupName2 = "@STNGGroup2"

#create group
$groupOneId = (New-AzureADGroup -Description "automated test group1" -DisplayName $groupName1 -MailEnabled $false -SecurityEnabled $true -MailNickName "group-1").ObjectId 
$groupTwoId = (New-AzureADGroup -Description "automated test group2" -DisplayName $groupName2 -MailEnabled $false -SecurityEnabled $true -MailNickName "group-2").ObjectId
