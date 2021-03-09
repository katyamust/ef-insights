"""
Script to generate datasets based on the EF assessment raw json output in csv formats that are easier to consume.
"""
import os
import json
import click
import logging
import pandas as pd


@click.command()
@click.option('--json_path', default="data/ef-assessment-raw-data-03-01-21.json", type=click.Path(), help="path to input json file")
@click.option('--output_path', default="data", type=click.Path(), help="path to output csv files")
def generate_csv_files(json_path: str, output_path: str):
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)

    # save the overall survey data for each survey
    df_overall = pd.json_normalize(data)
    df_overall.drop(['responseId', 'sections'], axis=1, inplace=True)
    overall_csv_path = os.path.join(output_path, 'overall.csv')
    df_overall.to_csv(overall_csv_path, index=False)
    logging.info(f"Saving the overall survey data to {overall_csv_path} with the columns {df_overall.columns}")

    # save the sections survey data
    df_sections = pd.json_normalize(data=data, record_path='sections', meta=['engagementId', 'engagementName', 'dateTaken'])
    df_sections.drop(['questions'], axis=1, inplace=True)
    sections_csv_path = os.path.join(output_path, 'sections.csv')
    df_sections.to_csv(sections_csv_path, index=False)
    logging.info(f"Saving the sections survey data to {sections_csv_path} with the columns {df_sections.columns}")

    # save the questions survey data
    df_questions = pd.json_normalize(data=data, record_path=['sections', 'questions'], meta=['engagementId', 'dateTaken', ['section', 'sectionName']])
    questions_csv_path = os.path.join(output_path, 'questions.csv')
    df_questions.to_csv(questions_csv_path, index=False)
    logging.info(f"Saving the questions survey data to {questions_csv_path} with the columns {df_questions.columns}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generate_csv_files()
