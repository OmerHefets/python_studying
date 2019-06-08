import urllib
import sys
import os

GVAHIM_URL = "http://data.cyber.org.il"
MESSAGE_FILE_PATH = "log_files/message_data.cyber.org.il"
LOGO_DATA_FILE_PATH = "log_files/logo_data.cyber.org.il"
URL_STRING = "/python/logpuzzle/"
FIRST = True
SECOND = False


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
            list_of_urls.append(search_for_space[:end_index])
    return list_of_urls


def sort_logo_urls(list_of_urls):
    list_of_words = []
    for url in list_of_urls:
        word = extract_word_from_url(url, first_or_second=FIRST)
        list_of_words.append(word)
    zipped_lists = zip(list_of_words, list_of_urls)
    zipped_lists = sorted(zipped_lists)
    sorted_urls_list = [x for y, x in zipped_lists]
    return sorted_urls_list


def sort_message_urls(list_of_urls):
    list_of_words = []
    for url in list_of_urls:
        first_word = extract_word_from_url(url, first_or_second=FIRST)
        second_word = extract_word_from_url(url, first_or_second=SECOND)
        concat_words = second_word + first_word
        list_of_words.append(concat_words)
    zipped_lists = zip(list_of_words, list_of_urls)
    zipped_lists = sorted(zipped_lists)
    sorted_urls_list = [x for y, x in zipped_lists]
    return sorted_urls_list


def extract_word_from_url(url, first_or_second):
    if first_or_second == FIRST:
        index = nth_occurrence_index(url, '-', 1)
        # word length = 4 chars
        return url[index + 1:index + 5]
    else:
        index = nth_occurrence_index(url, '-', 2)
        return url[index + 1:index + 5]


def nth_occurrence_index(string, char, n):
    if n <= 0:
        exit("n must be a positive number")
    for i in range(len(string)):
        if string[i] == char:
            n -= 1
        if n == 0:
            return i
    return -1


def download_images(sorted_urls, dest_folder):
    for i in range(len(sorted_urls)):
        concat_prefix = GVAHIM_URL + sorted_urls[i]
        print(concat_prefix)


def write_html_gui():
    pass


def add_urls_to_html():
    pass


def main():
    # read urls:
    logo_lines = read_file(LOGO_DATA_FILE_PATH)
    logo_urls = read_urls(logo_lines)
    message_lines = read_file(MESSAGE_FILE_PATH)
    message_urls = read_urls(message_lines)

    # sort urls:
    sorted_logo_urls = sort_logo_urls(logo_urls)
    sorted_massage_urls = sort_message_urls(message_urls)

    # download the images:
    download_images(sorted_massage_urls, True)
    # write to the html file:


if __name__ == "__main__":
    main()
