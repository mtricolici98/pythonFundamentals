import pandas
import pandas as pd
from pandas import DataFrame


def students_without_score(original_df):
    print(original_df[original_df['score'].isna()].to_string())


def score_between(original_df):
    _min = float(input('Min Score:'))
    _max = float(input('Max Score:'))
    print(original_df[original_df['score'].between(_min, _max)].to_string())


def scroe_sorted(original_df):
    print(original_df.sort_values('score').to_string())


def name_sorted(original_df):
    print(original_df.sort_values('name').to_string())


def add_new_record(original_df):
    name = input("New record name ?")
    score = float(input("New record score"))
    attempts = int(input("New record attempts number"))
    qualified = input('Qualified (y/n)').lower() == 'y'
    row = dict(name=name, score=score, attempts=attempts, qualify=qualified)
    # Making new dataframe from this dict, so we can combine them
    new_df = pd.concat([original_df, pandas.DataFrame([row])], ignore_index=True)
    print(new_df.to_string())
    return new_df


def remove_by_id(original_df):
    print(original_df.to_string())
    index = int(input('Index to remove: '))
    removed_df = original_df.drop(index)
    print(removed_df.to_string())
    return removed_df


def save_qualified(original_df):
    original_df[original_df['qualify'] == 'yes'][['name', 'score']].to_excel('qualified_studs.xlsx')


if __name__ == '__main__':
    # Requires package openpyxl
    original_df = pd.read_excel('homework.xlsx', engine='openpyxl')
    ex_map = {
        1: students_without_score,
        2: score_between,
        3: scroe_sorted,
        4: name_sorted,
        5: add_new_record,
        6: remove_by_id,
        7: save_qualified,
    }
    while True:
        print('Select what you want to see:')
        print('1: List students with no score')
        print('2: Select student with scroe between a and b')
        print('3: Show list sorted by score')
        print('4: Show list sorted by name')
        print('5: Add new record')
        print('6: Remove record')
        print('7: Save all qualified')
        print('0: Exit()')
        choice = int(input('Choice?: '))
        if choice == 0:
            break
        result = ex_map[choice](original_df)
        if result:
            if isinstance(result, DataFrame):
                original_df = result
            else:
                print(result)  # Single result, print it instead
