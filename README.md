# distroParser
Small python program to download XML from DistroWatch, parse, and maintain newly released Linux ISO torrent files.

Keeps track of how old the XML is, limiting to 1 update per day by default.

Removes old torrent files, limited to 1 year by default.

Meant to be used in conjunction with cron in a linux system to maintain/seed current Linux ISO torrent files.
