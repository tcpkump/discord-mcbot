# discord-mcbot

Discord Bot for managing docker Minecraft servers. This is pretty tailored to my personal setup/deployment method, so code changes are very likely needed if others would like to use it.

## Overview

This is a very simple bot which only has a few commands:

- /minecraft list
- /minecraft start
- /minecraft stop
- /minecraft extendtime

For a description of each command, see [Commands](#Commands).

The bot interacts with a separate API service [mc-manager-api](https://github.com/garrettleber/mc-manager-api) that provides the exact same commands. For more info on the API, view that project's README. 
Requests to the API are then executed on the actual instance that is hosting the Minecraft servers.

I run it in a docker container, built from the supplied `Dockerfile`.

## Commands

```
/minecraft list
```

Lists the minecraft servers that are available to interact with.

```
/minecraft start [server]
```

Starts the specified server. If no server is passed, it will start the default server.

```
/minecraft stop [server]
```

Stops the specified server. If no server is passed, it will stop the default server.

```
/minecraft extendtime [server] [days]
```

This extends the [auto-stop](https://docker-minecraft-server.readthedocs.io/en/latest/misc/autopause-autostop/autostop/) feature in itzg/docker-minecraft-server containers. When using this feature, servers will automatically turn off after a configured period of time when no players are online.

This command will keep the server running for the given number of days. It accepts a value between 1 and 30. This is useful for projects that you would like to keep running even when players are offline.

The `server` argument is optional, if not provided, it will use the default server.

The `days` argument is optional, if not provided, it will extend by 1 day.

## TODO

### CI/CD

I am currently building my docker images manually using the following commands:

```bash
docker build -t git.imkumpy.in/kumpy/discord-mcbot:latest .
docker push git.imkumpy.in/kumpy/discord-mcbot:latest
```

I would like to setup a simple CI/CD pipeline for this.

### Improve docker image

This currently builds into a fairly large docker image, and I could probably benefit from picking a more lightweight base image.

