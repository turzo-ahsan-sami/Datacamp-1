# Exercise_1 
json_path.write_text(json.dumps({
    "project": "Creating Robust Python Workflows",
  	# Convert the project name into snake_case
    "package": "{{ cookiecutter.project.lower().replace(' ', '_') }}",
    # Fill in the default license value
    "license": ["MIT", "BSD", "GPL3"]
}))

pprint(json.loads(json_path.read_text()))

--------------------------------------------------
# Exercise_2 
# Obtain keys from the local template's cookiecutter.json
keys = [*json.load(json_path.open())]
vals = "Your name here", "My Amazing Python Project"

# Create a cookiecutter project without prompting for input
main.cookiecutter(template_root.as_posix(), no_input=True,
                  extra_context=dict(zip(keys, vals)))

for path in pathlib.Path.cwd().glob("**"):
    print(path)

--------------------------------------------------
# Exercise_3 
zipapp.create_archive(
    # Zip up a project called "myproject"
    "myproject",                    
    interpreter="/usr/bin/env python",
    # Generate a __main__.py file
    main="mypackage.mymodule:print_name_and_file")

print(subprocess.run([".venv/bin/python", "myproject.pyz"],
                     stdout=-1).stdout.decode())

--------------------------------------------------
# Exercise_4 
def main():
    parser = argparse.ArgumentParser(description="Scikit datasets only!")
    # Set the default for the dataset argument
    parser.add_argument("dataset", nargs="?", default="diabetes")
    parser.add_argument("model", nargs="?", default="linear_model.Ridge")
    args = parser.parse_args()
    # Create a dictionary of the shell arguments
    kwargs = dict(dataset=args.dataset, model=args.model)
    return (classify(**kwargs) if args.dataset in ("digits", "iris", "wine")
            else regress(**kwargs) if args.dataset in ("boston", "diabetes")
            else print(f"{args.dataset} is not a supported dataset!"))

if __name__ == "__main__":
    main()

--------------------------------------------------
# Exercise_5 
# Read in the notebook to find the default parameter names
pprint(nbformat.read("sklearn.ipynb", as_version=4).cells[0].source)
keys = ["dataset_name", "model_type", "model_name", "hyperparameters"]
vals = ["diabetes", "ensemble", "RandomForestRegressor",
        dict(max_depth=3, n_estimators=100, random_state=0)]
parameter_dictionary = dict(zip(keys, vals))

# Execute the notebook with custom parameters
pprint(pm.execute_notebook(
    "sklearn.ipynb", "rf_diabetes.ipynb", 
    kernel_name="python3", parameters=parameter_dictionary
	))

--------------------------------------------------
# Exercise_6 
import scrapbook as sb

# Assign the scrapbook notebook object to nb
nb = sb.read_notebook("rf_diabetes.ipynb")

# Create a dataframe of scraps (recorded values)
scrap_df = nb.scrap_dataframe
print(scrap_df)

--------------------------------------------------
# Exercise_7 
import dask.dataframe as dd

# Read in a csv file using a dask.dataframe method
df = dd.read_csv("diabetes.csv")

df["bin_age"] = (df.age > 0).astype(int)

# Compute the columns means in the two age groups
print(df.groupby("bin_age").mean().compute())

--------------------------------------------------
# Exercise_8 
# Set up a Dask client with 4 threads and 1 worker
Client(processes=False, threads_per_worker=4, n_workers=1)

# Run grid search using joblib and a Dask backend
with joblib.parallel_backend("dask"):
    engrid.fit(x_train, y_train)

plot_enet(*enet_path(x_test, y_test, eps=5e-5, fit_intercept=False,
                    l1_ratio=engrid.best_params_["l1_ratio"])[:2])

--------------------------------------------------
