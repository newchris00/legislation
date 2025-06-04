import datetime as dt
import time
import random

MESSAGES = [
    "좋아요! 곧 끝나요",
    "수고했어요, 조금만 더!",
    "멋져요! 계속 힘내요",
    "조금만 더 버텨요!",
    "훌륭해요, 곧 마칠 거예요!"
]

def parse_end_time(input_str: str) -> dt.datetime:
    """Parse the input HH:MM time for today or tomorrow."""
    now = dt.datetime.now()
    try:
        end_parts = dt.datetime.strptime(input_str, "%H:%M")
    except ValueError:
        raise ValueError("잘못된 형식입니다. 예) 18:30")

    end_time = now.replace(hour=end_parts.hour, minute=end_parts.minute,
                           second=0, microsecond=0)
    if end_time <= now:
        # 입력한 시간이 이미 지났다면 다음 날로 간주
        end_time += dt.timedelta(days=1)
    return end_time

def main() -> None:
    end_input = input("오늘 퇴근할 시간(HH:MM)을 입력하세요: ").strip()
    try:
        end_time = parse_end_time(end_input)
    except ValueError as e:
        print(e)
        return

    while True:
        now = dt.datetime.now()
        if now >= end_time:
            print("퇴근 시간이에요! 수고하셨습니다!")
            break

        print(random.choice(MESSAGES))
        next_hour = now + dt.timedelta(hours=1)
        sleep_until = min(next_hour, end_time)
        time.sleep((sleep_until - now).total_seconds())

if __name__ == "__main__":
    main()
