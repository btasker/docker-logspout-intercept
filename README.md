Tailspout Syslog Capture
==========================

[Tailspout](https://github.com/gliderlabs/logspout) reconfigures docker containers to write logs elsewhere - whether that's Cloudwatch, papertrail or somewhere else.

This also prevents local tailing of the logs though.

This image allows you to watch logs for any services that Logspout has configured to send using the `syslog` protocol.

    docker run --rm --net=host [-v /var/run/docker.sock:/var/run/docker.sock] ghcr.io/btasker/logspout-syslog-watch:0.1 [container name or dest port]

Example:

    docker run --rm --net=host -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/btasker/logspout-syslog-watch:0.1 hello-world
    docker run --rm --net=host ghcr.io/btasker/logspout-syslog-watch:0.1 12345

If a port is specified, it should be the destination syslog port. Ordinarily, it's better to provide the container name (or id) of the container you want to tail logs for.


### Notes

- Where multiple containers are writing to the same syslog destination, the log output you receive will be mixed.
- This image makes no changes to running containers, it simply inspects them to get the log destination, and then uses [`scapy`](https://scapy.net/) to snoop packets



## TODO

- Switch to an alpine base image
