# wrk
https://github.com/wg/wrk

## Environmental variables
| Variable | Default |What it does|
|----------|--------|------|
|CONNECTIONS | 300 | Number of connections to keep open|
|THREADS | 3 | Number of threads to use|
|URL  | localhost | URL to send request|
|DURATION | 10 | Default to piz

## Volumes
| Path | What it does |
| -----| ----- |
| /tmp/script.lua | Allows sending specific data in post |

## Example

      docker run -e URL=localhost:8080/postapi banjocat/wrk
