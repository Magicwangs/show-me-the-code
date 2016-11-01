## 录音
`PyAudio`和`wave`    
- [PyAudio API](http://people.csail.mit.edu/hubert/pyaudio/docs/#pyaudio.Stream.read)
- [声音输入输出](http://old.sebug.net/paper/books/scipydoc/wave_pyaudio.html#id5)
- [xyjxyf Github](https://github.com/Show-Me-the-Code/python/blob/master/xyjxyf/0025/voice_open_browser.py)

##  Speech To Text API
谷歌的`Google Cloud Speech API`虽然传闻很牛，但是没有信用卡的孩子不能用，尝试了N多方法，最终得到的还是
```
HttpError: <HttpError 403 when requesting https://speech.googleapis.com/$discovery/rest?version=v1beta1 returned "Project magicwang-1151 (#796947488330) has billing disabled. Please enable it.">
```
我有一颗谷粉的心，奈何太年轻没办信用卡。。。
有信用卡的孩子可以按[这个教程](http://oranwind.org/-linkit-smart-7688-shi-yong-google-speech-recognition-fu-wu/)试试,墙内记得用代理。   
所幸IBM还是相对人性化的，有30天试用期，如果超过30，就必须添加信用卡才能使用。    
相关参考：   
- [基于IBM STT(语音识别)的Python side project](http://yabzhang.github.io/%E6%9D%82%E8%AE%B0/2016/04/09/a-python-based-on-ibm-stt-api)
- [speech_recognition](https://github.com/Uberi/speech_recognition)
