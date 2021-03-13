# Simple Docker HTTP server

[![GitHub CI](https://github.com/KSonny4/simple-docker-http-server/actions/workflows/ci.yaml)](https://github.com/KSonny4/simple-docker-http-server/actions/workflows/ci.yaml/badge.svg)

[![Docker Stars](https://img.shields.io/docker/stars/ksonny4/simple-docker-http-server.svg)](https://hub.docker.com/r/ksonny4/simple-docker-http-server)
[![Docker Pulls](https://img.shields.io/docker/pulls/ksonny4/simple-docker-http-server.svg)](https://hub.docker.com/r/ksonny4/simple-docker-http-server)
[![Docker Image Size](https://img.shields.io/docker/image-size/ksonny4/simple-docker-http-server.svg)](https://hub.docker.com/r/ksonny4/simple-docker-http-server)
[![Docker Image Version](https://img.shields.io/docker/v/ksonny4/simple-docker-http-server.svg)](https://hub.docker.com/r/ksonny4/simple-docker-http-server)

Yet another simple dockerized http web for testing purposes. I don't want to run someone else's
http server when I can quickly create my own and be sure what am I running. There are easier ways
to create HTTP server, but I am most familiar with `aiohttp`.

This is container uses `python`, `poetry`, `aiohttp` and `docker` to create web server listening GET and HEAD requests on port of your choice.

## examples

### Run docker container on local port 1234
 ```bash
 docker run -d -p 1234:8080 ksonny4/simple-docker-http-server
 curl 'http://127.0.0.1:1234/'
 curl 'http://localhost:1234/'
 ```

### Use port 8888 in container and local port 8080
```bash
 docker run -d -p 8080:8888 -e PORT=8888 ksonny4/simple-docker-http-server
 curl 'http://127.0.0.1:8080/'
 ```

### Change host in docker 
 ```bash
 docker run -d -p 8080:8888 -e HOST=0.0.0.0 -e PORT=8888 ksonny4/simple-docker-http-server
 curl 'http://127.0.0.1:8080/'
 ```