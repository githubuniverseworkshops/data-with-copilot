<h1 align="center">Data + GitHub Copilot for advanced data solutions</h1>
<em align="center">The perfect pairing ™</em>

## Intro

This repository contains the source code for the complete workshop. You will follow the step-by-step guide below, completing all the steps while working with data and GitHub Copilot within Codespaces.

> [!NOTE]
> This repo is intended to give an introduction to various **GitHub Copilot** features, such as **Copilot Chat** and **inline chat**. Hence the step-by-step guides below contain the general description of what needs to be done, and Copilot Chat or inline chat can support you in generating the necessary commands.
>
> Each step (where applicable) also contains a `Cheatsheet` which can be used to validate the Copilot suggestion(s) against the correct command.
>
> 💡 Play around with different prompts and see how it affects the accuracy of the GitHub Copilot suggestions. For example, when using inline chat, you can use an additional prompt to refine the response without having to rewrite the whole prompt.

## Data Project features

In this workshop, you will be working with data from a CSV file included in this repository, as well as a Python script file that will interact with the CSV file. Here are some features of the project you will work with:

1. Consume a CSV dataset and perform transformations
1. Identify and implement validations
1. Create a command-line tool that can be used in CI/CD environments

## Preparation

This repository is Codespaces-ready and is pre-configured so that you have all dependencies installed including the Visual Studio Code extensions necessary to work with GitHub Copilot and Python:

- GitHub Copilot
- Python extension
- Pre-installed Python dependencies with an activated Virtual Environment

> [!NOTE]
> If using this repository in your account or a non-GitHub-Universe organization, you might incur in charges or consumption of your free quoota for Codespaces.

### 1. Create a new repository from this template

Progress: [🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪] 1/12 (8%)

⏳ **~2min**

- Click `Use this template` :point_right: `Create a new repository`
- Set the owner to the GitHub Workshop organization: `githubuniverseworkshop`
- Give it a name
- Set visibility to `Private`
- Click `Create repository`

### 2. Create a Codespace using the provided template

Progress: [🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪] 2/12 (16%)

⏳ **~3min**

- In the newly created repo, click `Code` :point_right: `Codespaces` :point_right: `[ellipsis menu]` :point_right: `New with options` :point_right: _Ensure that `Dev container configuration` is set to `Default project configuration`_ :point_right: `Create codespace`
- ❗If you're having problems launching the Codespace then you can also clone the repo and continue from here in your IDE:

    ```sh
    git clone https://github.com/<YOUR_NAME_SPACE>/<YOUR_REPO_NAME>.git
    cd <YOUR_REPO_NAME>
    ```

    > [!NOTE]
    > There is no need to push changes back to the repo during the workshop

### 3. Verify Python is installed and set correctly

Progress: [🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪] 3/12 (25%)

⏳ **~2min**

- Use the command palette to toggle the terminal (search for "Create new terminal")
- Run `which python` and make sure it points to the Virtual Environment (`home/vscode/venv/bin/python`)
- Run `which pip` and ensure that it also points to the Virtual Environment (`home/vscode/venv/bin/pip`)

### 4. Run the Python scripts

Progress: [🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪] 4/12 (33%)

⏳ **~2min**

- Run the `main.py` script and confirm no errors occur:

    ```shell
    python main.py
    ```

- Run the `check.py` script and confirm no errors occur:

    ```shell
    python check.py
    ```

    There should be some OK and some FAIL lines:

    ```shell
    [OK  ]   verify_drop_notes
    [FAIL]   verify_high_ratings - Not all ratings are 90 or higher.
    [FAIL]   verify_one_hot_encoding - The 'Red Wine' column was not one-hot encoded correctly.
    [OK  ]   verify_remove_newlines_carriage_returns
    [FAIL]   verify_ratings_to_int - The 'ratings' column was not converted to integers correctly.
    ```

### 5. Open relevant files

Progress: [🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪] 5/12 (41%)

⏳ **~2min**

GitHub Copilot benefits from having context. One way to enhance context is by opening relevant files.

- Open the `main.py`, `check.py`, `train.csv`, and `transformed_train.csv` files

## Development

### 1. See how much you can learn about the project and the data

Progress: [🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪] 6/12 (50%) - Half way through!

⏳ **~5min**

- Open GitHub Copilot Chat
- Use the `@workspace` agent to ask Copilot what the `main.py` and `check.py` files are doing
- Again, with the `@workspace` agent, ask Copilot what is the nature of the data you are going to work with

#### 2. Fix the high ratings function

Progress: [🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪] 7/12 (58%)

⏳ **~3min**

- In `main.py` find the `select_high_ratings()` function
- Insert your cursor in the function signature or body somewhere
- Open inline chat with `Ctrl-i` or `Cmd-i` (on Mac)
- Prefix your prompt with the `/explain` slash command
- Ask why this function might not be working and implement any potential fixes
- Re-generate `transformed_train.csv` by running `python main.py`
- Verify the fix by running `python check.py` with this function returning an `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
/explain why this function might not be working correctly?
```

##### Expected output

