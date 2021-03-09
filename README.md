# ef-insights
Get insights from Engineering Fundamentals survey results

## Scripts

## generate_csv_datasets.py

Generates easy to consume csv files [overall, sections, questions] from the json survey results

```cmd
Usage: generate_csv_datasets.py [OPTIONS]

Options:
  --json_path PATH    path to input json file
  --output_path PATH  path to output csv files
  --help              Show this message and exit.
```

## generate_section_overall_sentiments.py

Generates a report with overall sentiments per engagement about a given section

```cmd
Usage: generate_section_overall_sentiment_report.py [OPTIONS]

Options:
  --section_csv PATH  path to section csv file
  --section TEXT      section to report on, e.g. Agile or Code Reviews etc.
  --help              Show this message and exit.
```

## generate_section_stats.py

Generate stats for a given section

```cmd
Usage: generate_section_stats.py [OPTIONS]

Options:
  --csv_path PATH  path to csv files
  --section TEXT   section to report on, e.g. Agile or Code Reviews etc.
  --help           Show this message and exit.
```
