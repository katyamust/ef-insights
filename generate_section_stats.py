"""
Script to generate statistics report for a given section
This requires an overall.csv, sections.csv and questions.csv which you can generate with generate_csv_datasets.py
"""
import os
import click
import pandas as pd


@click.command()
@click.option('--csv_path', default='data', type=click.Path(), help='path to csv files')
@click.option('--section', default='Code Reviews', help='section to report on, e.g. Agile or Code Reviews etc.')
def generate_report(csv_path: str, section: str):

    overall_csv = os.path.join(csv_path, 'overall.csv')
    df_overall = pd.read_csv(overall_csv)
    num_surveys = len(df_overall)
    print(f"TOTAL SURVEYS:\t\t\t\t\t{num_surveys}\n")

    # Stats for the sections
    sections_csv = os.path.join(csv_path, 'sections.csv')
    df_sections = pd.read_csv(sections_csv)
    df_sections = df_sections[df_sections['sectionName'] == section]
    print(f"STATS FOR SECTION {section}")
    print("------------------------------------")
    print(f"SURVEYS ANSWERING THIS SECTION:\t{len(df_sections)}")
    print(f"MAX POSSIBLE SCORE:\t\t\t\t{df_sections['sectionPossibleScore'].max()}\n")
    print("NUMBER OF SURVEYS BY POSSIBLE SCORE: (This indicates how many questions they answered)")
    print("Possible\tNum Surveys")
    print("------------------------------------")
    print(df_sections['sectionPossibleScore'].value_counts())
    print()
    print(f"MAX ACTUAL SCORE:\t\t\t\t{df_sections['sectionActualScore'].max()}")
    print(f"AVG ACTUAL SCORE:\t\t\t\t{df_sections['sectionActualScore'].mean():.2f}")
    df_sections['avg_of_answered'] = df_sections['sectionActualScore'] / df_sections['sectionPossibleScore']
    print(f"AVG OF MAX FOR ANSWERED %:\t\t{df_sections['avg_of_answered'].mean() * 100:.2f}%\n")

    # stats for the individual questions
    questions_csv = os.path.join(csv_path, 'questions.csv')
    df_questions = pd.read_csv(questions_csv)
    df_questions = df_questions[df_questions['section.sectionName'] == section]

    print(f"STATS FOR INDIVIDUAL QUESTIONS")
    print("------------------------------------")
    print("ANSWERS PER QUESTION:")
    print(df_questions['questionText'].value_counts())
    print()
    for question in df_questions['questionText'].unique():
        print(question)
        print("------------------------------------")
        dfq = df_questions[df_questions['questionText'] == question]
        print(f"ANSWERED IN {len(dfq)} SURVEYS")
        print(f"MAX POSSIBLE SCORE:\t\t\t\t{dfq['questionPossibleScore'].max()}")
        print(f"AVERAGE SCORE:\t\t\t\t\t{dfq['questionActualScore'].mean():.2f}\n")


if __name__ == '__main__':
    generate_report()
