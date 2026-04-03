# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- **Python**: 3.13+
- **Package manager**: `uv`
- **Dependency**: `pydantic[email]>=2.12.5` (Pydantic V2)

## Commands

```bash
# Activate virtual environment (Windows)
.venv\Scripts\Activate.ps1

# Run any learning script
python 01_basics/1.pydantic_basic.py

# Add a new package
uv add <package-name>
```

## Project Structure

Each numbered file builds on the previous one, following a single `Patient` model throughout:

| Folder | Concept |
|---|---|
| `01_basics/` | `BaseModel`, `TypedDict`, `List`, `Dict` |
| `02_fields/` | `Annotated` + `Field` with constraints and metadata |
| `03_validators/` | `@field_validator`, `@model_validator`, `@computed_field` |
| `04_nested_models/` | Composing models (e.g. `Address` inside `Patient`) |
| `05_serialization/` | `model_dump()`, `model_dump_json()`, `include`/`exclude` |
| `06_settings/` | Planned — Pydantic settings management |
| `07_real_world/` | Planned — real-world use cases |

## Conventions

- **Pydantic V2 only** — always use `json_schema_extra={"example": ...}` inside `Field()`, never `example=` directly (deprecated in V2)
- **`Annotated[type, Field(...)]`** is the standard pattern for all fields with constraints
- Every file wraps model instantiation in `try/except ValidationError` and prints `e.errors()` on failure
- `strict=True` on `age` fields — no type coercion allowed
- All files have a top comment block with `FILE:` and `TOPIC:` for orientation
