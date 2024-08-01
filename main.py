def checkifgap(year):
  if year%4 == 0:
    return True
  else:
    return False

def generate_cal(year):
  days = 31
  flag = False
  months = [['jan'], ['feb'], ['mar'], ['apr'], ['may'], ['jun'], ['jul'], ['aug'], ['sep'], ['oct'], ['nov'], ['dec']]
  month = 0
  for y in range(len(months)):
    if months[month][0] == "feb" and checkifgap(year) == True:
      days = 29
      flag = False
    elif months[month][0] == "feb":
      days = 28
      flag = True
    elif months[month][0] == "mar" or months[month][0] == "jul" or months[month][0] == "jul" or months[month][0] == "aug":
      if months[month][0] == "aug":
        days = 31
      else:
        days = 31
      flag = False
    for x in range(1, days+1):
      months[month].append(x)
    month += 1
    if flag == True:
      days = days + 1
      flag = False
    else:
      days = days - 1
      flag = True
  return months

def findmonth(cal, month):
  for x in range(len(cal)):
    if cal[x][0] == month:
      return x
  return 0
  print("That month doesn't exist.")

def select_month(year, month, day):
  cal = generate_cal(year)
  month = findmonth(cal, month)
  if day >= 32:
    return "There are too many days for that to be a day in a month."
  elif day <= 0:
    return "There are too little days for that to be a day in a month."

  month = cal[month]
  
  if len(month) - 1 < day:
    return "There are too many days."

  return month
