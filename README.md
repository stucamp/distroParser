# distroParser
Small python program to download XML from DistroWatch, parse, and maintain newly released Linux ISO torrent files.

Keeps track of how old the XML is, limiting to 1 update per day by default changed by modifying ```xml_age_to_keep```.

Removes old torrent files, limited to 1 year by default changed by modifying ```distor_age_to_keep```.

Meant to be used in conjunction with cron in a linux system to maintain/seed current Linux ISO torrent files.

To Use:

  Place file in whatever directory suites you.  Modify any of the paths (torrentXML, logDir, or torrentDir) to your liking.
  
  Ensure the "torrentDir" variable (```./torrents/``` by default) in the script to match the watch directory of your torrent client.
  
  Enable execution of the script with ```sudo chmod a+x ./distroParser.py```
  
  Ensure that all files have adequate permissions for the user.  ```sudo chown -R $USER /FULL/PATH/TO/DIR/```
  
  Can then put an entry for crontab for automatic updates to torrent files (or however frequently you choose) using ```/usr/bin/python3   /FULL/PATH/TO/distroParser.py```
