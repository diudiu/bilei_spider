from scrapy.cmdline import execute

name = 'icodrops'
cmd = 'scrapy crawl {}'.format(name)
execute(cmd.split())