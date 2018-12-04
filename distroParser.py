import xml.etree.ElementTree as ET
import urllib.request as requestit
import os, stat, time, sys
from datetime import date

distros = ["debian", "neon", "raspbian", "ubuntu", "antergos", "manjaro", "CentOS", "Fedora", "kali", "tails", "popos",
           "ipfire", "elementaryos", "pfsense", "openmediavault", "FreeNAS", "FreeBSD", "Peppermint", "linuxmint",
           "openSUSE", "Zorin"]

torrentXML = "./torrents.xml"
torrentDir = "./torrents/"

old_stdout = sys.stdout
log_file = open("message.log", "a")
sys.stdout = log_file


def file_age_in_years(pathname):
    return (time.time() - os.stat(pathname)[stat.ST_MTIME])/31540000


def file_age_in_days(pathname):
    return (time.time() - os.stat(pathname)[stat.ST_MTIME])/86400


def check_if_exists(pathname):
    return os.path.isfile(pathname)


def delete_old_torrents(pathname):
    for filename in os.listdir(pathname):
        if file_age_in_years(pathname+filename) > .5:
            print('Removing old file:', filename)
            os.remove(pathname+filename)


def print_header(xml):
    today = str(date.today())
    print('Retreived XML: ', today)
    print('--------------------------------------------------')


def parse_xml(xml):
    print('Parsing XML File')
    print('--------------------------------------------------')

    for item in xml[0].findall('item'):
        if item.text != xml[0][0].text:
            for name in distros:
                if name in item[0].text:
                    if check_if_exists(torrentDir + item[0].text):
                        print('\t---Already Exists', item[0].text, '---')
                        break
                    else:
                        print('\t---Downloading', item[0].text, '---')
                        requestit.urlretrieve(item[1].text, torrentDir + item[0].text)
                        break
                        

def get_xml(file):

    if (not os.path.isfile(file)) or (file_age_in_days(torrentXML) > 1):
        print('--------------------------------------------------')
        print('Downloading latest XML file from DistroWatch')
        print('--------------------------------------------------')
        url = 'https://distrowatch.com/news/torrents.xml'
        requestit.urlretrieve(url, file)
    else:
        print('--------------------------------------------------')
        print('Using existing XML file from DistroWatch')
        print('--------------------------------------------------')


def wrap_it_up():
    print('--------------------------------------------------')
    print('Finished Updating Torrent Files')
    print('--------------------------------------------------')
    print('\n\n\n\n')

    sys.stdout = old_stdout
    log_file.close()


get_xml(torrentXML)

tree = ET.parse(torrentXML)
root = tree.getroot()

print_header(root)

parse_xml(root)

delete_old_torrents(torrentDir)

wrap_it_up()
