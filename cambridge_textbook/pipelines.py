# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CambridgeTextbookPipeline(object):

    def open_spider(self, spider):
        self.file = open('book.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):

        print("=========item========")
        print(item)
        if item.get('author'):
            item['author'] = item['author'].strip('\n ')
            self.file.write('{} -- {} \n' .format(item.get('chapter'), item.get('author')))
            return item
