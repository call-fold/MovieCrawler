#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Common.CrawlerToHTML
import Common.CommonMovieCrawler
import Common.FileCommon
import os
import re


def change_code_type(input_str, encode_type):
    return input_str.encode(encode_type)


def change_search_str(byte_input):
    temp_str = str(byte_input).replace('\\x', '%')
    return re.findall(r'b\'(.+?)\'', temp_str)[0]


def make_search_url(search_url, add_str):
    return search_url + add_str


def get_search_url(default_search_url, search_str):
    search_str_byte = change_code_type(search_str, 'gbk')
    real_search_str = change_search_str(search_str_byte)
    real_search_url = make_search_url(default_search_url, real_search_str)
    return real_search_url


def compile_url_movie(url):
    return 'http://www.ygdy8.com' + url


def compile_url_page(url):
    return 'http://s.dydytt.net' + url


def delete_str_last_char(str):
    str_list = list(str)
    str_list.pop()
    return "".join(str_list)


def get_all_pages(url, decode_type='utf-8'):
    page_link_set = set(
        Common.CrawlerToHTML.get_links_from_html_separate(url, '/plus/search.php?keyword=', decode_type))
    real_page_link_list = []
    # 判断是否需要翻页
    if page_link_set:
        print('have more pages')
        real_page_link_list = list(map(compile_url_page, page_link_set))
        first_page_link = delete_str_last_char(real_page_link_list[0]) + '1'
        real_page_link_list.append(first_page_link)
        real_page_link_list.sort()
        return real_page_link_list
    else:
        print('only one page')
        real_page_link_list.append(url)
        return real_page_link_list


def get_movie_list(url, decode_type='utf-8'):
    movie_link_list = Common.CrawlerToHTML.get_links_from_html_re(url, '/html/(\w*)/(\w*)/2', decode_type)
    real_movie_link_list = list(map(compile_url_movie, movie_link_list))
    return real_movie_link_list


def get_total_movie_download_list(search_index_url, decode_type='utf-8', if_add_title=False):
    page_link_list = get_all_pages(search_index_url, decode_type)
    print(page_link_list)
    total_movie_link_list = []
    for page_link in page_link_list:
        total_movie_link_list += get_movie_list(page_link, decode_type)
    total_movie_download_list = Common.CommonMovieCrawler.get_movie_download_list(total_movie_link_list, decode_type,
                                                                                  if_add_title)
    return total_movie_download_list


if __name__ == '__main__':
    # input_name = input('movie to search: ')
    input_name = '火影忍者'
    my_search_index_url = get_search_url('http://s.dydytt.net/plus/search.php?kwtype=0&searchtype=title&keyword=',
                                         input_name)
    search_movie_download_list = get_total_movie_download_list(my_search_index_url, 'gbk', False)
    print('num of searched movies: ' + str(len(search_movie_download_list)))
    Common.FileCommon.write_result_to_txt(search_movie_download_list, os.path.abspath('.'), input_name + '.txt')
