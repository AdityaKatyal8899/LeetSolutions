def countfreedays(meetings, days):
  busy_days = set()

  for start, end in meetings:
    for day in range(start, end+1):
      busy_days.add(day)

  free_days = days - len(busy_days)