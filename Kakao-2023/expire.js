const today = "2022.05.19";
const terms = ["A 6", "B 12", "C 3"];
const privacies = [
  "2021.05.02 A",
  "2021.07.01 B",
  "2022.02.19 C",
  "2022.02.20 C",
];

function solution(today, terms, privacies) {
  const [tYear, tMonth, tDate] = today.split(".");
  const todayDate = new Date(
    Number(tYear),
    Number(tMonth) - 1,
    Number(tDate) + 1
  );

  let answer = [];
  const dataNum = privacies.length;

  for (let i = 0; i < dataNum; i++) {
    const [fullDate, term] = privacies[i].split(" ");
    let addMonth = findTerms(terms, term);

    const expireDate = calcDate(fullDate, addMonth);
    if (expireDate <= todayDate) {
      answer.push(i + 1);
    }
  }

  return answer;
}

function findTerms(terms, term) {
  let addMonth = 0;

  for (let i = 0; i < terms.length; i++) {
    let [name, month] = terms[i].split(" ");
    if (name === term) {
      addMonth = Number(month);
    }
  }

  return addMonth;
}

function calcDate(fullDate, addMonth) {
  let [year, month, date] = fullDate.split(".");
  year = Number(year);
  month = Number(month) - 1;
  date = Number(date) + 1;
  month += addMonth;
  if (month > 12) {
    year++;
    month -= 12;
  }

  const result = new Date(year, month, date);
  console.log(result);
  return result;
}

console.log(solution(today, terms, privacies));
