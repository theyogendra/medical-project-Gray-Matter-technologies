# Security

- This product handles medical records. **No real patient data** in the repo, issues, PRs or screenshots.
  Use fake names and fake files only.
- Secrets live in your local `.env` (never committed) and in GitHub Actions secrets.
- Every query must filter by `company_id` — one company must never see another company's data.
- Found a security problem? Tell Yogendra privately, not in a public issue.
