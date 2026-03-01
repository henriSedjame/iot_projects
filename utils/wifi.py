import network
import urequests

SSID = 'Freebox-C7BA14'
PASSWORD = '95f9xqzd4hqwt6d9qmddtz'

wlan = network.WLAN(network.STA_IF)

wlan.active(True)

wlan.connect(SSID, PASSWORD)

print("Successfully connected to WiFi\n\n")

print('**************************************\n')
print('Connection to Google...\n')
print('**************************************\n')
r = urequests.get('http://www.google.com')

print(r.content)

r.close()

print('**************************************\n')
print('Retrieving data from JSONPlaceholder...\n')
print('**************************************\n')

r = urequests.get('https://jsonplaceholder.typicode.com/todos/1')

print(r.json())

r.close()