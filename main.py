from kivy.app import App
from kivy.uix.label import Label

class HumanitiesApp(App):
    def build(self):
        return Label(text="مرحباً بك في تطبيق الدراسات الإنسانية المغربية", font_size='20sp')

if __name__ == '__main__':
    HumanitiesApp().run()
  
