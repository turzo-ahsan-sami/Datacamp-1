# Exercise_1 
def argparse_cli(func: Callable) -> None:
    # Instantiate the parser object
    parser = argparse.ArgumentParser()
    # Add an argument called in_files to the parser object
    parser.add_argument("in_files", nargs="*")
    args = parser.parse_args()
    print(func(args.in_files))

if __name__ == "__main__":
    argparse_cli(nbuild)

--------------------------------------------------
# Exercise_2 
# Add the section title in the docstring below
"""Usage: docopt_cli.py [IN_FILES...]"""

def docopt_cli(func: Callable) -> None:
    # Assign the shell arguments to "args"
    args = docopt(__doc__)
    print(func(args["IN_FILES"]))

if __name__ == "__main__":
    docopt_cli(nbuild)

--------------------------------------------------
# Exercise_3 
# Initialize a new repo in the current folder
repo = git.Repo.init()

# Obtain a list of untracked files
untracked = repo.untracked_files

# Add all untracked files to the index
repo.index.add(untracked)

# Commit newly added files to version control history
repo.index.commit(f"Added {', '.join(untracked)}")
print(repo.head.commit.message)

--------------------------------------------------
# Exercise_4 
changed_files = [file.b_path
                 # Iterate over items in the diff object
                 for file in repo.index.diff(None)
                 # Include only modified files
                 .iter_change_type("M")]

repo.index.add(changed_files)
repo.index.commit(f"Modified {', '.join(changed_files)}")
for number, commit in enumerate(repo.iter_commits()):
    print(number, commit.message)

--------------------------------------------------
# Exercise_5 
# Create an virtual environment
venv.create(".venv")

# Run pip list and obtain a CompletedProcess instance
cp = subprocess.run([".venv/bin/python", "-m", "pip", "list"], stdout=-1)

for line in cp.stdout.decode().split("\n"):
    if "pandas" in line:
        print(line)

--------------------------------------------------
# Exercise_6 
print(run(
    # Install project dependencies
    [".venv/bin/python", "-m", "pip", "install", "-r", "requirements.txt"],
    stdout=-1
).stdout.decode())

print(run(
    # Show information on the aardvark package
    [".venv/bin/python", "-m", "pip", "show", "aardvark"], stdout=-1
).stdout.decode())

--------------------------------------------------
# Exercise_7 
pd.DataFrame(
    np.c_[(diabetes.data, diabetes.target)],
    columns="age sex bmi map tc ldl hdl tch ltg glu target".split()
    # Pickle the diabetes dataframe with zip compression
    ).to_pickle("diabetes.pkl.zip")
                  
# Unpickle the diabetes dataframe
df = pd.read_pickle("diabetes.pkl.zip")
df.plot.scatter(x="ltg", y="target", c="age", colormap="viridis")
plt.show()

--------------------------------------------------
# Exercise_8 
# Train and pickle a linear model
joblib.dump(LinearRegression().fit(x_train, y_train), "linear.pkl")

# Unpickle the linear model
linear = joblib.load("linear.pkl")
predictions = linear.predict(x_test)
plt.scatter(y_test, predictions, edgecolors=(0, 0, 0))
min_max = [y_test.min(), y_test.max()]
plt.plot(min_max, min_max, "--", lw=3)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.show()

--------------------------------------------------
