#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.crawler_to_html import get_title_from_html, get_links_from_html_keyword


def get_movie_download_tuple(url, decode_type='utf-8'):
    movie_title = get_title_from_html(url, decode_type)
    download_link_list = get_movie_download_link(url, decode_type)
    if len(download_link_list) == 0:
        return movie_title, ''
    else:
        return movie_title, download_link_list[0]


def get_movie_download_link(url, decode_type='utf-8'):
    download_link_list = get_links_from_html_keyword(url, 'ftp', decode_type)
    return download_link_list


def get_movie_download_list(real_movie_link_list, decode_type='utf-8', if_add_title=True):
    movie_download_list = []
    for real_movie_link in real_movie_link_list:
        if if_add_title:
            movie_download_link_by_page = get_movie_download_tuple(real_movie_link, decode_type)
            if movie_download_link_by_page[1] is not '':
                print(movie_download_link_by_page)
                movie_download_list.append(movie_download_link_by_page)
        else:
            movie_download_list_by_page = get_movie_download_link(real_movie_link, decode_type)
            if movie_download_list_by_page:
                movie_download_list.extend(movie_download_list_by_page)
    return movie_download_list


def get_movie_download_dict(movie_download_tuple_list):
    movie_download_dict = dict()
    for movie_tuple in movie_download_tuple_list:
        movie_title = movie_tuple[0]
        download_url = movie_tuple[1]
        movie_download_dict[movie_title] = download_url
    return movie_download_dict
