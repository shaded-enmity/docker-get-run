# docker-get-run
Get back `docker run` command from a running container

## Rationale

If you work with Docker containers on a daily basis the following output of `docker ps` is probably not going to surprise you:` 
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS   NAMES
1cd567fa7d12        fedora:25           "bash"              About an hour ago   Up About an hour            reverent_newton
```
The surprising thing is that if you want to try to run the same container on your machine, or simply run a similar instance of that container, the only thing you can do is run `docker inspect <container>` and assemble all the bits and pieces on your own. And this is the point where `docker-get-run` steps in by providing this exact functionality, but example is worth thousand words.

## Examples

Piggybacking on the `docker ps` output above:
```
$ docker-get-run 1cd567
docker run -t -d --link 6b49 -m 512M fedora:25 bash
```

Another example:
```
$ docker-get-run 6b498                                                                                                     
docker run -v /opt/testmount:/testmount:Z --cap-add sys_admin -p 25:10000 -t -i fedora:25 bash
```

## Supported flags

| Flag | Support |
|------|---------|
| -m / --memory | Full |
| -v / --volume | Partial |
| --link | Partial |
| -e | Full |
| -i | Full |
| -t | Full |
| -d | Full |
| --privileged | Full |
| -p | Full |
| --cap-add | Full |
| --name | Full |
| --hostname | Full |

## License

MIT
