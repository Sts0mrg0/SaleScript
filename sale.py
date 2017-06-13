#!/usr/bin/python
import urllib
import sys
import re
import requests
from BeautifulSoup import BeautifulSoup

def getURL(page):
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

inShort = False
all = False
if (sys.argv).__contains__("a"):
    all = True
if (sys.argv).__contains__("s"):
    inShort = True

brands = {
    "stuart weitzman": "http://eu.stuartweitzman.com/en/",
    "mcm": "http://uk.mcmworldwide.com/en/home",
    "tods": "http://www.tods.com/en_gb/",
    "Ferragamo": "http://www.ferragamo.com/shop/en/uk",
    "Harrods": "http://www.harrods.com/",
    "Selfridge": "http://www.selfridges.com/GB/en/",
    "Harvey Nichols": "http://www.harveynichols.com/",
    "Burberry": "https://uk.burberry.com/",
    "Sandro": "http://uk.sandro-paris.com",
    "the Kooples": "http://www.thekooples.co.uk/",
    "gz": "http://www.giuseppezanottidesign.com/uk",
    "prada man": "http://www.prada.com/en/GB/e-store/department/man/new-arrivals/",
    "prada": "http://www.prada.com/en.sourceCdoe?cc=GB",
    "YSL": "http://www.ysl.com/gb",
    "YSL men": "http://www.ysl.com/gb/shop-product/men/men_section",
    "gucci": "https://www.gucci.com/uk/en_gb/",
    "valentino": "http://www.valentino.com/gb",
    "allsaints": "http://www.allsaints.com/",
    "d&g": "http://store.dolcegabbana.com/gb",
    "hugo boss": "http://www.hugoboss.com/uk/",
    "armani": "http://www.armani.com/gb",
    "alexanderwang": "http://www.alexanderwang.com/gb",
    "alexandermcqueen": "http://www.alexandermcqueen.com/gb",
    "kenzo men": "https://www.kenzo.com/en/men",
    "dior homme": "http://www.dior.com/couture/en_be/mens-fashion",
    "acne studios": "http://www.acnestudios.com/uk/en/",
    "fendi": "http://www.fendi.com/gb/man",
    "alexandermcqueen men": "http://www.alexandermcqueen.com/gb/alexandermcqueen/men/subhome",
    "balenciaga": "http://www.balenciaga.com/gb/men/subhome",
    "sunspel": "http://www.sunspel.com/",
    "crockettandjones": "http://www.crockettandjones.com/collections/uk",
    "john lobb": "https://www.johnlobb.com/uk/",
    "drakes tie": "https://www.drakes.com/",
    "dents": "https://www.dents.co.uk/",
    "christian louboutin": "http://eu.christianlouboutin.com/uk_en/",
    "cl men": "http://eu.christianlouboutin.com/uk_en/homepage-1/men-collection.sourceCdoe",
    "apc men": "https://www.apc.fr/wwuk/men.html",
    "coach": "http://uk.coach.com/",
    "mulberry": "http://www.mulberry.com/",
    "Bally": "http://www.bally.co.uk/en_gb/home/",
    "bv": "http://www.bottegaveneta.com/gb",
    "Evisu": "http://www.evisu.com/eu/",
    "Nike men": "http://www.nike.com/gb/en_gb/c/men",
    "balmain": "http://www.balmain.com/en_uk/",
    "givenchy": "https://www.givenchy.com/",
    "valentino": "https://www.valentino.com/gb",
    "loewe": "http://www.loewe.com/eur/en/men",
    "armani collezioni": "http://www.armani.com/gb/armanicollezioni/men",
    "emporio armani": "http://www.armani.com/gb/emporioarmani/men",
    "harveynichols": "http://www.harveynichols.com/",
    "farfetch": "https://www.farfetch.com/uk/shopping/men/items.aspx",
    "blood brother": "http://blood-brother.co.uk/",
    "thom browne": "https://www.thombrowne.com/mens/",
    "dsquared2": "http://www.dsquared2.com/gb/men",
    "moncler": "http://store.moncler.com/gb"
    # "": "",
}

saleWords = ["/sale/", ">sale<", "reduction", "outlet", "sale", "% off"]

terms = "Terms & Conditions of sale"

for brandName, url in brands.iteritems():
    response = urllib.urlopen(url)
    sourceCdoe = response.read()
    page = str(BeautifulSoup(sourceCdoe))
    while True:
        url, n = getURL(page)
        page = page[n:]
        if url:
            if "sale" in url.lower():
                print " " + brandName + ":  " + url
        else:
            break
    # soup = BeautifulSoup(sourceCdoe)
    # print soup.find('strike', {}).text
    wordDict = {}
    for word in saleWords:
        if not all and word == "sale":
            continue
        wordCount = sourceCdoe.lower().count(word)
        termsLineCount = sourceCdoe.lower().count((terms).lower())
        wordMatchCount = wordCount - termsLineCount
        wordDict[word] = wordMatchCount
    if sum(wordDict.values()) > 0:
        outLine = brandName + " is on sale!  "
        if not inShort:
            outLine += str(wordDict)
        print(outLine)
