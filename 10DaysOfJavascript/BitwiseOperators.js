'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getMaxLessThanK(n, k)
{
    var MaxVal = 0;
    var i, j;
    for (i = 1; i <= n-1; i++)
    {
        for (j = i+1; j <= n; j++)
        {
            var val = i & j;
            if (val < k && val > MaxVal)
                MaxVal = val;
        }
    }
    return MaxVal;
}


function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}



