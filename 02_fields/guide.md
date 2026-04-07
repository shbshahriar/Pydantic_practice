# 02 — Fields: Annotated + Field with constraints and metadata

## File 3 — `Annotated` + `Field` (`3.pydantic_Field_Annoted.py`)

## Key concepts

### Why `Annotated`?

`Annotated[type, Field(...)]` is the Pydantic V2 standard for attaching constraints and metadata to a field **inline with the type**.

```python
from typing import Annotated
from pydantic import Field

name: Annotated[str, Field(min_length=2, max_length=50)]
```

Without `Annotated` you'd have to do `name: str = Field(...)` — both work but `Annotated` is the V2 convention.

---

## Field constraints

| Constraint | Applies to | Meaning |
|---|---|---|
| `min_length` | str | minimum character count |
| `max_length` | str | maximum character count |
| `gt` | int / float | greater than (exclusive) |
| `lt` | int / float | less than (exclusive) |
| `ge` | int / float | greater than or equal |
| `le` | int / float | less than or equal |
| `default` | any | value used when field is not provided |

```python
age:    Annotated[int,   Field(gt=0, lt=120)]       # 1–119
weight: Annotated[float, Field(gt=0, lt=500)]       # any positive float under 500
name:   Annotated[str,   Field(min_length=2, max_length=50)]
```

---

## Field metadata (for docs / JSON schema)

```python
Field(
    title="Patient Name",
    description="The name of the patient",
    json_schema_extra={"example": "John Doe"}   # V2 correct — never use example= directly
)
```

- `title` / `description` appear in generated JSON schema (used by FastAPI docs).
- `json_schema_extra={"example": ...}` is the **V2 way** to provide an example — `example=` directly on `Field()` is deprecated.

---

## Special field types

```python
from pydantic import EmailStr, AnyUrl

email:    Annotated[EmailStr, Field(...)]   # validates format like user@domain.com
LinkedIn: Annotated[AnyUrl,   Field(...)]   # validates any valid URL (http/https/ftp)
```

Requires `pip install pydantic[email]` for `EmailStr`.

---

## Optional fields with defaults

```python
from typing import Optional

married: Annotated[Optional[bool], Field(default=False)]
```

- `Optional[bool]` = `bool | None` — the value can be `True`, `False`, or `None`.
- `default=False` makes the field **not required** — omitting it uses `False`.

---

## Full pattern recap

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, ValidationError
from typing import Annotated, Optional, List, Dict, Any

class Patient(BaseModel):
    name:      Annotated[str,          Field(min_length=2, max_length=50, title="...", json_schema_extra={"example": "John"})]
    age:       Annotated[int,          Field(gt=0, lt=120)]
    email:     Annotated[EmailStr,     Field(title="Email")]
    LinkedIn:  Annotated[AnyUrl,       Field(title="LinkedIn")]
    weight:    Annotated[float,        Field(gt=0, lt=500)]
    married:   Annotated[Optional[bool], Field(default=False)]
    allergies: Annotated[List[str],    Field(title="Allergies")]
    contact:   Annotated[Dict[str,str],Field(title="Contact")]

try:
    p = Patient(**data)
except ValidationError as e:
    print(e.errors())
```
