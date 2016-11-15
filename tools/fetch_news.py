#!/usr/bin/env python3

import urllib.request
import re
import os
import html as pyhtml

def fetch_all_news_links():

    result = set()
    visited = set()

    url = "https://manjaro.org/news/"

    while url:

        print("Visit " + url + " ...")
        visited.add(url)
        html = urllib.request.urlopen(url).read().decode("utf-8")

        matches = re.findall("\"https:\\/\\/manjaro.org\\/\\d{4}\\/\\d{2}\\/\\d{2}\\/\\S+\\/\"", html)
        matches_pages = re.findall("\"https:\\/\\/manjaro.org\\/news\\/page\\/\\d+\\/\"", html)

        result |= set([ m[1:-1] for m in matches])
        matches_pages = set([ m[1:-1] for m in matches_pages]) - visited

        print("Found " + str(len(result)) + " links")

        if matches_pages:
            url = list(matches_pages)[0]
        else:
            url = None

    return result

def make_archives():

    news_urls = set()

    f = open("news_links.txt", "r")

    for _line in f:
        line = _line.strip()

        if line:
            news_urls.add(line)

    f.close()

    if not os.path.exists("news-archive"):
        os.mkdir("news-archive")

    archives = { url.split("/")[4] + "_" + url.split("/")[3] : { "month" : int(url.split("/")[4]), "year" : int(url.split("/")[3]), "name" : url.split("/")[4] + "_" + url.split("/")[3]} for url in news_urls }
    archives = list(sorted(archives.values(), key = lambda x: x["year"] * 12 + x["month"]))
    archive_names = [ x["name"] for x in archives]

    for arch in archives:

        year = arch["year"]
        month = arch["month"]
        name = arch["name"]

        print(name)

        f = open("news-archive/" + name + ".md", "w")

        f.write("\n".join(["+++",
         "archive = \"" + name + "\"",
         "weight = " + str(archive_names.index(name)),
         "title = \"" + str(month) + "/" + str(year) + "\"",
         "type = \"news-archive\"",
         "+++"
         ]))

        f.close()

def extract_news():

    news_urls = set()

    f = open("news_links.txt", "r")

    for _line in f:
        line = _line.strip()

        if line:
            news_urls.add(line)

    f.close()

    for url in news_urls:

        print("Visit " + url)

        html = urllib.request.urlopen(url).read().decode("utf-8")


        f = open("debug.html", "w")
        f.write(html)
        f.close()

        html = html.replace("\r","").replace("\n", "")

        title = pyhtml.unescape(re.split("[><|]", re.findall("<title>.*<\\/title>", html)[0].strip())[2]).strip()
        author = pyhtml.unescape(re.split("[><]", re.findall("\"author\">.*<\\/a>", html)[0].strip())[1]).strip()
        date = pyhtml.unescape(re.split("[><]", re.findall("\"entry-date\">.*<\\/li>", html)[0].strip())[1]).strip()
        content = pyhtml.unescape(re.split("[><]", re.findall("\"text\">.*", html)[0].strip())[1]).strip()

        print(title + " by " + author + " on " + date)
        print(content)

        return


def main():

    if not os.path.exists("news_links.txt"):
        f = open("news_links.txt", "w")
        f.write("\n".join(fetch_all_news_links()))
        f.close()
    else:
        print("Skipping extraction of news links")

    make_archives()
    extract_news()

main()
