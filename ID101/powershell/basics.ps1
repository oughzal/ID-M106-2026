$n = Read-Host "Enter a number"
foreach($i in 1..$n){
    if($i %2 -eq 0){
        Write-Host "$i"
    }
}

if( $n -eq 1 -or $n -eq 2){
    Write-Host "The number is prime"
}
else{
    $i = 2 
    while($n % $i -ne 0){
        $i++
    }
    if($i -eq $n){
        Write-Host "The number is prime"
    }
    else{
        Write-Host "The number is not prime"
    }
}