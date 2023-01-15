class Time:

# constructor
  def __init__(self, seconds):
     self.seconds = seconds

# function to convert and return a string of minutes and seconds
  def convert_to_minutes(self):
     mins = self.seconds//60 # get the total minutes in the given seconds
     secs = self.seconds - (mins*60) # get the remaining seconds

# return the string of minutes:seconds
     return "%d:%d" %(mins,secs)

# function to convert and return string of hours, minutes, and seconds
  def convert_to_hours(self):
     secs = self.seconds
     hours = secs//3600 # get the total hours in the given seconds
     secs = secs - (hours*3600) # get the remaining seconds
     mins = secs//60 # get the total minutes in the remaining seconds
     secs = secs - (mins*60) # get the remaining seconds

# return the string of hours:minutes:seconds
     return "%d:%d:%d" %(hours,mins,secs)

# test the Time class
time = Time(230)
print(time.convert_to_minutes())
time = Time(4520)
print(time.convert_to_hours())
#call the main function
