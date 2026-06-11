

$services = get-service
$services | where {$_.status -eq "Running"} | sort DisplayName  | format-list

get-process | format-list
