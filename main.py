from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class VoiceApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.status_label = Label(text="Ready (Hands-free Bluetooth)...", font_size='20sp')
        layout.add_widget(self.status_label)
        
        btn = Button(text="Speak Now", font_size='20sp', size_hint=(1, 0.3))
        btn.bind(on_press=self.start_listening)
        layout.add_widget(btn)
        
        return layout

    def start_listening(self, instance):
        self.status_label.text = "Listening via Bluetooth..."

if __name__ == '__main__':
    VoiceApp().run()
