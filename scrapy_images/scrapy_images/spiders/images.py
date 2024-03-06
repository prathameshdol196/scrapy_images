import csv
import mysql.connector
import os
import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["worldometers.info"]
    start_urls = ["https://worldometers.info"]

    def start_requests(self):
        urls = [
            "https://www.worldometers.info/geography/flags-of-the-world/"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        flags = response.css(".col-md-4")

        for flag in flags:
            img_url = flag.css("a>img").attrib["src"]
            name = flag.css("::text").get().strip()

            yield {
                'name': f"{name}.jpg",
                'image_urls': [f"https://www.worldometers.info{img_url}"]
            }




