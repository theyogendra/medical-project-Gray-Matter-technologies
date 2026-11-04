# API conventions

- URLs: `/api/<module code>/<things>` — e.g. `/api/e1/cases`, `/api/e1/cases/7`
- Plural nouns, lowercase, words joined with `-` (`/api/e4/review-requests`)
- JSON fields in `snake_case`; dates as `YYYY-MM-DD`, timestamps as ISO 8601
- `GET` list -> 200 + array · `GET` one -> 200 or 404 · `POST` -> 201 + the created item
- Bad input -> 422 (Pydantic does this for you) · Not yours / not found -> 404 (never reveal another company's data)
- Every endpoint takes `company_id: int = Depends(get_company_id)`
- Every endpoint has a docstring — it appears on http://localhost:8000/docs
