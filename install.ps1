param([Parameter(ValueFromRemainingArguments=$true)][string[]]$KitArgs)
$ErrorActionPreference = 'Stop'
& python (Join-Path $PSScriptRoot 'scripts/kit.py') @KitArgs
exit $LASTEXITCODE
