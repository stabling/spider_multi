from scrapy import cmdline
from scrapy.cmdline import execute

# cmdline.execute("scrapy crawl ivsky".split(" "))

# cmdline.execute("scrapy crawl zol".split(" "))
# cmdline.execute("scrapy crawl cha".split(" "))
# cmdline.execute("scrapy crawl star".split(" "))
# cmdline.execute("scrapy crawl xsnvshen".split(" "))
# cmd='scrapy crawl start_urls -a "start_urls=http://stackoverflow.com,http://httpbin.org"'
# cmdline.execute(cmd)


execute(['scrapy', 'crawl', 'xsnvshen',"-a","start_urls=https://www.xsnvshen.com/album/?p=0"])

# cmdline.execute("scrapy crawl sexmen".split(" "))

# cmdline.execute("scrapy crawl xsnvshen2".split(" "))


