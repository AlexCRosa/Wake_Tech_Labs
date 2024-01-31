#
# Alex Cesar Rosa
# 1/17/2024
# Air Quality Classifier
#

# Get the AQI.
aqi = int(input('Enter the Air Quality Index (AQI): '))

# Determine the classification of the AQI
# and display the result.
if aqi <= 50:
    print('Good')
elif aqi > 50 and aqi <= 100:
    print('Moderate')
elif aqi > 100 and aqi <= 150:
    print('Unhealthy for Sensitive Groups')
elif aqi > 150 and aqi <= 200:
    print('Unhealthy')
elif aqi > 200 and aqi <= 300:
    print('Very Unhealthy')
else:
    print('Hazardous')