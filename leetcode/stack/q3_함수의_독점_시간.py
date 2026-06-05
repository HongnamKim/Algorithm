def exclusiveTime(n, logs):
    call_stack = []
    exec_times = [0] * n
    time = 0

    for log in logs:
        status = log.split(":")[1]
        if status == "start":
            func_id, func_status, func_time = log.split(":")

            if call_stack:
                last_id, last_status, last_time = call_stack[-1].split(":")
                exec_times[int(last_id)] += (int(func_time) - time)

            call_stack.append(log)
            time = int(func_time)
        else:
            start_id, start_status, start_time = call_stack.pop().split(":")
            end_id, end_status, end_time = log.split(":")

            exec_times[int(start_id)] += (int(end_time) - time + 1)

            time = int(end_time) + 1

    return exec_times

n = 3
l = ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]

print(exclusiveTime(n, l))