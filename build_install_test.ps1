# python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel

# pip install dist/pyRawDataReader_zwf-0.0.1-py3-none-any.whl
pip install dist/pyRawDataReader_zwf-0.0.1-py3-none-any.whl --upgrade

Write-Host "Testing RawFileReader.py"
python tests/test_RawFileReader.py E:\DIAData\PECAN\20mz\20141010_DIA_20x20mz_500to900.raw

Write-Host "Test WiffFileReader.py"
python tests/test_WiffFileReader.py E:\DIAData\LFQBench\DIA\HYE110_TTOF6600_32fix_lgillet_I160308_001.wiff

# upload into pypi
# python -m pip install --user --upgrade twine
# python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*