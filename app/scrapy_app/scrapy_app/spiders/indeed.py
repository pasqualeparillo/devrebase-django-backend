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
                'job_company': ,
                'job_title': job.css("div.title > a::attr(title)").extract_first(),
                'job_body': job.css("div.summary::text"),
                'job_url': job.css("div.title > a::attr(href)"),
                'job_source': job.setdefault('indeed'),
                'job_location': job.css("div > div::attr(loc)"),
            }

        next_page_url = response.css("div.pagination > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))