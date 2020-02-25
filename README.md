# Tierras Virgenes

Custom UO server.

It use ServUO as server (GPL license) and provide crossUO as client (GPL) 

# Folders organization

* bin: You can use this folder to store your binaries related to UO. *Empty at clone*.
* downloads: You can use this folder to store your binaries related to UO. *Empty at clone*.
* resources: Installed resources
    * 2D: Default path for resources. *Empty at clone*.
    * crossuo/Config: Example UO client configuration.
    * tv: All Tierras Virgenes customization files.
* submodules: Repositories as dependencies:
    * crossuo: Compatible UO client version. Use relative resources path by default. More info [HERE](**TODO**)
    * ServUO: Compatible UO server. Use relative resources path by default. Use `helper.py` to manage changes with repository. More info [HERE](**TODO**)
    * wiki: TV-server wiki as submodule to ease integration and versioning.
* backup: Use `helper.py` to generate standalone backup copies of your server. *Empty at clone*. More info [HERE](**TODO**)

# Quick start

## 1º Cloning

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

## 2º Resources

The second step is to look for a correct version of the resources. You will need UO resources to run a server and a client. 

* resources/2D folder: Put here Ultima onlines binaries. I use "Time of Legends" 2D from the link above.
* In example, you can use: UO2D.zip extracted from https://runuo.theabyss.eu/?files
* You can use `python helper.py --check` from `servuo-utils` to check if all expected resources are ok and located in default path.

## 3º Set up server & client

Check how to start in the Wiki:

* [How](https://github.com/Tierras-virgenes/tv-server/wiki/server) to set up a server
* [How](https://github.com/Tierras-virgenes/tv-server/wiki/client) to set up a client

# Versions

| ServUO | Client classic | Client enhaced |
|:------|:-------|:--------|
| 56.1 | 7.0.76.46 | 67.0.59.0 |

* Note: cross uo current version is: 7.0.45.0 **TODO** check this.

# Other servers

* [Tierras Baldias community on Facebook](https://www.facebook.com/TierrasBaldiasUO), still missing the old shard.
* [UO Demise](https://www.uogdemise.com/)

# References

* [UO Guide](http://www.uoguide.com/Main_Page)