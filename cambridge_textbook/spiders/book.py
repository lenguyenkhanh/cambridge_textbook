# -*- coding: utf-8 -*-
import scrapy

class BookSpider(scrapy.Spider):
    name = 'book'
    start_urls = ['https://www.cambridge.org/core/books/how-to-prove-it/6D2965D625C6836CD4A785A2C843B3DA']

    def parse(self, response):
        for chapter in response.css("li.title h5"):
            link_chapter = chapter.css("a.part-link::attr(href)").get()
            if link_chapter:
                link_chapter = response.urljoin(link_chapter)
                yield scrapy.Request(link_chapter, callback=self.parse_chapter)

    def parse_chapter(self, response):
        yield {
            "author": response.css("span.author-name::text").get(),
            "chapter": response.css("h1.article-title::text").get()
        }