import heapq
import math

from collections import defaultdict


class Record:
    def __init__(self, in_time):
        self.in_time = in_time
        self.out_time = None

    def __str__(self):
        return "IN: " + str(self.in_time) + "\nOUT: " + str(self.out_time)

    def set_out_time(self, out_time):
        self.out_time = out_time

    def get_parking_time(self):
        out_time = self.out_time
        in_time = self.in_time

        out_hour, out_minute = map(int, out_time.split(":"))
        in_hour, in_minute = map(int, in_time.split(":"))

        if out_minute < in_minute:
            out_hour -= 1
            out_minute += 60

        hour = out_hour - in_hour
        minute = out_minute - in_minute

        return hour * 60 + minute


def solution(fees, records):
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    parsed_records = defaultdict(None)

    total_times = defaultdict(int)

    for record in records:
        time, number, action = record.split()
        if action == "IN":
            parsed_records[number] = Record(time)
        else:
            parsed_record: Record = parsed_records[number]
            parsed_record.set_out_time(time)
            parking_time = parsed_record.get_parking_time()
            total_times[number] += parking_time

    # 출차 안한 차량 종료 시간 설정
    for number, record in parsed_records.items():
        if not record.out_time:
            record.set_out_time("23:59")
            parking_time = record.get_parking_time()
            total_times[number] += parking_time

    parking_fees = []

    for number, parking_time in total_times.items():
        fee = (
            (
                default_fee
                + math.ceil((parking_time - default_time) / unit_time) * unit_fee
            )
            if parking_time > default_time
            else default_fee
        )
        heapq.heappush(parking_fees, (number, fee))

    answer = []
    while parking_fees:
        answer.append(heapq.heappop(parking_fees)[1])

    return answer


# 기본시간(분) / 기본 요금(원) / 단위 시간(분) / 단위 요금(원)
a = [180, 5000, 10, 600]
b = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

aa = solution(a, b)
print()
print(aa)
