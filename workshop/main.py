import pandas as pd


def drop_notes(df):
    """
    Drop the 'notes' column from the DataFrame.
    """
    if 'notes' in df.columns:
        df = df.drop(columns=['notes'])
    return df


def select_high_ratings(df):
    """
    Select only rows where the 'rating' column is 90 or higher.
    """
    if 'rating' in df.columns:
        df = df[df['rating'] >= 90]
    return df


def drop_and_one_hot_encode_red_wine(df):
    """
    Create a 'Red_Wine' column that is 1 if 'variety' is 'Red Wine' and 0 otherwise.
    Drop the original 'variety' column.
    """
    if 'variety' in df.columns:
        df['Red_Wine'] = (df['variety'] == 'Red Wine').astype(int)
        df = df.drop(columns=['variety'])
    return df


def remove_newlines_carriage_returns(df):
    """
    Remove newlines and carriage returns from all string columns in the DataFrame.
    """
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace('\n', ' ').str.replace('\r', ' ')
    return df


def convert_ratings_to_int(df):
    """
    Convert the 'rating' column from float to integer.
    """
    if 'rating' in df.columns:
        df['rating'] = df['rating'].astype(int)
    return df

# Example usage
if __name__ == "__main__":
    df = pd.read_csv('train.csv')
    df = drop_notes(df)
    df = select_high_ratings(df)
    df = drop_and_one_hot_encode_red_wine(df)
    df = remove_newlines_carriage_returns(df)
    df = convert_ratings_to_int(df)
    df.to_csv('transformed_train.csv', index=False)