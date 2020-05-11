# Template-Migration
 This software automates the process to migrate one Network from standalone to template format (recreating the VLAN config)

HOW TO USE:

1 - Insert your credentials under the config.py file.

2 - Run the getVLANs.py file, it will list all your Networks so you can choose which Network you wish to migrate.

3 - Migrate the Network using the Meraki Dashboard (No API available to do this job right now)

4 - Run the updateVLANs.py file, it will ask you the name of the file previously generated using the getVLANs script and will update your migrated Network to the values saved on the NETWORK-NAME.json.

5 - Enjoy your free time.
