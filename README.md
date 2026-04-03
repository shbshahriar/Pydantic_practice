# Pydantic Learning Project

A comprehensive learning repository for mastering **Pydantic** — a data validation and serialization library for Python that uses type hints and provides built-in support for JSON validation, error handling, and model management.

## 📚 Project Structure

### 01_basics/ — Pydantic Fundamentals
Introduction to Pydantic models and basic data validation.

- **[1.pydantic_basic.py](01_basics/1.pydantic_basic.py)** — Basic Pydantic model definition and usage
- **[2.pydantic_basic_List_Dict.py](01_basics/2.pydantic_basic_List_Dict.py)** — Working with Lists and Dictionaries in Pydantic

### 02_fields/ — Field Configuration
Advanced field configuration with annotations and metadata.

- **[3.pydantic_Field_Annoted.py](02_fields/3.pydantic_Field_Annoted.py)** — Using `Field` with `Annotated` for rich field definitions

### 03_validators/ — Validation & Computed Fields
Custom validators and computed fields for complex validation logic.

- **[4.pydantic_Field_Validator.py](03_validators/4.pydantic_Field_Validator.py)** — Field-level validators using `@field_validator`
- **[5.pydantic_Model_Validator.py](03_validators/5.pydantic_Model_Validator.py)** — Model-level validators using `@model_validator` for cross-field validation
- **[6.pydantic_Computed_Field.py](03_validators/6.pydantic_Computed_Field.py)** — Auto-calculated fields using `@computed_field`

### 04_nested_models/ — Nested Model Structures
*Coming soon* — Validation of nested and complex data structures

### 05_settings/ — Configuration Management
*Coming soon* — Using Pydantic for application settings and configuration

### 06_serialization/ — Serialization & Export
*Coming soon* — Converting models to JSON, dictionaries, and other formats

### 07_real_world/ — Real-World Examples
*Coming soon* — Practical applications and use cases

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- `uv` (UV package manager)

### Installation

1. Clone/navigate to the project:
```bash
cd pydantic_learn
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
```

3. Dependencies are already installed via `uv`. To add more packages:
```bash
uv add pydantic
```

### Running Examples

Run any Python script directly:
```bash
python 01_basics/1.pydantic_basic.py
```

Or execute from the project root:
```bash
python -m 01_basics.1_pydantic_basic
```

## 📖 Key Concepts Covered

- **Data Validation** — Type checking and constraint enforcement
- **Field Configuration** — Using `Field()` and `Annotated` for metadata
- **Field Validators** — Custom validation logic per field
- **Model Validators** — Cross-field validation and complex rules
- **Computed Fields** — Auto-calculated properties derived from other fields
- **Type Hints** — Leveraging Python's type system for better IDE support

## 🔧 Technologies

- **[Pydantic](https://docs.pydantic.dev/)** — Data validation using Python type hints
- **[UV](https://github.com/astral-sh/uv)** — Fast Python package manager
- **Python 3.9+** — Modern Python with type hints support

## 📝 Notes

Each file includes:
- Topic header with file description
- Detailed comments explaining concepts
- Working examples with actual model definitions
- Use cases and best practices

## ✨ Progress

- ✅ 01_basics — Complete (2 files)
- ✅ 02_fields — Complete (1 file)
- ✅ 03_validators — Complete (3 files)
- ⏳ 04_nested_models — Planned
- ⏳ 05_settings — Planned
- ⏳ 06_serialization — Planned
- ⏳ 07_real_world — Planned
