


### Comandos usados

```shell
# instalar dependencias
conda create --name py310 python=3.10

# ativar ambiente
conda activate py310



```

```python
# Executar testes
python -m unittest discover -s . -p "*_test.py"

python -m unittest handle_test.TestHandle
python -m unittest handle_test.TestHandle.test_get_list
python -m unittest handle_test.TestHandle.test_read_csv
python -m unittest handle_test.TestHandle.test_save_csv
python -m unittest handle_test.TestHandle.test_line_by_line

```
Co-authored-by new test teste
