

BOT_NAME = "books"

SPIDER_MODULES = ["books.spiders"]
NEWSPIDER_MODULE = "books.spiders"



#USER_AGENT = "books (+http://www.yourdomain.com)"


ROBOTSTXT_OBEY = True


#CONCURRENT_REQUESTS = 32


#DOWNLOAD_DELAY = 3

#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


#COOKIES_ENABLED = False


#TELNETCONSOLE_ENABLED = False


#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}


#SPIDER_MIDDLEWARES = {
#    "books.middlewares.BooksSpiderMiddleware": 543,
#}

#DOWNLOADER_MIDDLEWARES = {
#    "books.middlewares.BooksDownloaderMiddleware": 543,
#}


#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}



ITEM_PIPELINES = {
   "books.pipelines.MongoPipeline": 300,
}


#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

MONGO_URI = "mongodb://locahost:27017"
MONGO_DATABASE = "books_db"

LOG_LEVEL = "INFO"
LOG_LEVEL = "WARNING"
LOG_FILE = "book_scraper.log"
