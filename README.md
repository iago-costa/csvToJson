### Comandos usados

```shell
# install dependencies
conda create --name py310 python=3.10

# Environmental
conda activate py310

```

```python
# Perform tests
python -m unittest discover -s ./src -p "*_test.py"

python -m unittest src.handle_test.TestHandle
python -m unittest src.handle_test.TestHandle.test_get_list
python -m unittest src.handle_test.TestHandle.test_read_csv
python -m unittest src.handle_test.TestHandle.test_save_csv
python -m unittest src.handle_test.TestHandle.test_line_by_line

```

### Pre-Commit Commands

```shell
# Environmental
conda activate py310

# install dependencies
pip install pre-commit

# install pre-Commit
pre-commit install

# install pre-Commit for commit-msg
pre-commit install --hook-type commit-msg

# install pre-Commit for prepare-commit-msg
pre-commit install --hook-type prepare-commit-msg

# install pre-Commit for pre-push

# run pre-Commit
pre-commit run --all-files

# Run pre-Commit with debug
pre-commit run --all-files --verbose --show-diff-on-failure

# Run pre-Commit with debug and without cache
pre-commit run --all-files --verbose --show-diff-on-failure --no-cache

```

### Create pull request with hooks

```shell
pre-commit run create-pull-request
```
