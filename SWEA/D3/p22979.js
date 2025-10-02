const fs = require("fs");

const input = fs.readFileSync(0).toString().trim().split("\n");

const testCase = +input[0];

for (let t = 1; t <= testCase * 3; t += 3) {
  const str = input[t].split("");
  const K = +input[t + 1];
  const X = input[t + 2].split(" ").map(Number);

  const sum = X.reduce((prev, curr) => prev + curr, 0);

  const length = str.length;

  const operations = ((sum % length) + length) % length;

  const cut = str.splice(operations);

  const result = [...cut, ...str].join("");

  console.log(result);
}
