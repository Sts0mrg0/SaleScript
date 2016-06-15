#!/usr/local/bin/python

import urllib
import sys

inShort = False
all = False
if (sys.argv).__contains__("a"):
    all = True
if (sys.argv).__contains__("s"):
    inShort = True

brands = {
    "Bally": "http://www.bally.co.uk/en_gb/home/",
    "Ferragamo": "http://www.ferragamo.com/shop/en/uk",
    "Harrods": "http://www.harrods.com/",
    "Selfridge": "http://www.selfridges.com/GB/en/",
    "Harvey Nichols": "http://www.harveynichols.com/",
    "Burberry": "https://uk.burberry.com/",
    "Sandro": "http://uk.sandro-paris.com",
    "the Kooples": "http://www.thekooples.co.uk/",
    "gz": "http://www.giuseppezanottidesign.com/uk",
    "prada man": "http://www.prada.com/en/GB/e-store/department/man/new-arrivals.html",
    "prada": "http://www.prada.com/en.html?cc=GB",
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
    "cl men": "http://eu.christianlouboutin.com/uk_en/homepage-1/men-collection.html",
    "apc men": "http://www.apc.fr/wwuk/men.html",
    "coach": "http://uk.coach.com/",
    "mulberry": "http://www.mulberry.com/",
    "tods": "http://www.tods.com/en_gb/",
    "bv": "http://www.bottegaveneta.com/gb"
    # "": "",
}

saleWords = ["/sale/", ">sale<", "reduction", "outlet", "sale", "% off"]

terms = "Terms & Conditions of sale"

for brandName, url in brands.iteritems():
    response = urllib.urlopen(url)
    html = response.read()
    wordDict = {}
    for word in saleWords:
        if not all and word == "sale":
            continue
        wordCount = html.lower().count(word)
        termsLineCount = html.lower().count((terms).lower())
        wordMatchCount = wordCount - termsLineCount
        wordDict[word] = wordMatchCount
    if sum(wordDict.values()) > 0:
        outLine = brandName + " is on sale!  "
        if not inShort:
            outLine += str(wordDict)
        print(outLine)
