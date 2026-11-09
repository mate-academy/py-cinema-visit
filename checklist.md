# Check Your Code Against the Following Points

1. If the function definition line is too long, place each parameter on a new line.

**Good example:**
```python
def long_function_name(
        var_one,
        var_two,
        var_three,
        var_four
) -> None:
```

**Bad example:**
```python
def long_function_name(var_one, var_two,
                       var_three,var_four) -> None:
```

2. Only use absolute imports.

**Good example:**
```python
from app.module import Component
```

**Bad example:**
```python
from .module import Component
```
