import json
import sys

with open('ef-assessment-raw-data-03-01-21.json') as f:
  all_projects = json.load(f)

with open('code_reviews_insights.md',"w") as f1:
    original_stdout = sys.stdout # Save a reference to the original standard output
    sys.stdout = f1 # Change the standard output to the file we created.

    for project in all_projects:
        print("## " + project["engagementName"])
        print(" ")
        for section in project["sections"]:
            if section["sectionName"] ==  "Code Reviews":
                print(section["overallSentiment"])
                for question in section["questions"]:
                    if question["questionAnswer"] is not None:
                        print(question["questionText"])
                        print(question["questionAnswer"])

    sys.stdout = original_stdout