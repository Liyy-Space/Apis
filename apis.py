import requests
response = requests.get("https://api.github.com")
response.content
#b'{"current_user_url":"https://api.github.com/user", ...}'

type(response.content)
