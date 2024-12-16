import scrapy

from weather.items import WeatherItem

class ReportSpider(scrapy.Spider):
    name = "report"
    allowed_domains = ["weather.gov"]
    start_urls = ["https://forecast.weather.gov/MapClick.php?lat=39.9947&lon=-83.0041"]

    def parse(self, response):
        for report in response.css("div.tombstone-container"):
            item = WeatherItem()
            item["period"] = report.css(".period-name::text").get()

            # Get either the high or low temperature
            low_temp = report.css(".temp-low::text").get()
            high_temp = report.css(".temp-high::text").get()
            if low_temp:
                item["temperature"] = low_temp.split(": ")[1]
            if high_temp:
                item["temperature"] = high_temp.split(": ")[1]

            condition = report.css(".short-desc::text").getall()
            condition = " ".join([text.strip() for text in condition if text.strip()])
            item["condition"] = condition
            yield item
