$Body = @{ vpgName = $env:ZertoVPGName } | ConvertTo-Json

# Define parameters cleanly in a hash table
# This script need be uploaded to Zerto VPG from the ZVM GUI (target site)
$RestParams = @{
    Uri         = "http://192.168.222.135:8000/zerto"
    Method      = "Post"
    Body        = $Body
    ContentType = "application/json"
    TimeoutSec  = 10
}

try {
    # Use '@' instead of '$' to splat the parameters
    Invoke-RestMethod @RestParams
} 
catch {
    $LogDir = if ($env:ZertoOutputDir) { $env:ZertoOutputDir } else { "/tmp" }
    $OutputFile = Join-Path $LogDir "webhook_error.txt"
    "Webhook failed to send at $(Get-Date). Error: $_" | Out-File -FilePath $OutputFile -Force
}