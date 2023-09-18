from collections import defaultdict
from datetime import datetime as dt

EXAMPLE = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""


def parse_input(aoc_input: str):
    lines = aoc_input.strip().split("\n")
    parts = [
        (dt.strptime(p.split("] ")[0], r"[%Y-%m-%d %H:%M"), p.split("] ")[1])
        for p in lines
    ]
    return parts


def guard_sleep_hours(logs: [(dt, str)]):
    current_guard = None

    guard_sleep_hours = defaultdict(lambda: [0 for _ in range(60)])
    sleep = None

    for (timestamp, log) in logs:
        if "Guard" in log:
            if sleep:
                guard_sleep_hours[current_guard] = [
                    n + 1 if sleep <= i <= 59 else n
                    for i, n in enumerate(guard_sleep_hours[current_guard])
                ]

            current_guard = log.split(" ")[1][1:]
            sleep = None

        elif "falls" in log:
            sleep = timestamp.minute

        elif "wakes" in log:
            guard_sleep_hours[current_guard] = [
                n + 1 if sleep <= i < timestamp.minute else n
                for i, n in enumerate(guard_sleep_hours[current_guard])
            ]
            sleep = None

    return guard_sleep_hours


def get_most_asleep(sleep_schedule: dict[str, [int]]):
    sleepy_guard = None
    max_sleep = 0

    for guard, sleep in sleep_schedule.items():
        if sum(sleep) > max_sleep:
            sleepy_guard = guard
            max_sleep = sum(sleep)

    return int(sleepy_guard), sleep_schedule[sleepy_guard].index(
        max(sleep_schedule[sleepy_guard])
    )


def get_most_minute_asleep(sleep_schedule: dict[str, [int]]):
    most = (0, 0, "")

    for guard, schedule in sleep_schedule.items():
        for minute, total in enumerate(schedule):
            if total > most[0]:
                most = (total, minute, guard)

    return most


def solution_1(aoc_input: str):
    logs = parse_input(aoc_input)
    logs.sort(key=lambda l: l[0])
    guard_sleeps = guard_sleep_hours(logs)
    guard, minute = get_most_asleep(guard_sleeps)
    return int(guard) * minute


def solution_2(aoc_input):
    logs = parse_input(aoc_input)
    logs.sort(key=lambda l: l[0])
    guard_sleeps = guard_sleep_hours(logs)

    total, minute, guard = get_most_minute_asleep(guard_sleeps)
    return minute * int(guard)
