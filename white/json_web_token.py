import base64
header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9'
print(base64.b64decode(header))
payload = 'eyJsb2dpbiI6InF3ZSIsImlhdCI6IjE1ODQzNTcyNzEifQ=='
print(base64.b64decode(payload))
s = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9.eyJsb2dpbiI6InF3ZSIsImlhdCI6IjE1ODQzNTUyOTEifQ==.ZjFhY2UzYTlmNmQ0NzI1NWYzODQ5N2M1Y2NlMzNjZDEzZWFkMzI1ZDhkOTljZDUxZjA2YTJjMjc2OWQyMjI4ZA'
print(s.split("."))
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9.eyJsb2dpbiI6InF3ZSIsImlhdCI6IjE1ODQzNTUyOTEifQ==.
