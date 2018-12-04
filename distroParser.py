#!/usr/bin/python3

import xml.etree.ElementTree as ET
import urllib.request as requestit
import os, stat, time, sys
from datetime import date

# List of linux distros to look out for.  Case and format is sensitive/specific to naming schemes.
distros = ["debian", "neon", "raspbian", "ubuntu", "antergos", "manjaro", "CentOS", "Fedora", "kali", "tails", "popos",
           "ipfire", "elementaryos", "pfsense", "openmediavault", "FreeNAS", "FreeBSD", "Peppermint", "linuxmint",
           "openSUSE", "Zorin", "proxmox", "gparted-live", "systemrescuedc", "OSMC", "FreeBSD", "untangle"]

# Provides length to keep torrent files (years) and xml (days)
distro_age_to_keep = 1
xml_age_to_keep = 1

# Paths for XML file, log file, and torrent client watch dir.
torrentXML = "./torrents.xml"
logDir = "./message.log"

torrentDir = "./torrents/"

# URL for DistroWatch RSS feed, provides xml.
url = 'https://distrowatch.com/news/torrents.xml'

# Sets print to output to log instead of stdout
old_stdout = sys.stdout
log_file = open(logDir, "a")
sys.stdout = log_file


def file_age_in_years(pathname):
    return (time.time() - os.stat(pathname)[stat.ST_MTIME])/31540000


def file_age_in_days(pathname):
    return (time.time() - os.stat(pathname)[stat.ST_MTIME])/86400


def check_if_exists(pathname):
    return os.path.isfile(pathname)


def delete_old_torrents(pathname):
    for filename in os.listdir(pathname):
        if file_age_in_years(pathname+filename) > distro_age_to_keep:
            print('Removing old file:', filename)
            os.remove(pathname+filename)


def print_run_date():
    print('Run on: ' + str(date.today()))


def parse_xml(xml):
    print_line_msg('Parsing XML File')

    for item in xml[0].findall('item'):
        if item.text != xml[0][0].text:
            for name in distros:
                if name in item[0].text:
                    if check_if_exists(torrentDir + item[0].text + '.added') or \
                            check_if_exists(torrentDir + item[0].text):
                        print('\t---Already Exists', item[0].text, '---')
                        break
                    else:
                        print('\t---Downloading', item[0].text, '---')
                        requestit.urlretrieve(item[1].text, torrentDir + item[0].text)
                        break


def get_xml(file):
    if (not os.path.isfile(file)) or (file_age_in_days(torrentXML) > xml_age_to_keep):
        print_line_msg('Downloading latest XML file from DistroWatch')
        requestit.urlretrieve(url, file)
    else:
        print_line_msg('Using existing XML file from DistroWatch')


def wrap_it_up():
    print_line_msg('Finished Updating Torrent Files')
    print('\n\n\n\n')

    sys.stdout = old_stdout
    log_file.close()


def print_line_msg(msg):
    print('--------------------------------------------------')
    print(msg)
    print('--------------------------------------------------')


def check_log_age(path_to_log):
    if os.path.isfile(path_to_log) and file_age_in_years(path_to_log) > .25:
        os.remove(path_to_log)
        print('New Log started' + str(date.today()))


check_log_age(logDir)

get_xml(torrentXML)

tree = ET.parse(torrentXML)
root = tree.getroot()

print_run_date()

parse_xml(root)

delete_old_torrents(torrentDir)

wrap_it_up()
