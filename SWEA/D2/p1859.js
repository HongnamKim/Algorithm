const fs = require("fs");

const input = fs.readFileSync(0).toString().trim().split("\n");

const testCase = +input[0];

for (let i = 1; i <= testCase; i++) {
  const days = +input[1];

  const prices = input[2].split(" ").map(Number);

  let revenue = 0;

  let max = prices[days - 1];

  for (let j = days - 1; j >= 0; j--) {
    if (prices[j] > max) {
      max = prices[j];
    } else {
      revenue = revenue + (max - prices[j]);
    }
  }

  console.log(`#${i} ${revenue}`);
}
