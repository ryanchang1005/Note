from playwright import sync_playwright

from config.config import *
from services.map_scrape import MapScrapeService

if __name__ == '__main__':
    for keyword in keyword_list:
        for city in city_list:
            try:
                with sync_playwright() as playwright:
                    MapScrapeService.run(playwright, f'{city} {keyword}')
            except Exception as e:
                print(str(e))
    # with sync_playwright() as playwright:
    #     MapScrapeService.run(playwright, f'台北 美食')
