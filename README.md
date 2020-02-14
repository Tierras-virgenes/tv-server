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

### Client configuration

Here you are a sample configuration, with account name test, and password test.  

* CustomPath should work with default resource path in GNU/Linux.
* The file has to be in `crossuo` binary path with name: `crossuo.cfg`.
* Example content:

```
AcctID=test
AcctPassword=test
RememberAcctPW=no
AutoLogin=no
TheAbyss=no
Asmut=no
Crypt=no
CustomPath=../../../../UO/2D
LoginServer=127.0.0.1,2593
ClientVersion=7.0.45.0
```

* Note: You can generate a configuration file with xuolauncher.

### Fast way Windows

* Go to https://crossuo.com/#download and install it. In example: https://github.com/crossuo/crossuo/releases
* Generate a configuration file `crossuo.cfg` at crossuo.exe path:

### Developer way Windows

** TODO: Test this method

* Install CMake. In example `cmake-3.16.4-win64-x64.msi` from: https://cmake.org/download/
* Visual Studio 2019 Community edition. In example from: https://visualstudio.microsoft.com/es/downloads/
* Install Cygwin64. In example from: https://cygwin.com/install.html
    * Select mingw64-gcc, and apply changes.
    * Add to environment variables MinGW path: `C:\MinGW\bin`
* Go to `submodules\crossuo` path
* Execute cmake:

```
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j4
```

### Developer way GNU/Linux

* Install dependencies (OpenGL ... **TODO**)
* Compile crossuo
```
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j4
```
* Copy `tv-server/resources/crossuo/Config/` into build path and edit it. In example: 
```
cp tv-server/resources/crossuo/Config/crossuo.cfg submodules/crossuo/build/src
```
* Run `crossuo` binary.

Note: By default should work use: `CustomPath=../../../../resources/2D`

# Other servers

* [Tierras Baldias community on Facebook](https://www.facebook.com/TierrasBaldiasUO), still missing the old shard.
* [UO Demise](https://www.uogdemise.com/)

# References

* [UO Guide](http://www.uoguide.com/Main_Page)