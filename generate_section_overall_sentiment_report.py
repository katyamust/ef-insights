"""
Script to generate report of overall sentiments for a given section
This requires a sections.csv which you can generate with generate_csv_datasets.py
"""
import click
import pandas as pd


@click.command()
@click.option('--section_csv', default='data/sections.csv', type=click.Path(), help='path to section csv file')
@click.option('--section', default='Code Reviews', help='section to report on, e.g. Agile or Code Reviews etc.')
def generate_report(section_csv: str, section: str):
    df_sections = pd.read_csv(section_csv)
    df_sections = df_sections[df_sections['sectionName'] == section]
    df_sections.sort_values(by='engagementId', inplace=True)

    prev_engagement_id = 0
    for index, row in df_sections.iterrows():
        if row['engagementId'] != prev_engagement_id:
            prev_engagement_id = row['engagementId']
            print()
            print(row['engagementName'])
            print('----------------------------')
        print(f"Possible score: {row['sectionPossibleScore']}, Actual score: {row['sectionActualScore']}, Date: {row['dateTaken'][:10]}")
        if pd.notnull(row['overallSentiment']):
            print(row['overallSentiment'])
        else:
            print("NO OVERALL STATEMENT")


if __name__ == '__main__':
    generate_report()
