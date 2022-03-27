from collections import defaultdict

def GroupTotals(strArr):
  # use a dictionary to map letters with their counts
  counts_dict = defaultdict(int)
  for elem in strArr:
    letter, num = elem.split(':')[0], int(elem.split(':')[1])
    counts_dict[letter] += num

  ans = ''
  for key in sorted(counts_dict):
    if counts_dict[key] != 0:
      ans += key + ':' + str(counts_dict[key]) + ','

  # return final string without the final comma
  return ans[:-1]

print(GroupTotals([]))

def CountingMinutes(strParam):
  # parse am and pm and times info
  first_time, second_time = strParam.split('-')
  first_time_hours = int(first_time[:-2].split(':')[0])
  first_time_minutes = + int(first_time[:-2].split(':')[1])
  second_time_hours = int(second_time[:-2].split(':')[0])
  second_time_minutes = int(second_time[:-2].split(':')[1])
  first_time_am_pm = first_time[-2:]
  second_time_am_pm = second_time[-2:]

  # convert to 24-hour clock
  if first_time_am_pm == 'am':
    if first_time_hours == 12:
      first_time_hours = 0
  elif first_time_am_pm == 'pm':
    if first_time_hours != 12:
      first_time_hours += 12 

  if second_time_am_pm == 'am':
    if second_time_hours == 12:
      second_time_hours = 0
  if second_time_am_pm == 'pm':
    if second_time_hours != 12:
      second_time_hours += 12

  # convert to minutes
  first_time_converted_minutes = first_time_hours * 60 + first_time_minutes
  second_time_converted_minutes = second_time_hours * 60 + second_time_minutes

  # three cases:
  # if equal - return 0,
  # if second time larger - simply return the difference,
  # if first time larger - take the number of minutes in a day, and subtract (first - second)
  if second_time_converted_minutes == first_time_converted_minutes:
    return 0
  elif second_time_converted_minutes > first_time_converted_minutes:
    return second_time_converted_minutes - first_time_converted_minutes
  else:
    return (24*60) - (first_time_converted_minutes - second_time_converted_minutes)

# keep this function call here 
print(CountingMinutes(input()))