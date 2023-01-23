#Things to Do
#3.1

#assign variables to their respective time units and solve
seconds = 60
minutes = 60
seconds_per_hour = seconds * minutes
print(seconds_per_hour)
#seconds per hour = 3,600


seconds_per_day = seconds_per_hour * 24
print(seconds_per_day)
#seconds per day = 86,400

seconds_per_day = 86400
float_point = seconds_per_day / seconds_per_hour
print(float_point)
#float point = 24.0

integer = seconds_per_day // seconds_per_hour
print(integer)
#integer = 24
#the number did infact, agree with the float point number asides from the final ".0"