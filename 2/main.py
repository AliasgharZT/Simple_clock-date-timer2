    
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ObjectProperty
import datetime
import time
from kivy.clock import Clock

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    timer=ObjectProperty()
    dates=ObjectProperty()
    clocks=ObjectProperty()
    actived=ObjectProperty()
    _start_stop=ObjectProperty()
    _reset_register=ObjectProperty()
    _actived=True
    sec=0
    min=0
    h=0

    def _reset(self):
        self.timer.text='00:00:00'
        self.sec=0
        self.min=0
        self.h=0
        self._pause()
    def _start(self,*args):
        self.sec+=1
        if self.sec==59:
            self.sec=0
            if self.min==59:
                self.min=0
                self.h+=1
            self.min+=1

        self.timer.text=str(self.h)+':'+str(self.min)+':'+str(self.sec)
    def active_start(self):
        Clock.schedule_interval(self._start,0.98) 
    def _pause(self):
        Clock.unschedule(self._start) 
# ////////////////////////////////////////////////
    def _start_stop_(self):
        if self._start_stop.text=='start':
            self._start_stop.text='pause'
            self._start_stop.md_bg_color='red'
            self.active_start()
            self._reset_register.text='register'
            self._reset_register.md_bg_color='gray'
        else:
            self._start_stop.text='start'
            self._start_stop.md_bg_color='blue'
            self._pause()
            self._reset_register.text='reset'
            self._reset_register.md_bg_color='red'
    def _reset_register_(self):
        if self._reset_register.text=='reset':
            self._reset()
            self._reset_register.md_bg_color='blue'
        else:
            pass 
# ///////<<<date>>>////////////<<<clock>>>//////////////
    def _dates(self,*args):
        self.dates.text=str(datetime.date.today())
    def _clocks(self,*args):
        q=time.localtime()
        qq=str(q.tm_hour)+':'+str(q.tm_min)+':'+str(q.tm_sec)
        self.clocks.text=qq
    def active_clock(self):
        Clock.schedule_interval(self._clocks,1)
    def turn_on__turn_off(self):
        if self._actived==True:
            self.actived.text='turn_off\nDate-clock'
            self.actived.md_bg_color='red'
            self._actived=False
            # /////////////////////
            Clock.schedule_interval(self._dates,1)
            self.active_clock()
            Clock.unschedule(self._dates)
        else:
            self.actived.text='Active\nDate-clock'
            self.actived.md_bg_color='green'
            self._actived=True
            # /////////////////
            self.dates.text='0000:00:00'
            Clock.unschedule(self._clocks)
            self.clocks.text='00:00:00'


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        return Style()

MainApp().run()

