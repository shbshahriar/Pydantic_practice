# 03 — Validators: field_validator, model_validator, computed_field

Three tools for custom logic on top of Pydantic's built-in type/constraint checks.

---

## File 4 — `@field_validator` (`4.pydantic_Field_Validator.py`)

### What it does
Runs **custom Python logic** on a single field, after Pydantic's built-in checks.

### Pattern

```python
from pydantic import field_validator

@field_validator('email', mode="after")
@classmethod
def validate_email(cls, value):
    if not value.endswith('@example.com'):
        raise ValueError('Email must be from the domain example.com')
    return value   # always return the value on success
```

### Rules
- Must be `@classmethod` — Pydantic calls it on the class, not an instance.
- `mode="after"` — runs **after** the built-in type check (e.g. after `EmailStr` confirms valid format).
- `mode="before"` — runs **before** type coercion (less common).
- Raise `ValueError` to fail — the message becomes the error detail.
- **Always `return value`** at the end.
- Multiple validators can target different fields independently.

### `strict=True` on a field

```python
age: Annotated[int, Field(strict=True, gt=0, lt=120)]
```

With `strict=True`, Pydantic **refuses type coercion** — passing `"20"` (str) for an int field raises an error instead of silently converting it.

---

## File 5 — `@model_validator` (`5.pydantic_Model_Validator.py`)

### What it does
Runs validation on the **entire model** after all individual fields are validated. Used when a rule involves **two or more fields together**.

### Pattern

```python
from pydantic import model_validator
from typing_extensions import Self

@model_validator(mode="after")
@classmethod
def validate_emergency_contact(cls, model):
    # Cross-field rule: age + contact checked together
    if model.age > 60 and "emergency_contact" not in model.contact:
        raise ValueError('Emergency contact required for patients over 60')
    return model   # always return the model on success
```

### Key differences from `field_validator`

| | `field_validator` | `model_validator` |
|---|---|---|
| Targets | one field | entire model |
| Has access to | `value` (that field only) | `model` (all fields) |
| Use case | single-field custom rule | cross-field rule |
| Runs | after its field passes | after ALL fields pass |

---

## File 6 — `@computed_field` (`6.pydantic_Computed_Field.py`)

### What it does
Defines a field whose value is **automatically calculated** from other fields. Never passed in by the user.

### Pattern

```python
from pydantic import computed_field

@computed_field
@property
def bmi(self) -> float:         # return type annotation is required
    bmi = self.weight / ((self.height / 100) ** 2)
    return round(bmi, 2)
```

### Rules
- Requires `@property` — makes it accessible as `patient.bmi` not `patient.bmi()`.
- Return type annotation (`-> float`) is **required** by Pydantic.
- The value is derived at model creation — it stays consistent with the input fields.
- It appears in `model_dump()` and `model_dump_json()` output automatically.
- You **cannot** pass `bmi` as input — it is always computed.

---

## Execution order

When you call `Patient(**data)`, Pydantic runs in this order:

```
1. Type checks (is age an int?)
2. Field constraints (is age > 0 and < 120?)
3. @field_validator (custom per-field logic)
4. @model_validator (cross-field logic on the whole model)
5. @computed_field (derived fields calculated last)
```

All errors from steps 1–4 are **collected** before raising a single `ValidationError`.

---

## Quick recap

```python
@field_validator('field_name', mode="after")   # single field custom rule
@classmethod
def my_validator(cls, value):
    ...
    return value

@model_validator(mode="after")                 # cross-field rule
@classmethod
def my_model_validator(cls, model):
    ...
    return model

@computed_field                                 # auto-calculated field
@property
def derived_field(self) -> float:
    return ...
```
