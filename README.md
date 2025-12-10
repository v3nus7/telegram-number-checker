
![Logo](https://irbots.com/wp-content/uploads/2024/07/irbot-logo-e1752507899813.webp)


# Telegram Number Checker(Analyze)

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

IRbots provides a Telegram number status-checking service that lets you verify your target numbers on Telegram and determine whether they are banned, fresh, or already have an active session.

This is a clean and minimal Python wrapper for the **irbots.com Telegram number status API**, supporting both **synchronous** and **asynchronous** usage.  
[Click here to get your API key](https://irbots.com/TG-Number-Analyzer/)

## Usage/Examples


```bash
  pip install Tgchecker --upgrade
```

## Sync Example

```python
from Tgchecker import TgChecker

client = TgChecker(api_key="YOUR_API_KEY")
result = client.check_sync(["+12345678901", "+989121234567"])
print(result.data)
```
## Async Example
```python
import asyncio
from Tgchecker import TgChecker

async def main():
    client = TgChecker(api_key="YOUR_API_KEY")
    result = await client.check_async(["+12345678901"])
    print(result.data)

asyncio.run(main())
```

## output/Examples

```json
  {"+12345678901": "session", "+989121234567": "ban"}
```

## API Reference

#### check numbers
```http
  GET http://api.irbots.com/?key={your_api_key}&target=checker&numbers=1,2,3,4
```


#### Reponse

| json | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Time taken` | `string` | Time the API took to return response |
| `data` | `string` | Numbers and their statuses |
| `errors` | `string` | The numbers that check was not successful |
| `status` | `string` | Status of the request |


#### Example

```json
  {
  "Time taken": 0.23,
  "data": {
    "+14343540268": "ban",
    "+989175834924": "session"
  },
  "errors": 0,
  "status": "ok"
}

```
## Authors

- [@javadnr](https://github.com/javadnr)
- [@v3nus7](https://github.com/v3nus7)
## License

[MIT](https://choosealicense.com/licenses/mit/)
