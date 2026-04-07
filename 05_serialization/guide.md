# 05 — Serialization: model_dump() and model_dump_json()

## File 8 — Serialization (`8.pydantic_Serialization.py`)

## Key concept

Serialization = converting a Pydantic model **out** of a Python object into a dict or JSON string, so you can send it over an API, save it, log it, etc.

---

## The two methods

| Method | Returns | Use case |
|---|---|---|
| `model_dump()` | `dict` | Pass to other Python code, further processing |
| `model_dump_json()` | `str` (JSON) | Send over HTTP, write to file, log |

```python
patient.model_dump()       # → Python dict
patient.model_dump_json()  # → JSON string
```

---

## `include` — only serialize specific fields

```python
# Only include these top-level fields
patient.model_dump(include={"name", "age", "email"})

# Include specific nested fields (exclude address.city)
patient.model_dump(include={"address": {"street", "zip_code"}})
```

The value for a nested key is a **set of field names** to include from that nested model.

---

## `exclude` — serialize everything except specific fields

```python
# Exclude these fields, keep everything else
patient.model_dump(exclude={"age", "email", "LinkedIn"})
```

---

## Combining with nested models

```python
# Full dump — nested Address model is included as a nested dict automatically
patient.model_dump()
# → {"name": "John", ..., "address": {"street": "...", "city": "...", "zip_code": "..."}}

# Selective nested dump
patient.model_dump(include={"address": {"street", "zip_code"}})
# → {"address": {"street": "123 Main St", "zip_code": "12345"}}
```

---

## Type check

```python
type(patient.model_dump())       # <class 'dict'>
type(patient.model_dump_json())  # <class 'str'>
```

---

## Common pattern: validate then serialize

```python
try:
    patient = Patient(**data)
except ValidationError as e:
    print(e.errors())
    raise SystemExit(1)   # stop — no point serializing invalid data

# Only reaches here if validation passed
result = patient.model_dump()
json_result = patient.model_dump_json()
```

---

## Quick recap

```
model_dump()              → Python dict (all fields)
model_dump_json()         → JSON string (all fields)
include={"a", "b"}        → only those fields
exclude={"a", "b"}        → everything except those fields
include={"nested": {"x"}} → specific fields from a nested model
```
