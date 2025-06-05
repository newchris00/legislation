import datetime as dt


def parse_end_time(input_str: str, now: dt.datetime | None = None) -> dt.datetime:
    """Parse the input HH:MM time for today or tomorrow."""
    if now is None:
        now = dt.datetime.now()
    try:
        end_parts = dt.datetime.strptime(input_str, "%H:%M")
    except ValueError as exc:
        raise ValueError("잘못된 형식입니다. 예) 18:30") from exc

    end_time = now.replace(hour=end_parts.hour, minute=end_parts.minute,
                           second=0, microsecond=0)
    if end_time <= now:
        end_time += dt.timedelta(days=1)
    return end_time


def time_until(end_input: str, now: dt.datetime | None = None) -> dt.timedelta:
    """Return time remaining until the given end time string."""
    end_time = parse_end_time(end_input, now)
    if now is None:
        now = dt.datetime.now()
    return end_time - now


def main() -> None:
    end_input = input("퇴근 예정 시간(HH:MM)을 입력하세요: ").strip()
    try:
        delta = time_until(end_input)
    except ValueError as e:
        print(e)
        return

    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes = remainder // 60
    print(f"퇴근까지 {hours}시간 {minutes}분 남았습니다.")


if __name__ == "__main__":
    main()