```sh
Based on the provided code, there are a few potential reasons why the `select_high_ratings` function might not be working correctly:

1. Typo in Column Name: The function checks if the column name 'ratings' exists in the DataFrame `df.columns` If there is a typo in the column name, such as 'rating' instead of 'ratings', the condition `if 'ratings' in df.columns`

```

</details>

> [!NOTE]
> Feel free to use the GitHub Copilot Chat to implement or corroborate the fix

#### 3. Fix the one-hot encoding problem

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪] 8/12 (66%)

⏳ **~3min**

- Select the `drop_and_one_hot_encode_red_wine()` function and open inline chat (Ctrl-i/ Cmd-i)
- Use the `/fix` slash command to ask GitHub Copilot to suggest a potential fix
- Re-generate `transformed_train.csv` by running `python main.py`
- Verify the fix by running `python check.py` with this function returning an `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
This function is not doing one-hot encoding on the variety column
```

##### Expected output

```python
def drop_and_one_hot_encode_red_wine(df):
    """
    Create a 'Red_Wine' column that is 1 if 'variety' is 'Red Wine' and 0 otherwise.
    Drop the original 'variety' column.
    """
    if 'variety' in df.columns:
        df['Red_Wine'] = df['variety'].apply(lambda x: 1 if x == 'Red Wine' else 0)
        df = df.drop(columns=['variety'])
    return df
```

</details>

#### 4. Fix the ratings conversion to int

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪] 9/12 (75%)

⏳ **~3min**

- If your `verify_ratings_to_int` check is already "OK", then Copilot may have already fixed this issue for you. If not, continue with the following steps.
- Select the `convert_ratings_to_int()` function and open inline chat (Ctrl-i / Cmd-i)
- Use the `/explain` slash command to ask GitHub Copilot why this function might not be working correctly
- Identify the problem and implement the fix
- Re-generate `transformed_train.csv` by running `python main.py`
- Verify the fix by running `python check.py` with this function returning an `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
This function is not converting the ratings to integers
```

##### Expected output

```python
def convert_ratings_to_int(df):
    """
    Convert the 'rating' column from float to integer.
    """
    if 'rating' in df.columns:
        df['rating'] = df['rating'].to_int()
    return df
```

</details>

## Testing

A robust Python project can benefit from testing. You will add some unit tests and find more on how to run these tests with the help of GitHub Copilot.

Make sure you have the terminal open by running the command palette and typing `toggle terminal`

### 1. Test your CLI

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪] 10/12 (83%)

⏳ **~5min**

- This project has the Pytest test runner and framework pre-installed, make sure it is available by running `pytest --version`
- Run the tests while in the `workshop` directory by using the following command: `pytest -v`

The output should give you a failure.

#### 2. Fix the failing test

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪] 11/12 (91%)

⏳ **~5min**

- Select the output in the terminal and paste it into GitHub Copilot Chat, prefixing with a request for a fix and an explanation
- Use the output from the chat to implement a fix in `test_main.py`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
Fix the test and explain your fix:
// Copy and paste the output from the terminal here
```

##### Expected output

The error occurs because the drop_notes function is likely modifying the DataFrame in place, rather than returning a new DataFrame with the 'notes' column dropped. To fix the test, we need to ensure that the drop_notes function returns a new DataFrame without the 'notes' column and then check the columns of this new DataFrame.

Here is the corrected test function:

```python
def test_drop_notes_column_dropped():
    # Create a sample DataFrame with 'notes' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'notes': ['note1', 'note2', 'note3']})

    # Call the drop_notes function and get the result
    result = main.drop_notes(df)
    
    # Assert that 'notes' column in result dataframe is dropped
    columns = result.columns.to_list()
    assert columns == ['A', 'B']
```

By storing the result of the drop_notes function in a new variable and checking its columns, we ensure that the test correctly verifies the behavior of the function.

</details>

#### 3. Add tests for the one hot encoding function

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) - 🎉 Celebrate!

⏳ **~5min**

- Ensure that the `python check.py` has all OK output, otherwise this step might not work.
- Select the `drop_and_one_hot_encode_red_wine` function in `main.py`
- Open inline chat with `Ctrl-i`/`Cmd-i`
- Use the `/tests` slash command to get suggestions on tests
- Review the output, accept it, and verify with the `pytest -v` command. All tests should be passing, and you should have more tests than before. Sometimes Copilot will indent the suggested tests incorrectly (nesting them inside an existing test function), so make sure the tests are correctly indented before running them.

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
/tests
```

##### Expected output

