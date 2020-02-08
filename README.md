# Tierras Virgenes

Custom UO server.

It use ServUO as server (GPL license) and provide crossUO as client () 

# Folders organization

* git: Repositories
* resources: Installed resources
* downloads: raw data downloaded

# Quick start

## Cloning

First step.

If you want to start RIGHT NOW, and you don't care about what version, try mine configuration and version using crossuo and ServUO as submodules:

```
git clone --recursive git@github.com:Tierras-virgenes/tv-server.git
```

Note: If you already clone it without recursive option, run the following lines:

```
git submodule init
git submodule update
```

## Resources

Second step

You will need UO resources. In example: UO2D.zip extracted from https://runuo.theabyss.eu/?files

* 2D: Put here Ultima onlines binaries. I use "Time of Legends" 2D from the link above.

## Compile server

1. Go to submodule/ServUO folder.
2. Execute `Compile.WIN - Release.bat`. If you are in GNU/Linux use `make`
3. Press any key 2 times, and then put your UO binary folder wehn 'Enter the Ultima Online directory' appear. In example: `../../resources/2D`
4. Create a GM account.
5. Allow firewall.
6. When a message like: `Listening: 127.0.0.1:2593`, the server is running in localhost and port 2593. It also have a public IP.

Note I: To compile in GNU/Linux you will need mono-complete v>=5.0
Note II: Server allow to use several commands. Try write `?` to learn more.

## Compile client

...
