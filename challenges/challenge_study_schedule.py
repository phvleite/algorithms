def study_schedule(permanence_period, target_time):
    try:
        students = 0
        for student in permanence_period:
            entry_time = student[0]
            departure_time = student[1]
            students = study_schedule_checked(
                entry_time, departure_time, target_time, students
            )
    except Exception:
        return None
    else:
        return students


def study_schedule_checked(entry_time, departure_time, target_time, students):
    if target_time == entry_time:
        students += 1
    if target_time > entry_time and target_time + 1 <= departure_time:
        students += 1
    if target_time == departure_time and target_time != entry_time:
        students += 1

    return students


if __name__ == "__main__":
    target_time = [1, 2, 3, 4, 5]
    for time in target_time:
        result = study_schedule(
            [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], time
        )
        print(f"target_time {time}: {result}")

    # time = 1
    # result = study_schedule(
    #     [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], time
    # )
    # print(f"target_time {time}: {result}")
