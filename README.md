# legislation

이 저장소에는 간단한 파이썬 스크립트들이 들어 있습니다.

## 사용법

`positive_hourly_messages.py` 스크립트는 오늘 퇴근 예정 시간을 입력하면 그때까지 매시간 긍정적인 메시지를 출력합니다.

```bash
python positive_hourly_messages.py
```

프로그램 실행 후 `HH:MM` 형식으로 퇴근 시각을 입력하면 현재 시각부터 입력한 시각까지 한 시간 간격으로 랜덤한 메시지가 터미널에 표시됩니다.

`time_until_off.py` 스크립트는 퇴근 예정 시간을 입력하면 남은 시간을 시각적으로 보여줍니다.

```bash
python time_until_off.py
```

`HH:MM` 형식의 시간을 입력하면 지금부터 그때까지 남은 시간이 `X시간 Y분` 형태로 출력됩니다.
