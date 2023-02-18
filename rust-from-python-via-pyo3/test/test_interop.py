import rust_from_python_via_pyo3


def test_call_into_rust():
    result = rust_from_python_via_pyo3.sum_as_string(5, 20)
    assert result == '25'