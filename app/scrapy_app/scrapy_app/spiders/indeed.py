# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class IndeedSpider(CrawlSpider):
    name = 'indeed'
    start_urls = [
        'https://www.indeed.com/jobs?q=software+engineer&l=',
    ]
    def parse(self, response):
        for job in response.css(".jobsearch-SerpJobCard"):
            yield {
                'job_company': job.xpath("normalize-space(.//div[@class='sjcl']/div/span/descendant::*/text())").get(default='Not Provided'),
                'job_title': job.css("a::attr(title)").extract_first(),
                'job_body': job.xpath("normalize-space(.//div[@class='summary'])").get(),
                'job_url': job.xpath("string(.//div[@class='title']/a/@href)").get(),
                'job_source': job.css("indeed.com"),
                'job_location': job.css("div.sjcl > div.accessible-contrast-color-location::text").extract_first(default="Not Provided"),
            }

        next_page_url = response.css("div.pagination > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))