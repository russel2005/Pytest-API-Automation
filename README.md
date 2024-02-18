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
  ``` > pytest -v folder/folder```
- run test single file/ module
  ``` > pytest -v folder/test_module1.py```
- run test single test/function
  ``` > pytest -v folder/test_module1.py::test_api1```
- run set of test based on function name
  ``` > pytest -v -k api01
      > pytest -v -k "api01 and api02"
  ```
- run test with marker for group test, test can have multiples marker
  ``` > pytest -v -m smoke```
- run test but check the collection of test before run
  ``` > pytest -v --collect-only -k "api01"```
- exit test when it failed during run
  ``` > pytest -v --exitfirst```
- exit test when it failed multiple number of test
  ``` > pytest -v --maxfail=3```
- print something in cmd during test
  ``` > pytest -v -s```
