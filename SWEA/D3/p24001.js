const fs = require("fs");

const input = fs.readFileSync(0).toString().trim().split("\n");

const testCases = +input[0];

let maxDistance;

const dfs = (directions, idx, pos) => {
  if (idx === directions.length) {
    maxDistance = Math.max(maxDistance, Math.abs(pos));
    return;
  }

  if (directions[idx] === "L") {
    dfs(directions, idx + 1, pos - 1);
  } else if (directions[idx] === "R") {
    dfs(directions, idx + 1, pos + 1);
  } else {
    dfs(directions, idx + 1, pos - 1);
    dfs(directions, idx + 1, pos + 1);
  }
};

for (let i = 1; i <= testCases; i++) {
  const directions = input[i].split("");

  maxDistance = 0;

  dfs(directions, 0, 0);

  console.log(maxDistance);
}
