const fs = require("fs");

const input = fs.readFileSync(0).toString().trim().split("\n");

for (let i = 0; i < 20; i += 2) {
  const buildingCount = +input[i];
  //console.log(input[i + 1]);
  //console.log(typeof input[i + 1]);
  const heights = input[i + 1].split(" ").map(Number);

  let views = 0;

  for (let j = 2; j < buildingCount - 2; j++) {
    const maxHeight = Math.max(
      heights[j - 2],
      heights[j - 1],
      heights[j + 1],
      heights[j + 2]
    );

    if (maxHeight < heights[j]) {
      views = views + heights[j] - maxHeight;
    }
  }

  console.log(`#${i / 2 + 1} ${views}`);
}
