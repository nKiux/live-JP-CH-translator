# live-JP-CH-translator
Live translator for PC input

# 更新消息
Version 2
- 新增requirements.txt提供套件安裝
- 新增DeepL翻譯 (需自備API Key，獲取API Key的方法請[參考此影片](https://www.youtube.com/watch?v=f_QhiUK80kQ&ab_channel=TutorialsWithJames))
- 新增錯誤訊息
- 改進version 1無法邊偵測邊語音識別的問題

# 使用教學

## **Pre. 先下載上方除了README.md外其他檔案並存至同一個資料夾**
## - 1. 安裝 [VB-Virtual Audio Device](https://vb-audio.com/Cable/)
## - 2. 安裝後將CABLE Input設定為預設播放裝置

![image](https://github.com/nKiux/live-JP-CH-translator/assets/46084374/820300ed-2ee2-4ba3-a0ca-e91c96685375)

## - 3. 到錄製，選擇電腦音訊輸出並且將聆聽此裝置勾選，並且將透過此裝置播放選擇為使用中的耳機

![image](https://github.com/nKiux/live-JP-CH-translator/assets/46084374/9908bc11-15ce-43d0-92e1-44c234c383d1)


## - 4. 在同一個資料夾開啟終端機或者CMD(命令提示字元)並輸入下列指令
`python.exe -m pip install -r requirements.txt`

## __**(註：請先安裝Python並加入PATH)**__

## - 5. 先使用IDE (VSCode或其他Python編輯器) 分別啟動兩個程式確認是否有錯誤訊息，若有：
  - 嘗試Debug
  - 截圖錯誤訊息並在Issues提出問題

    ![image](https://github.com/nKiux/live-JP-CH-translator/assets/46084374/e00764b0-028f-41f3-a77a-355848e849e4)

## - 6. 確認沒有錯誤訊息後使用Python同時開啟兩個程式，開啟先後順序不影響

## - 7-1. 若要使用DeepL，請將API Key輸入`.env`檔案內，請移除井字號(#)
檔案範例：
`你的API Key`
## - 7-2. 若要使用Google翻譯，請將`.env`檔案內的字元清空，並輸入井字號(#)
檔案範例
`#`

# 備註
- 程式預設使用Google Translate機器翻譯，準確度與連續對話翻譯結果僅供參考
- 建議搭配語音辨識結果理解文意
- 若有需要新增功能或其他問題，歡迎至Issues提出！我會一一回覆並提出修正

# 預覽：
![image](https://github.com/nKiux/live-JP-CH-translator/assets/46084374/a3c1f232-1cb0-4b6d-aef8-4f1cd3178552)
