# squash
- 合併commit, 當你"add func test1"後發現有個小地方要補, 而再去commit一個小修正"fix syntax error", 會顯得commit很分散, 我們可以合併commit(053ae04 + d59f4f9)

![rebase1](images/rebase1.png)
```
git rebase -i 04bca74  // 先進入更之前的commit的rebase互動模式, -i = interactive
```

![rebase2](images/rebase2.png)
```
將pick 053ae04改為squash 053ae04, 儲存
squash : 如同底下解釋和前一個(上方)commit融合
```

![rebase3](images/rebase3.png)
```
上一個步驟儲存後會到此畫面(上), 準備合併commit
井號(#)後方的文字會被忽略, 所以只需要保留要合併起來的內容即可
```

![rebase4](images/rebase4.png)
```
最後log一下, 剛才那兩個commit就融合了
```