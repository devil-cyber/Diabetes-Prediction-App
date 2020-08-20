from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from text_input_helper import p_helper, g_helper, bmi_helper, age_helper, dp_helper, bp_helper, i_helper, st_helper, \
    label_helper
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from model import MlModel
from kivymd.uix.dialog import MDDialog
import numpy as np

Window.size = (366, 600)


class Diabetes(MDApp):
    def build(self):
        screen = MDScreen()
        label = Builder.load_string(label_helper)
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.theme_style = "Dark"
        self.Pregnancies = Builder.load_string(p_helper)
        self.Glucose = Builder.load_string(g_helper)
        self.BloodPressure = Builder.load_string(bp_helper)
        self.SkinThickness = Builder.load_string(st_helper)
        self.Insulin = Builder.load_string(i_helper)
        self.BMI = Builder.load_string(bmi_helper)
        self.DiabetesPedigreeFunction = Builder.load_string(dp_helper)
        self.Age = Builder.load_string(age_helper)
        button = MDRectangleFlatButton(text='Submit', pos_hint={'center_x': .5, 'center_y': .04}, on_release=self.model)
        screen.add_widget(label)
        screen.add_widget(self.Pregnancies)
        screen.add_widget(self.Glucose)
        screen.add_widget(self.BloodPressure)
        screen.add_widget(self.SkinThickness)
        screen.add_widget(self.Insulin)
        screen.add_widget(self.BMI)
        screen.add_widget(self.DiabetesPedigreeFunction)
        screen.add_widget(self.Age)
        screen.add_widget(button)
        return screen

    def model(self, obj):
        try:
            pr = float(self.Pregnancies.text)
            gl = float(self.Glucose.text)
            bp = float(self.BloodPressure.text)
            st = float(self.SkinThickness.text)
            i = float(self.Insulin.text)
            bmi = float(self.BMI.text)
            dp = float(self.DiabetesPedigreeFunction.text)
            age = float(self.Age.text)
            m = MlModel(pr, gl, bp, st, i, bmi, dp, age)
            value = m.predict()
            if value == 0:
                check_string = 'You have no any sign of Diabetes'
            else:
                check_string = 'Consult to doctor you have sign of Diabetes'
        except Exception as e:
            check_string=str(e) + ' ' + 'or try to provide numeric value and provide value for each component listed'
        close_button = MDRectangleFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title='Result', text=check_string, size_hint=(.7, 1),
                               buttons=[close_button])
        self.dialog.open()


    def close_dialog(self, obj):
        self.dialog.dismiss()


Diabetes().run()
