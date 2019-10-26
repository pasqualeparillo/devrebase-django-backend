# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from api.models import Job

class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        item = Job(job_body=item.get('text'), job_company=item.get('author'), job_title=item.get('author'), job_source=('indeed'), job_url=item.get('url'), job_location=item.get('location') )
        item.save()
        return item