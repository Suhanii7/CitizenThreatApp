from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle  # Add this import for Color
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase
cred = credentials.Certificate(r"C:\Users\hp\OneDrive\Documents\VSCode\CitizenThreatApp\firebase-key.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Reference to the Firestore collection for storing reports
reports_ref = db.collection("threat_reports")

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Label(text="Citizen Threat Reporting", font_size=24))

        report_button = Button(text="Report Threat", size_hint=(1, 0.2), background_color=(0.2, 0.6, 1, 1))
        report_button.bind(on_press=self.open_report_screen)
        self.add_widget(report_button)

        view_button = Button(text="View Reports", size_hint=(1, 0.2), background_color=(0.1, 0.8, 0.5, 1))
        view_button.bind(on_press=self.open_view_screen)
        self.add_widget(view_button)

    def open_report_screen(self, instance):
        self.clear_widgets()
        self.add_widget(ReportThreatScreen())

    def open_view_screen(self, instance):
        self.clear_widgets()
        self.add_widget(ViewReportsScreen())


class ReportThreatScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Label(text="Describe the Threat:", font_size=18))
        self.description_input = TextInput(hint_text="Enter threat details", multiline=True)
        self.add_widget(self.description_input)

        self.add_widget(Label(text="Enter Location:", font_size=18))
        self.location_input = TextInput(hint_text="Enter location details", multiline=True)
        self.add_widget(self.location_input)

        submit_button = Button(text="Submit", size_hint=(1, 0.2), background_color=(0.3, 0.8, 0.2, 1))
        submit_button.bind(on_press=self.submit_report)
        self.add_widget(submit_button)

        back_button = Button(text="Back", size_hint=(1, 0.2), background_color=(1, 0.2, 0.2, 1))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

    def submit_report(self, instance):
        description = self.description_input.text
        location = self.location_input.text
        if description and location:
            # Get current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Add report to Firestore with time, description, and location
            reports_ref.add({
                "description": description,
                "location": location,
                "time": current_time  # Ensure time is being added
            })
            self.description_input.text = "Report Submitted!"  # Feedback to the user
            self.location_input.text = ""

    def go_back(self, instance):
        self.clear_widgets()
        self.add_widget(HomeScreen())


class ViewReportsScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Label(text="Submitted Reports", font_size=24, bold=True, size_hint=(1, 0.1)))

        self.scroll_view = ScrollView(size_hint=(1, 0.8))
        self.report_list = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=10)
        self.report_list.bind(minimum_height=self.report_list.setter("height"))
        self.scroll_view.add_widget(self.report_list)
        self.add_widget(self.scroll_view)

        back_button = Button(text="Back", size_hint=(1, 0.1), background_color=(1, 0.2, 0.2, 1))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        self.load_reports()

    def load_reports(self):
        # Fetch reports from Firestore and display them, sorted by time
        reports = [doc.to_dict() for doc in reports_ref.stream()]
        sorted_reports = sorted(reports, key=lambda x: x.get("time", "1900-01-01 00:00:00"), reverse=True)  # Default value for missing 'time'

        for report in sorted_reports:
            report_card = BoxLayout(orientation="vertical", size_hint_y=None, height=150, padding=10, spacing=5)

            # Use .get() to avoid KeyError if 'description' or 'location' is missing
            description = report.get("description", "No description provided")
            location = report.get("location", "No location provided")
            time = report.get("time", "Not Provided")

            report_card.add_widget(Label(text=f"Description: {description}", font_size=16, size_hint_y=None, halign="left"))
            report_card.add_widget(Label(text=f"Location: {location}", font_size=14, size_hint_y=None, halign="left"))
            report_card.add_widget(Label(text=f"Time: {time}", font_size=14, size_hint_y=None, halign="left"))

            separator = Widget(size_hint_y=None, height=2)
            separator.canvas.add(Color(0.8, 0.8, 0.8, 1))  # Color is now imported
            separator.canvas.add(Rectangle(size=(self.width, 2)))
            report_card.add_widget(separator)

            self.report_list.add_widget(report_card)

    def go_back(self, instance):
        self.clear_widgets()
        self.add_widget(HomeScreen())



class CitizenThreatApp(App):
    def build(self):
        return HomeScreen()


if __name__ == "__main__":
    CitizenThreatApp().run()
