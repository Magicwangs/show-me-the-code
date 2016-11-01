# -*- coding: utf-8 -*-
# python2.7
"""
Created on Mon Oct 31 20:25:19 2016

@author: MagicWang
"""
import wave
from pyaudio import PyAudio, paInt16, paContinue
import time
import webbrowser
import IBM

CHUNK = 1024        #缓存块大小
FORMAT = paInt16    #采样值的量化格式 16 bit int
RATE = 8000         #采样频率
CHANNELS = 1        #声道数
RECORD_SECONDS = 5  #录音时间
save_buffer = list()

def callback_record(in_data, frame_count, time_info, status):
    """
    append data into frames
    """
    save_buffer.append(in_data)
    return (in_data, paContinue)


def record_wave(to_dir=None):
    '''to_dir:wave file dir'''
    if to_dir is None:
        to_dir = './'
    
    pa = PyAudio()
    stream = pa.open(format=FORMAT, channels=CHANNELS,
                     rate=RATE, input=True,
                     stream_callback=callback_record)

    '''阻塞式的录音'''
#    print '***Recording***'
#    for i in range(0,int(RATE / CHUNK * RECORD_SECONDS)):
#        audio_data = stream.read(CHUNK)
#        save_buffer.append(audio_data)
#    print '***Record Finished***'
    
    '''非阻塞式'''
    stream.start_stream()
    try:
        while stream.is_active():
            get = raw_input("Type '\q' or 'q' to stop:\n")
            if 'q' in get or '\q' in get:
                stream.stop_stream()
            time.sleep(0.1)
    finally:
        stream.close()
        pa.terminate()
    
    '''Use pyaudio.Stream.stop_stream() to pause playing/recording, 
        and pyaudio.Stream.close() to terminate the stream
       Finally, terminate the portaudio session using pyaudio.PyAudio.terminate()
    '''
    stream.stop_stream()
    stream.close()
    pa.terminate()
    
#    wave_name = time.strftime("%Y%m%d_%H%M", time.localtime())+'.wav'
    wave_name = 'file.wav'
    if to_dir.endswith('/'):
        wave_path = to_dir+wave_name
    else:
        wave_path = to_dir+'/'+wave_name
    ## save wave file
    wf = wave.open(wave_path, 'wb')
    wf.setnchannels(CHANNELS) 
    wf.setsampwidth(pa.get_sample_size(FORMAT)) 
    wf.setframerate(RATE) 
    wf.writeframes("".join(save_buffer)) 
    wf.close()
    ## 返回
    print wave_name+' saved'
    return wave_path

def wave2Text(wave_path):
    return IBM.speech2Text(wave_path)

def browser_open(text):
    if text is None:
        print 'There is No text'
    else:
        if text.startswith(u"谷歌") or text.startswith(u"google"):
            url = 'http://www.google.com'
            webbrowser.open_new_tab(url)
        elif text.startswith(u"博客") or text.startswith(u"blog"):
            url = 'http://blog.magicwang.tech'
            webbrowser.open_new_tab(url)
        else:
            print 'You said '+text
    
if __name__ == "__main__":
    wavePath = record_wave()
    text = wave2Text(wavePath)
    browser_open(text)