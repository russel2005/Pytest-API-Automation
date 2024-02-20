# Pytest

### Naming convention
- Name all the test classes start with Test 
- Name all the test modules with test_.py 
- Name all the test functions with test_():
### [Fixtures](#fixtures)
That are run by pytest before the actual test fuctions. Ex Setup DB Connection, or initialize webDriver. Can put fixtures in test files or, in conftest.py for making fixtures available in multiple test files. it use as an argument in the test function. fixture called from test function.

### [Marker](#marker)
```
import pytest
@pytest.mark.smoke
def test_api1():
```
- Markers running supports: and, or, not, parentheses operators.
-- • E.g. ```pytest -m "sanity and uitest"```
- Can define markers in module/file level:
-- • ```pytestmark=[pytest.mark.smoke, pytest.mark.sanity]```
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

### find all application content-type : [Visit](https://stackoverflow.com/questions/23714383/what-are-all-the-possible-values-for-http-content-type-header)
 
