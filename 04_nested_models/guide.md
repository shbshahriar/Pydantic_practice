# 04 — Nested Models: composing models inside other models

## File 7 — Nested Models (`7.pydantic_Nested_Models.py`)

## Key concept

A Pydantic model can use **another Pydantic model as a field type**. Pydantic validates the nested model recursively — errors inside it include the full path to the failing field.

---

## Pattern

### Define the inner model

```python
class Address(BaseModel):
    street:   Annotated[str, Field(min_length=1)]
    city:     Annotated[str, Field(min_length=1)]
    zip_code: Annotated[str, Field(min_length=5, max_length=10)]
```

### Use it as a field in the outer model

```python
class Patient(BaseModel):
    name:    Annotated[str, Field(...)]
    # ... other fields ...
    address: Address    # no Annotated needed — the type itself is the validation
```

### Provide nested data as a plain dict

```python
data = {
    "name": "John Doe",
    # ...
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip_code": "12345"
    }
}

patient = Patient(**data)
```

Pydantic automatically converts the `address` dict into an `Address` instance.

---

## Accessing nested fields

```python
patient.address           # Address instance
patient.address.street    # "123 Main St"
patient.address.city      # "Anytown"
patient.address.zip_code  # "12345"
```

---

## Nested error paths

If a nested field fails, `e.errors()` shows the full path:

```python
[
    {
        "loc": ("address", "zip_code"),   # path to the failing field
        "msg": "String should have at least 5 characters",
        "type": "string_too_short"
    }
]
```

The `loc` tuple traces through each level: `("address", "zip_code")` means `patient.address.zip_code`.

---

## Why use nested models?

- **Reusability** — `Address` can be used in `Patient`, `Doctor`, `Hospital`, etc.
- **Clarity** — groups related fields together logically.
- **Recursive validation** — constraints on inner fields are enforced automatically.
- **Clean access** — `patient.address.city` is clearer than `patient.contact["city"]`.

---

## Quick recap

```
Inner model     → normal BaseModel with its own fields and constraints
Outer model     → uses inner model as a field type (address: Address)
Input           → pass nested data as a plain dict — Pydantic converts it
Access          → patient.address.city (dot notation through levels)
Error path      → loc: ("address", "zip_code") — full path shown in e.errors()
```
