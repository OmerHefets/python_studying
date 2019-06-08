import urllib.request
import sys
import os

GVAHIM_URL = "http://data.cyber.org.il"
MESSAGE_FILE_PATH = "log_files/message_data.cyber.org.il"
LOGO_DATA_FILE_PATH = "log_files/logo_data.cyber.org.il"
URL_STRING = "/python/logpuzzle/"
FOLDER_PATH = "~/programming/python/python_studying/log_puzzle"
LOGO_FOLDER_PATH = "logo_images"
MESSAGE_FOLDER_PATH = "message_images"

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
            url_from_start_index = line[start_index:]
            end_index = url_from_start_index.find(' ')
            full_url = url_from_start_index[:end_index]
            if full_url not in list_of_urls:
                list_of_urls.append(full_url)
    return list_of_urls


def sort_urls(list_of_urls, message):
    list_of_words = []
    if not message:
        for url in list_of_urls:
            word = extract_word_from_url(url, first_or_second=FIRST)
            list_of_words.append(word)
    else:
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
        url_with_prefix = GVAHIM_URL + sorted_urls[i]
        filename = 'img' + str(i)
        filename_and_path = dest_folder + '/' + filename + '.jpg'
        urllib.request.urlretrieve(url_with_prefix, filename_and_path)


def write_html_gui():
    pass


def add_urls_to_html():
    pass


def main(download):
    # read urls:
    logo_lines = read_file(LOGO_DATA_FILE_PATH)
    logo_urls = read_urls(logo_lines)
    message_lines = read_file(MESSAGE_FILE_PATH)
    message_urls = read_urls(message_lines)

    # sort urls:
    sorted_logo_urls = sort_urls(logo_urls, message=False)
    sorted_message_urls = sort_urls(message_urls, message=True)

    # download the images:
    if download:
        download_images(sorted_message_urls, MESSAGE_FOLDER_PATH)
        download_images(sorted_logo_urls, LOGO_FOLDER_PATH)
    # write to the html file:


if __name__ == "__main__":
    main(download=False)
