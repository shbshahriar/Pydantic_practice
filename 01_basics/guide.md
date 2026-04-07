# 01 — Basics: BaseModel, TypedDict, List, Dict

## Key concepts

### TypedDict vs BaseModel

| Feature | `TypedDict` | `BaseModel` |
|---|---|---|
| Runtime validation | No | Yes |
| Type checking tool | mypy / pyright | Pydantic |
| Raises errors | Never | `ValidationError` |

`TypedDict` only tells the type checker the shape of a dict. Pydantic's `BaseModel` **actually enforces** types at runtime when you create an instance.

---

## File 1 — Simple model (`1.pydantic_basic.py`)

### Pattern

```python
from pydantic import BaseModel, ValidationError

class Patient(BaseModel):
    name: str
    age: int
```

- Fields are defined as class attributes with type hints.
- Pydantic validates on instantiation — wrong type raises `ValidationError`.
- Access fields with dot notation: `patient.name`, `patient.age`.
- You can mutate fields after creation: `patient.age = 30`.

### Unpacking a dict into a model

```python
data = {"name": "John", "age": 20}
patient = Patient(**data)   # ** unpacks dict to keyword args
```

### Error handling

```python
try:
    patient = Patient(**data)
except ValidationError as e:
    print(e.errors())   # list of dicts — each describes one failed field
```

`e.errors()` returns a list like:
```python
[{"loc": ("age",), "msg": "Input should be a valid integer", "type": "int_parsing"}]
```

---

## File 2 — Complex types (`2.pydantic_basic_List_Dict.py`)

### Extra field types

```python
from typing import List, Dict

class Patient(BaseModel):
    weight:    float            # decimal number
    married:   bool             # True or False
    allergies: List[str]        # every item must be a string
    contact:   Dict[str, str]   # keys and values must both be strings
```

### Key points

- `List[str]` — Pydantic checks **every element** in the list.
- `Dict[str, str]` — Pydantic checks **every key and value** in the dict.
- `float` accepts both `70` and `70.5` (integers are coerced to float by default).
- `bool` accepts `True` / `False`.

---

## Quick recap

```
BaseModel      → runtime validated model
TypedDict      → type-checker hint only, no runtime check
List[str]      → list where each item is a string
Dict[str, str] → dict where keys and values are strings
e.errors()     → list of all validation failures with field name + reason
**dict         → unpacks dict into keyword arguments
```
