from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.graphics import Color, Rectangle
import math

class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  
        self.theme_cls.primary_palette = "DeepPurple"
        
        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.canvas.before.clear()

        self.entry_num1 = MDTextField(hint_text="Enter first number")
        self.entry_num2 = MDTextField(hint_text="Enter second number")
        self.result_label = MDLabel(text="", halign="center", theme_text_color="Secondary")
        
        buttons_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        buttons_layout.bind(minimum_height=buttons_layout.setter('height'))

        operations = ["Add", "Subtract", "Multiply", "Divide", "Log", "Percentage"]

        for operation in operations:
            button = MDRaisedButton(text=operation, on_release=self.calculate)
            buttons_layout.add_widget(button)

        layout.add_widget(self.entry_num1)
        layout.add_widget(self.entry_num2)
        layout.add_widget(self.result_label)
        layout.add_widget(buttons_layout)
        
        return layout

    def calculate(self, button):
        operation = button.text.lower().replace(" ", "_")
        num1_str = self.entry_num1.text
        num2_str = self.entry_num2.text
        
        try:
            num1 = float(num1_str)
            num2 = float(num2_str) if num2_str else None
            
            if operation == "add":
                result = num1 + (num2 or 0)
            elif operation == "subtract":
                result = num1 - (num2 or 0)
            elif operation == "multiply":
                result = num1 * (num2 or 1)
            elif operation == "divide":
                if num2 is None:
                    result = "Please enter a valid second number"
                elif num2 != 0:
                    result = num1 / num2
                else:
                    result = "Cannot divide by zero"
            elif operation == "log":
                result = math.log(num1)
            elif operation == "percentage":
                result = (num1 / num2) * 100 if num2 else "Please enter a valid second number"
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Please enter valid numbers"
        except Exception as e:
            result = f"Error: {str(e)}"
            
        self.result_label.text = str(result)

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
