import uuid, re, requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwux8Xt8qZtgUav8lo3AUlfWpz-HL4OH0DhfpxkDZ1C9r3S0w22tDSL9xJXXQNU7d5nzg/exec"

def get_android_hwid():
    mac = uuid.getnode()
    return ':'.join(re.findall('..', '%012x' % mac)).upper()

class SLDDownloadDramaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.title_label = Label(text="SLD download Drama v1.0", font_size='22sp', bold=True)
        self.layout.add_widget(self.title_label)
        self.status_label = Label(text="Status: Checking License...", font_size='16sp')
        self.layout.add_widget(self.status_label)
        self.key_input = TextInput(hint_text="Enter License Key Here", multiline=False, size_hint_y=None, height=50)
        self.layout.add_widget(self.key_input)
        self.activate_btn = Button(text="Activate Key", size_hint_y=None, height=50)
        self.activate_btn.bind(on_press=self.check_license)
        self.layout.add_widget(self.activate_btn)
        return self.layout

    def check_license(self, instance):
        user_key = self.key_input.text.strip()
        if not user_key:
            self.status_label.text = "Status: Please enter a key!"
            return
        hwid = get_android_hwid()
        try:
            resp = requests.get(WEB_APP_URL, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if user_key in data:
                    key_info = data[user_key]
                    exp_date = key_info.get("expire_date", "LIFETIME")
                    saved_hwid = key_info.get("hwid", "")
                    if not saved_hwid or saved_hwid == hwid:
                        if not saved_hwid:
                            requests.get(WEB_APP_URL, params={"action": "bind_hwid", "key": user_key, "hwid": hwid}, timeout=5)
                        self.status_label.text = f"✅ Active! Exp: {exp_date}"
                    else:
                        self.status_label.text = "❌ Key used on another device!"
                else:
                    self.status_label.text = "❌ Invalid License Key!"
            else:
                self.status_label.text = "❌ Server Error!"
        except Exception as e:
            self.status_label.text = f"❌ Connection Error!"

if __name__ == '__main__':
    SLDDownloadDramaApp().run()
