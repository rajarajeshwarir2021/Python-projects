from flask import Flask, render_template, request
from flask.views import MethodView
from flatmates_bill.flat import Bill, Flatmate
from wtforms import Form, StringField, SubmitField

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", billform=bill_form)

    def post(self):
        bill_form = BillForm(request.form)

        the_bill = Bill(float(bill_form.bill_amount.data), bill_form.bill_period.data)
        print(bill_form.days_in_house1.data)
        print(float(bill_form.days_in_house1.data))
        flatmate_1 = Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
        flatmate_2 = Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))

        flatmate_1_share = flatmate_1.pays(the_bill, flatmate_2)
        flatmate_2_share = flatmate_2.pays(the_bill, flatmate_1)

        return render_template("bill_form_page.html", billform=bill_form, result= True, name1=flatmate_1.name, name2=flatmate_2.name, amount1=flatmate_1_share, amount2=flatmate_2_share)


class ResultsPage(MethodView):

    def get(self):
        bill_form = BillForm(request.form)

        the_bill = Bill(float(bill_form.bill_amount.data), bill_form.bill_period.data)
        print(bill_form.days_in_house1.data)
        print(float(bill_form.days_in_house1.data))
        flatmate_1 = Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
        flatmate_2 = Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))

        flatmate_1_share = flatmate_1.pays(the_bill, flatmate_2)
        flatmate_2_share = flatmate_2.pays(the_bill, flatmate_1)

        return render_template("results.html", name1=flatmate_1.name, name2=flatmate_2.name, amount1=flatmate_1_share, amount2=flatmate_2_share)


class BillForm(Form):
    bill_amount = StringField("Bill Amount: ", default="100")
    bill_period = StringField("Bill Period: ", default="December 2020")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the House: ")

    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the House: ")

    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill_form", view_func=BillFormPage.as_view("bill_form_page"))
#app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"), methods=["GET"])


#if __name__ == '__main__':
app.run(debug=True)