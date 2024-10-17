import argparse
import pandas as pd

def drop_notes(df):
    return df.drop(columns=['notes'])

def select_high_ratings(df):
    return df[df['rating'] >= 90]

def drop_and_one_hot_encode_red_wine(df):
    df = pd.get_dummies(df, columns=['variety'])
    return df.drop(columns=['variety_Red Wine'])

def remove_newlines_carriage_returns(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace('\n', '').str.replace('\r', '')
    return df

def convert_ratings_to_int(df):
    df['rating'] = df['rating'].astype(int)
    return df

def main():
    parser = argparse.ArgumentParser(description="DataFrame manipulation CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    subparsers.add_parser("drop_notes", help="Drop the 'notes' column from the DataFrame")
    subparsers.add_parser("select_high_ratings", help="Select rows where the 'rating' column is 90 or higher")
    subparsers.add_parser("drop_and_one_hot_encode_red_wine", help="One-hot encode 'Red Wine' and drop 'variety' column")
    subparsers.add_parser("remove_newlines_carriage_returns", help="Remove newlines and carriage returns from string columns")
    subparsers.add_parser("convert_ratings_to_int", help="Convert the 'rating' column from float to integer")
    subparsers.add_parser("run_all", help="Run all functions sequentially")

    args = parser.parse_args()

    # Load your DataFrame here
    df = pd.read_csv('train.csv')

    if args.command == "drop_notes":
        df = drop_notes(df)
    elif args.command == "select_high_ratings":
        df = select_high_ratings(df)
    elif args.command == "drop_and_one_hot_encode_red_wine":
        df = drop_and_one_hot_encode_red_wine(df)
    elif args.command == "remove_newlines_carriage_returns":
        df = remove_newlines_carriage_returns(df)
    elif args.command == "convert_ratings_to_int":
        df = convert_ratings_to_int(df)
    elif args.command == "run_all":
        df = drop_notes(df)
        df = select_high_ratings(df)
        df = drop_and_one_hot_encode_red_wine(df)
        df = remove_newlines_carriage_returns(df)
        df = convert_ratings_to_int(df)
    else:
        parser.print_help()

    # Save the transformed DataFrame
    df.to_csv('transformed_train.csv', index=False)
if __name__ == "__main__":
    main()