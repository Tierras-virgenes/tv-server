# Configuring the server

ServUO have a folder to set up all configurations for the server. Go to ServUO/Config, and change whatever you need.

* Note: Fast notation is `${FILENAME}.cfg:${VARIABLE}=${CONTENT}`

# Basic configuration

If you want to start right now, this could be a basic configuration, edit these parameters:

* Server.cfg:Name=Tierras Virgenes
* DataPath.cfg:CustomPath=C:\Users\test\uo\resources\2D
* Expansion.cfg:CurrentExpansion=TOL
* VetRewards.cfg:Enabled=False

# Full configuration

This folder contain:

* Accounts.cfg: Configure parameters referred to creation/deletion accounts and IP restrictions.
* AutoRestart.cfg: Configure scheduler to autorestart server.
* AutoSave.cfg: Configure time between server saves and warnings.
* Champions.cfg: Champion spawns are set groups of creatures, spawning in selected locations and normally around an altar. Configure spawn time and rewards.
* ChampionSpawns.xml: Configure spawn parameters. Related with Champions.cfg
* Chat.cfg: Configure parameters referred to allow chat global or not.
* CityLoyalty.cfg: Enable/Disable the loyalty system.
* CityTrading.cfg: Configure the city trading reward and timing.
* Client.cfg: Configure clients allowed and kick time.
* DailyRares.cfg: Configure parameter referred to Daily rare spawn.
* DataPath.cfg: Configure default UO data path. 
* Email.cfg: Configure parameters referred to email server and authentication.
* Expansion.cfg: Configure what Ultima Online version use.
* Factions.cfg: Configure factions.
* General.cfg: Configure support email, metrics, and other stuff.
* Honesty.cfg: Configure virtue honesty and enables it.
* Housing.cfg: Configure parameters referred to 
* Loot.cfg: Configure loot parametrization.
* PlayerCaps.cfg: Configure player stats.
* Reports.cfg: Configure automatic reports
* Server.cfg: Configure here the name and port of your server.
* Shadowguard.cfg: Configure parameters referred to Shadow guards at Minax's fortress in the Valley of Eodon.
* Siege.cfg: Configure parameters referred to siege mode
* Staff.cfg: Configure parameters referred to gmbody-command
* Store.cfg: Configure parameters referred to Ultima Store.
* TestCenter.cfg: Set up test mode in startup. 
* TreasureMaps.cfg: Enable treasure spawn and allow customize it.
* Vendors.cfg: Set up vendors and spawn times.
* VetRewards.cfg: Enable Veteran regards and its configuration.
* VvV.cfg: Configure parameters referred to Virtue/Vice system.
* XmlSpawner2.cfg: Configure parameters referred to XmlSpawner2.

Note: It is required to restart the server after a change. Use restart option in server script or switch off and switch on the execution.