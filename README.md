# mombot-api

## Instructions

Copy `.env.example` to a new file `.env` and fill with appropriate Discord values.

Build the image:

```
docker build -t mombot-api .
```

Run the container:

```bash
docker run -d -p 80:80 --env-file ./.env mombot-api
```