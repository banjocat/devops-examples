# wrk
https://github.com/wg/wrk

## Environmental variables
| Variable | Default |What it does|
|----------|--------|------|
|WRK_METHOD | GET | Method to use |
|WRK_BODY | "" | Body to send|
|WRK_CONTENT_TYPE | /txt/plain | Content type..|
|WRK_CONNECTIONS | 300 | Number of connections to keep open|
|WRK_THREADS | 3 | Number of threads to use|
|WRK_URL  | localhost | URL to send request|
|WRK_DURATION | 10 | Duration to run test|


## Example

      docker run -e URL=www.google.com banjocat/wrk
