# -*- coding: utf-8 -*- 
from config import *
import urllib
import json
import os
import pandas as pd
from bs4 import BeautifulSoup
import datetime
def get_today():
	return datetime.datetime.today().strftime("%Y%m%d")

def get_naver(query, collection):
	all_items = []
	params = {'key':key_naver, 'query':query, 'target':collection, 'start':1, 'display':100}
	base_url = base_url_naver
	url = base_url + '?' + urllib.urlencode(params)
	
	return eval(get_retrieve_function(url, collection))

def get_daum(query, collection):
	all_items = []

	for i in range(1, 6):
		params = {'q':query, 'apikey':key_daum, 'result':20, 'pageno':i}
		base_url = os.path.join(base_url_daum, collection)
		url = base_url + '?' + urllib.urlencode(params)
	
		all_items += eval(get_retrieve_function(url, collection))
		all_items += get_images(url)

	return all_items

def get_retrieve_function(url, collection):
	return 'get_' + collection + '(' + url + ')'

def get_socialpick():
	params = {'n':200, 'apikey':key_daum, 'output':'json'}
	url = base_url_socialpick + '?' + urllib.urlencode(params)
	search_result = urllib.urlopen(url)
	
	socialpick = json.loads(search_result.read())['socialpick']
	return socialpick['item']

def get_news(url):
	search_result = urllib.urlopen(url)
    data = search_result.read()
    soup = BeautifulSoup(data)

    items = soup.find_all('item')
	all_items = []

	for item in items:
        title = item.title.getText()
        originallink = item.originallink.getText()
        description = item.description.getText()
        current_item = {'title':title, 'originallink': originallink, 'description':description}
        all_items.append(current_item)

    return all_items


def get_images(url):
    search_result = urllib.urlopen(url)
    data = search_result.read()
    soup = BeautifulSoup(data)

    items = soup.find_all('item')
    all_items = []
    for item in items:
        title = item.title.getText()
        link = item.link.getText()
        image = item.thumbnail.getText()
        current_item = {'title':title, 'link': link, 'image':image}
        all_items.append(current_item)

    return all_items

