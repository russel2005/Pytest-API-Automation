# Pytest

### Naming convention
- Name all the test classes start with Test 
- Name all the test modules with test_.py 
- Name all the test functions with test_():
### [Marker](#marker)
```
import pytest
@pytest.mark.smoke
def test_api1():
```
### [Test Discovery](#Test)
- run all test
  ``` > pytest ```
- run all test in folder
  ``` > pytest folder/folder```
- run test with specific name
  ``` > pytest -k api01```
- run test single file/ module
  ``` > pytest -k folder/test_module1.py```
- run test single test/funciton
  ``` > pytest -k folder/test_module1.py::api1```
- run test with marker
  ``` > pytest -m smoke```