```python
def test_drop_and_one_hot_encode_red_wine_red_wine_column_created():
    # Create a sample DataFrame with 'variety' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Call the drop_and_one_hot_encode_red_wine function
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Assert that 'Red_Wine_Red Wine' column is created
    assert 'Red_Wine_Red Wine' in result.columns

def test_drop_and_one_hot_encode_red_wine_red_wine_column_encoded():
    # Create a sample DataFrame with 'variety' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Call the drop_and_one_hot_encode_red_wine function
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Assert that 'Red_Wine_Red Wine' column is encoded correctly
    assert result['Red_Wine_Red Wine'].tolist() == [1, 0, 1]

def test_drop_and_one_hot_encode_red_wine_variety_column_dropped():
    # Create a sample DataFrame with 'variety' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Call the drop_and_one_hot_encode_red_wine function
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Assert that 'variety' column is dropped
    assert 'variety' not in result.columns

def test_drop_and_one_hot_encode_red_wine_dataframe_unchanged():
    # Create a sample DataFrame with 'variety' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Call the drop_and_one_hot_encode_red_wine function
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Assert that the shape of the DataFrame is unchanged
    assert result.shape == (3, 3)

    # Assert that the original DataFrame is not modified
    assert 'variety' in df.columns
    assert df.shape == (3, 3)
```

</details>

## Bonus

There are a couple of bonus challenges if you've completed all the tasks and your scripts are in good shape.

### Bonus Challenge 1 - Create a robust CLI tool

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) 🎉  
Optional: [🚀 Turbo Boost! (1/2) 50%]  

- Use GitHub Copilot chat with the `@workspace` prefix to convert the project into a CLI with options and a help menu
- Ensure that the prompt specifies no external dependencies and it should only use the standard library

<details>
<summary>Cheatsheet</summary>

#### Prompt

```shell
@workspace I want to convert this project into a CLI with a help menu. Help me do this without using any dependencies, just pure Python standard library
```

#### Expected output

```python
def main():
    parser = argparse.ArgumentParser(description="DataFrame manipulation CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("drop_notes", help="Drop the 'notes' column from the DataFrame")
    subparsers.add_parser("select_high_ratings", help="Select rows where the 'rating' column is 90 or higher")
    subparsers.add_parser("drop_and_one_hot_encode_red_wine", help="One-hot encode 'Red Wine' and drop 'variety' column")
    subparsers.add_parser("remove_newlines_carriage_returns", help="Remove newlines and carriage returns from string columns")
    subparsers.add_parser("convert_ratings_to_int", help="Convert the 'rating' column from float to integer")

    args = parser.parse_args()

    # Load your DataFrame here
    df = pd.read_csv('workshop/train.csv')

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
    else:
        parser.print_help()

    # Save the transformed DataFrame
    df.to_csv('workshop/transformed_train.csv', index=False)

if __name__ == "__main__":
    main()
```

</details>

### Bonus Challenge 2 - Document your project

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) 🎉  
Optional: [🚀 Turbo Boost! (1/2) 50%]  
Optional: [🌟 Extra Points! (2/2) 100% 🏆]

- Create a new `docs/` folder and a file called `README.md`
- Use GitHub Copilot chat with the `@workspace` prefix to get started documenting your project using Markdown in a README.md
- In your prompt, ask for help documenting the project goals, the nature of the data in the CSV files, and how the CLI works.

<details>
<summary>Cheatsheet</summary>

#### Prompt

```shell
@workspace help me create a good README.md file in Markdown so that I can document this and help others understand how it works and the nature of the data
```

#### Expected output

```markdown
# DataFrame Manipulation CLI

This project provides a command-line interface (CLI) for manipulating a DataFrame using various operations. The CLI is built using the Python standard library and does not require any external dependencies.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
- [Data](#data)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Set up a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r workshop/requirements.txt
    ```

## Usage

To use the CLI, navigate to the `workshop` directory and run the `main.py` script with the desired command.

### Commands

- `drop_notes`: Drop the 'notes' column from the DataFrame.
- `select_high_ratings`: Select rows where the 'rating' column is 90 or higher.
- `drop_and_one_hot_encode_red_wine`: One-hot encode 'Red Wine' and drop the 'variety' column.
- `remove_newlines_carriage_returns`: Remove newlines and carriage returns from string columns.
- `convert_ratings_to_int`: Convert the 'rating' column from float to integer.

### Examples

1. Drop the 'notes' column:
    ```sh
    python main.py drop_notes
    ```

2. Select rows with high ratings:
    ```sh
    python main.py select_high_ratings
    ```

3. One-hot encode 'Red Wine' and drop 'variety' column:
    ```sh
    python main.py drop_and_one_hot_encode_red_wine
    ```

4. Remove newlines and carriage returns from string columns:
    ```sh
    python main.py remove_newlines_carriage_returns
    ```

5. Convert 'rating' column to integer:
    ```sh
    python main.py convert_ratings_to_int
    ```

## Data

The data used in this project is stored in CSV files located in the `workshop` directory. The primary file is `train.csv`, which contains the following columns:

- `notes`: Text notes about the data.
- `ratings`: Numeric ratings for the data.
- `variety`: The variety of the data (e.g., 'Red Wine').

The transformed data is saved to `transformed_train.csv` after applying the CLI commands.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
```

</details>

## Clean-up

### 1. Delete your Codespace

⏳ **~1min**

Before deleting, if you wish, you can push your changes. Remember workshop repositories are temporary too.

Go to [https://github.com/codespaces](https://github.com/codespaces) and find your current running Codespace and delete it.
