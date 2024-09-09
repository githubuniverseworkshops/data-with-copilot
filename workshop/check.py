import pandas as pd


def verify_drop_notes(df):
    """
    Verify that the 'notes' column has been dropped.
    """
    return 'notes' not in df.columns

def verify_high_ratings(df):
    """
    Verify that all ratings are 90 or higher.
    """
    if 'ratings' in df.columns:
        return df['ratings'].min() >= 90
    return False

def verify_one_hot_encoding(df):
    """
    Verify that the 'Red_Wine' column has been one-hot encoded.
    """
    return 'Red_Wine' in df.columns and df['Red_Wine'].isin([0, 1]).all()

def verify_remove_newlines_carriage_returns(df):
    """
    Verify that there are no newlines or carriage returns in string columns.
    """
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].str.contains('\n').any() or df[col].str.contains('\r').any():
            return False
    return True

def verify_ratings_to_int(df):
    """
    Verify that the 'ratings' column has been converted to integers.
    """
    if 'ratings' in df.columns:
        return pd.api.types.is_integer_dtype(df['ratings'])
    return False

# Example usage
if __name__ == "__main__":
    df = pd.read_csv('transformed_train.csv')
    functions = [
        [verify_drop_notes, "The 'notes' column was not dropped correctly."],
        [verify_high_ratings, "Not all ratings are 90 or higher."],
        [verify_one_hot_encoding, "The 'Red Wine' column was not one-hot encoded correctly."],
        [verify_remove_newlines_carriage_returns, "Newlines or carriage returns were not removed correctly."],
        [verify_ratings_to_int, "The 'ratings' column was not converted to integers correctly."]
    ]
     
    for func, message in functions:
        if func(df):
            print(f"[OK  ]\t {str(func.__name__)}")
        else:
            print(f"[FAIL]\t {str(func.__name__)} - {message}")
