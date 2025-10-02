const cap = 4;
const n = 5;
const deliveries = [1, 0, 3, 1, 2];
const pickups = [0, 3, 0, 4, 0];

// 멀리 있는 집부터 처리

function solution(cap, n, deliveries, pickups) {
  let answer = 0;
  let deliTotal = deliveries.reduce((acc, curr) => acc + curr, 0);
  let pickupsTotal = pickups.reduce((acc, curr) => acc + curr, 0);

  let deliTarget = [];
  let pickupsTarget = [];

  let currCap = 0;

  for (let i = n - 1; i > -1; i--) {
    if (currCap + deliveries[i] <= cap) {
      currCap += deliveries[i];
    }
  }
  console.log("del", currCap);
  return answer;
}

console.log(solution(cap, n, deliveries, pickups));
