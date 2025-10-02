const fs = require("fs");

const input = fs.readFileSync(0).toString().trim().split("\n");

const testCase = +input[0];

for (let i = 1; i <= testCase; i++) {
  const [card, changeCount] = input[i].split(" ");

  let maxVal = 0;
  const visited = new Set();

  function dfs(arr, k) {
    const key = arr.join("") + "-" + k;

    if (visited.has(key)) return;
    visited.add(key);

    if (k === 0) {
      const num = parseInt(arr.join(""), 10);
      if (num > maxVal) maxVal = num;
      return;
    }

    const n = arr.length;
    for (let j = 0; j < n - 1; j++) {
      for (let k = j + 1; k < n; k++) {
        [arr[j], arr[k]] = [arr[k], arr[j]];
        dfs(arr, k - 1);
        [arr[j], arr[k]] = [arr[k], arr[j]];
      }
    }
  }

  dfs(card.split(""), changeCount);

  console.log(`#${i} ${maxVal}`);
}
