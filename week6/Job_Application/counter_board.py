import pandas as pd
import os
from turtle import Turtle, Screen


class Counterboard:
    def __init__(self):
        # Create indidviual turtles for each counter
        self.job_app_turtle = Turtle()
        self.success_turtle = Turtle()
        self.reject_turtle = Turtle()
        

        # Intialise turtles
        for turtle in [self.job_app_turtle, self.success_turtle, self.reject_turtle]:
            turtle.color("black")
            turtle.penup()
            turtle.hideturtle()

        self.job_app_count = self.get_count_from_csv("week6/Job_Application/job_apps.csv")
        self.success_count = self.get_count_from_csv("week6/Job_Application/job_successes.csv")
        self.reject_count = self.get_count_from_csv("week6/Job_Application/job_rejects.csv")

        self.job_app_turtle.goto(-10, 105)
        self.success_turtle.goto(-355, -195)
        self.reject_turtle.goto(355, -195)
        
        self.update_job_app()
        self.update_success()
        self.update_reject()

    def get_count_from_csv(self, filename):
        # Read the amount of rows from a CSV file
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            return len(df)
        return 0

    def update_job_app(self):
        self.job_app_turtle.clear()
        self.job_app_turtle.write(self.job_app_count, align="center", font=("Courier", 80, "normal"))

    def update_success(self):
        self.success_turtle.clear()
        self.success_turtle.write(self.success_count, align="center", font=("Courier", 80, "normal"))

    def update_reject(self):
        self.reject_turtle.clear()
        self.reject_turtle.write(self.reject_count, align="center", font=("Courier", 80, "normal"))


    def job_app_point(self):
        self.job_app_count += 1
        # Ask user to enter in a company
        # Save answer to csv file
        company_name = self.prompt_for_company("Job Application").title()
        if company_name:
            self.save_to_csv("week6/Job_Application/job_apps.csv", {"Company": company_name})
        self.update_job_app()

    def success_point(self):
        self.success_count += 1
        company_name = self.prompt_for_company("Job Successful Application").title()
        if company_name:
            self.save_to_csv("week6/Job_Application/job_successes.csv", {"Company": company_name})
        self.update_success()
        
    def reject_point(self):
        self.reject_count += 1
        company_name = self.prompt_for_company("Job Rejection").title()
        if company_name:
            self.save_to_csv("week6/Job_Application/job_rejects.csv", {"Company": company_name})
        self.update_reject()

    def prompt_for_company(self, category):
        # Display a textbox asking for company name
        screen = Screen()
        return screen.textinput(title=f"{category} Entry", prompt="Enter a Company Name: ")
    
    def save_to_csv(self, filename, data):
        df = pd.DataFrame([data])
        df.to_csv(filename, mode='a', header=not os.path.exists(filename), index = False)


    