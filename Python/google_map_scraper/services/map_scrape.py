import re

from services.file import FileService


class MapScrapeService:

    @staticmethod
    def run(playwright, keyword):
        timeout = 5000
        browser = playwright.chromium.launch(headless=True)
        context = browser.newContext()
        context.setDefaultTimeout(timeout)  # timeout

        page = context.newPage()
        page.setDefaultTimeout(timeout)

        print(f'keyword={keyword}')
        page.goto(f'https://www.google.com.tw/maps/search/{keyword}')
        for search_page in range(1):

            exception_count = 0

            for row in range(10):
                # skip, if exception too high
                if exception_count >= 5:
                    continue

                try:
                    raw_row = row * 2 + 1

                    MapScrapeService.scrape_one_row(page, raw_row)
                except Exception as e:
                    print(f'{str(e)}, exception_count={exception_count}')
                    exception_count += 1

            # next_page(page)

        # Close page
        page.close()

        # ---------------------
        context.close()
        browser.close()

    @staticmethod
    def scrape_one_row(page, row):
        # name
        def scrape_name(page):
            text = MapScrapeService.scrape_text_content(
                page,
                [
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]'
                ]
            )
            if text is None:
                raise Exception('Scrape name timeout')
            return text

        # category
        def scrape_category(page):
            text = MapScrapeService.scrape_text_content(
                page,
                [
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]'
                    '/span[1]/span[1]/button'
                ]
            )
            if text is None:
                raise Exception('Scrape category timeout')
            return text

        # address
        def scrape_address(page):
            text = MapScrapeService.scrape_text_content(
                page,
                [
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[10]/button/div[1]/div[2]/div[1]',
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[11]/button/div[1]/div[2]/div[1]',
                    '/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[12]/button/div[1]/div[2]/div[1]',
                ]
            )
            if text is None:
                raise Exception('Scrape address timeout')
            return text

        # address
        def scrape_google_map_url(page):
            text = MapScrapeService.scrape_text_content(
                page,
                [
                    '/html/body/jsl/div[3]/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div[4]/div[2]/div[1]/input'
                ]
            )
            if text is None:
                raise Exception('Scrape google_map_url timeout')
            return text

        # latlng
        def scrape_latlng(url):
            # 'https://www.google.com.tw/maps/place/%E9%87%91%E6%B2%A2%E6%8B%89%E9%BA%B5/@25.0673351,121.5255703,15z/data=!4m8!1m2!2m1!1z5ouJ6bq1!3m4!1s0x3442a9dba82ad7e7:0xcb15d355dde48722!8m2!3d25.0648153!4d121.5253428'
            try:
                match_list = re.findall("\d+\.\d+", url)
                return match_list[-2], match_list[-1]
            except:
                print(url)
                return None, None

        data = {}

        # Click 1 row
        MapScrapeService.click_row(page, row)

        data['name'] = scrape_name(page)
        data['category'] = scrape_category(page)
        data['address'] = scrape_address(page)
        data['lat'], data['lng'] = scrape_latlng(page.evaluate('document.URL'))

        page.click("img[alt=\"分享\"]")
        data['google_map_url'] = scrape_google_map_url(page)
        page.click("button[aria-label=\"關閉\"]")

        print(f'{data["name"]} ok')

        FileService.write_file_by_append([
            data['name'],
            data['category'],
            data['address'],
            data['google_map_url'],
            data['lat'],
            data['lng'],
        ], 'data/output.csv')

        MapScrapeService.go_back(page)

    @staticmethod
    def go_back(page):
        try:
            # Google Map返回按鈕
            with page.expect_navigation():
                page.click("text=\"返回結果\"")
                return
        except Exception as e:
            pass

        try:
            # 瀏覽器返回
            page.goBack()
            return
        except Exception as e:
            pass

        raise Exception('Go back timeout...')

    @staticmethod
    def next_page(page):
        try:
            with page.expect_navigation(timeout=5000):
                page.click(
                    "//button[normalize-space(@aria-label)='下一頁']/img", timeout=5000)
                return
        except Exception as e:
            pass

        raise Exception('Next page timeout...')

    @staticmethod
    def click_row(page, row):
        try:
            page.click(
                f'xpath=/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div[{row}]')
            return
        except Exception as e:
            pass

        try:
            page.click(
                f'xpath=/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[{row}]')
            return
        except Exception as e:
            pass

        raise Exception(f'Click timeout, row={row}')

    @staticmethod
    def scrape_text_content(page, xpath_list):
        for xpath in xpath_list:
            try:
                return page.textContent(f'xpath={xpath}')
            except Exception as e:
                pass
        return None
