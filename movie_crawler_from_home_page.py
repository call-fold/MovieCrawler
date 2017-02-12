#!/usr/bin/env python
# -*- coding: utf-8 -*-

import common.crawler_to_html
import common.common_movie_crawler
import common.file_common
import os
import sys


def compile_url(url):
    return 'http://www.dytt8.net' + url


def get_movie_list(url, decode_type='utf-8'):
    movie_link_list = common.crawler_to_html.get_links_from_html_keyword(url, '/html/gndy/dyzz/2016', decode_type)
    movie_link_list = list(map(compile_url, movie_link_list))
    movie_link_set = set(movie_link_list)
    final_movie_link_list = list(movie_link_set)
    return final_movie_link_list


def main():
    my_index_url = 'http://www.dytt8.net/'
    my_real_movie_link_list = get_movie_list(my_index_url, 'gbk')
    search_movie_download_list = common.common_movie_crawler.get_movie_download_list(my_real_movie_link_list, 'gbk',
                                                                                     False)
    common.file_common.write_result_to_txt(search_movie_download_list, os.path.abspath('.') + '/top_movies',
                                          'movies2016.txt')
    # tv_url = 'http://www.ygdy8.com/html/tv/oumeitv/20151007/49245.html'
    # tv_list = get_tv_drama_program_list(tv_url, 'gbk')
    # write_result_to_txt(tv_list, os.path.abspath('.'), 'tv_drama_program_list.txt')


if __name__ == '__main__':
    main()
