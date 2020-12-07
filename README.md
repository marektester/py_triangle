# Triangle test
Simple tests for triangle app.

How to use:
1. Create venv 
2. Install requirements 
3. Run tests > pytest -v

Results:

    test_triangle.py::test_equilateral[1-1-1] PASSED                                                                 [  7%]
    test_triangle.py::test_equilateral[9223372036854775807-9223372036854775807-9223372036854775807] PASSED           [ 14%]
    test_triangle.py::test_isosceles[2-1-2] PASSED                                                                   [ 21%]
    test_triangle.py::test_isosceles[9223372036854775807-9223372036854775807-9223372036854775797] PASSED             [ 28%]
    test_triangle.py::test_scalene[2-3-4] PASSED                                                                     [ 35%]
    test_triangle.py::test_scalene[9223372036854775797-9223372036854775802-9223372036854775807] PASSED               [ 42%]
    test_triangle.py::test_invalid[-1--2--3] PASSED                                                                  [ 50%]
    test_triangle.py::test_invalid[0-2-2] PASSED                                                                     [ 57%]
    test_triangle.py::test_invalid[4-7-16] PASSED                                                                    [ 64%]
    test_triangle.py::test_invalid[4.5-5-5.5] PASSED                                                                 [ 71%]
    test_triangle.py::test_invalid[18446744073709551614-9223372036854775807-9223372036854775807] PASSED              [ 78%]
    test_triangle.py::test_invalid[None-2-2] PASSED                                                                  [ 85%]
    test_triangle.py::test_invalid[a-b-43] PASSED                                                                    [ 92%]
    test_triangle.py::test_invalid[%-&-=] PASSED                                                                     [100%]