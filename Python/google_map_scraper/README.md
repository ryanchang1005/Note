# google_map_scraper

### 開始錄製
```
python -m playwright codegen --target python -o 'tmp.py' -b chromium https://www.google.com.tw/maps
```

### 準備
```python
keyword = '火鍋'
city_list = ['台北市', '新北', '宜蘭']  # 加在關鍵字的前綴, 例如 : "台北 火鍋"
search_center_location = ['121.5173748', '25.0477022']  # 給瀏覽器吃位置用

for page in range(5):

    # save exception count
    exception_count = 0  
    
    for row in range(20):
        try:
            # skip, if exception too high
            if exception_count >= 5:
                continue
            # scrape
        except Exception as e:
            # timeout
            print(str(e))
            
            # exception++
            exception_count += 1
            pass
        # next row
    # next page

```

### Reference
* Tutorial.1([link](https://segmentfault.com/a/1190000038697288))
* Playwright Github([link](https://github.com/microsoft/playwright-python))
* Playwright doc selectors([link](https://playwright.dev/docs/api/working-with-selectors/))
