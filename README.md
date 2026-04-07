# Pydantic Learning Project

A learning repository for mastering **Pydantic V2** — runtime data validation and serialization using Python type hints.

## Project Structure

### 01_basics/ — Pydantic Fundamentals

- **[1.pydantic_basic.py](01_basics/1.pydantic_basic.py)** — `BaseModel`, `TypedDict`, field access, `ValidationError`
- **[2.pydantic_basic_List_Dict.py](01_basics/2.pydantic_basic_List_Dict.py)** — `List[str]`, `Dict[str, str]`, `float`, `bool`
- **[guide.md](01_basics/guide.md)** — recap

### 02_fields/ — Field Configuration

- **[3.pydantic_Field_Annoted.py](02_fields/3.pydantic_Field_Annoted.py)** — `Annotated + Field`, constraints (`gt`, `lt`, `min_length`), `EmailStr`, `AnyUrl`, `Optional`, `json_schema_extra`
- **[guide.md](02_fields/guide.md)** — recap

### 03_validators/ — Validators & Computed Fields

- **[4.pydantic_Field_Validator.py](03_validators/4.pydantic_Field_Validator.py)** — `@field_validator`, `strict=True`
- **[5.pydantic_Model_Validator.py](03_validators/5.pydantic_Model_Validator.py)** — `@model_validator`, cross-field rules
- **[6.pydantic_Computed_Field.py](03_validators/6.pydantic_Computed_Field.py)** — `@computed_field`, auto-calculated BMI
- **[guide.md](03_validators/guide.md)** — recap

### 04_nested_models/ — Nested Models

- **[7.pydantic_Nested_Models.py](04_nested_models/7.pydantic_Nested_Models.py)** — composing models, recursive validation, nested error paths
- **[guide.md](04_nested_models/guide.md)** — recap

### 05_serialization/ — Serialization

- **[8.pydantic_Serialization.py](05_serialization/8.pydantic_Serialization.py)** — `model_dump()`, `model_dump_json()`, `include`, `exclude`
- **[guide.md](05_serialization/guide.md)** — recap

## Getting Started

```bash
# Activate virtual environment (Windows)
.venv\Scripts\Activate.ps1

# Run any script
python 01_basics/1.pydantic_basic.py

# Add a package
uv add <package-name>
```

## Key Concepts Covered

- `BaseModel` — runtime validated model
- `Annotated + Field` — constraints and metadata inline with the type
- `@field_validator` — custom logic on a single field
- `@model_validator` — cross-field validation
- `@computed_field` — auto-derived fields
- Nested models — recursive validation
- Serialization — `model_dump()` / `model_dump_json()` with `include` / `exclude`
