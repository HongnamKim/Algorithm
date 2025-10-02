const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');

const testCase = +input[0];

for(let i = 1; i< testCase+1; i++){
    //console.log(input[i])
    const nums = input[i].split(' ').map(Number);


    let total = 0;

    for(let j = 0; j < nums.length; j++){
        if(nums[j] % 2 === 1) {
            total += nums[j];
        }
    }

    console.log(`#${i} ${total}`);
}