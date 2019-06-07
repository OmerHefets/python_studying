import urllib
import sys
import os

GVAHIM_URL = "http://data.cyber.org.il/python/logpuzzle/"
MESSAGE_FILE = "log_files/message_data.cyber.org.il"
LOGO_DATA_FILE = "log_files/logo_data.cyber.org.il"
URL_STRING = "/python/logpuzzle/"


def read_file(source_path):
    with open(source_path, "r") as file:
        line_list = file.readlines()
        return line_list


def read_urls(list_of_lines):
    list_of_urls = []
    for line in list_of_lines:
        if URL_STRING in line:
            start_index = line.find(URL_STRING)
            search_for_space = line[start_index:]
            end_index = search_for_space.find(' ')
            print(search_for_space[:end_index])


def sort_urls():
    pass


def write_html_gui():
    pass


def add_urls_to_html():
    pass


def main():
    urls = []
    lines = read_file(LOGO_DATA_FILE)
    read_urls(lines)
    pass


if __name__ == "__main__":
    main()
