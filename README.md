# distroParser
Small python program to download XML from DistroWatch, parse, and maintain newly released Linux ISO torrent files.

Keeps track of how old the XML is, limiting to 1 update per day by default changed by modifying ```xml_age_to_keep```.

Removes old torrent files, limited to 1 year by default changed by modifying ```distro_age_to_keep```.

Meant to be used in conjunction with cron in a linux system to maintain/seed current Linux ISO torrent files.

To Use:

  Place file in whatever directory suites you.  Modify any of the paths (torrentXML, logDir, or torrentDir) to your liking use the full path for each.
  
  Ensure the "torrentDir" variable (```./torrents/``` by default) matches the full path of the watch directory of your torrent client.
  
  Enable execution of the script with ```sudo chmod a+x ./distroParser.py```
  
  Ensure that all files have adequate permissions for the user.  ```sudo chown -R $USER /FULL/PATH/TO/DIR/```
  
  Can then put an entry in crontab for automatic updates to torrent files using:
  
  ```/usr/bin/python3    /FULL/PATH/TO/distroParser.py```
  
  Note, the log file will continuously append the output and a list of torrents/xml downloaded (if any).  It will keep a log for 3 months and start anew if the file is found to be older than this.
  
  Note 2, some torrent clients append ```.added``` to the filename of the torrent file once it's been worked.  This program checks for the filename + .added.
