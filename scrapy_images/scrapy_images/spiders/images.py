import csv
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

        with open("data.csv", "a", newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)

            # Write the header row
            csv_writer.writerow(["Name", "Image_URL"])

            for flag in flags:
                img = flag.css("a>img").attrib["src"]
                name = flag.css("::text").get()

                csv_writer.writerow([name, f"https://www.worldometers.info{img}"])



