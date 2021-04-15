# mombot-api

## Instructions

Copy `.env.example` to a new file `.env` and fill with appropriate Discord values.

Pull the image:

```
docker pull ryilliams/mombot-api
```

Or if you'd rather build it yourself:

```
docker build -t mombot-api .
```

Run the container:

```bash
docker run -d -p 80:80 --env-file ./.env mombot-api
```

Send a request:
```bash
curl http://localhost/weather/30/sunny
```

Endpoint format: `http://localhost/weather/:temperature/:condition`

`temperature` must be an int, conditions include: sunny, snowy, windy, and rainy.