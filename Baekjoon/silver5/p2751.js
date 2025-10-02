const fs = require("fs");

const input = fs.readFileSync(0).toString().trim().split("\n");

const nums = input.splice(1).map(Number);

const sorted = nums.sort((a, b) => a - b);

for (const num of sorted) {
  console.log(num);
}
