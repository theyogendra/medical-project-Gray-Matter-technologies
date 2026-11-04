# How we work (Git + GitHub)

## Branches

| Branch | What it holds | Who can push |
| --- | --- | --- |
| `main` | Only modules Yogendra has signed off. Tagged at each sign-off (`E0-signed-off`, …). | Nobody directly — PR from `develop` |
| `develop` | Everyone's merged work. Yogendra tests here. | Nobody directly — PRs only |
| `E<n>/<story-id>-<short-name>` | One task from the sheet, e.g. `E1/E1-01-case-from-web-form` | The module owner |
| `fix/E<n>-<issue>-<short-name>` | A bug fix, e.g. `fix/E0-42-grace-banner` | The module owner |

## Every task, step by step

```bash
git checkout develop
git pull origin develop                         # 1. start from the latest code
git checkout -b E1/E1-01-case-from-web-form     # 2. one branch per sheet task
# 3. code ONLY inside your module folders, run the app and `pytest`
git add backend/app/modules/e1_case_core frontend/lib/features/e1_case_core
git commit -m "E1-01: create case from public web form"   # 4. Story ID first
git pull origin develop                         # 5. bring in others' work, fix conflicts
git push -u origin E1/E1-01-case-from-web-form  # 6. push
```

7. On GitHub: **Compare & pull request** → base `develop` → fill the template → **Create**.
8. Fix review comments on the same branch; the PR updates itself.
9. After the merge, mark the task **Done** in your sheet tab and start again from step 1.

Push at least once a day. Not finished? Open the PR as a **Draft**.

## Rules

1. Never push to `main` or `develop` directly.
2. One sheet task = one branch = one PR. Keep it small (under ~400 changed lines).
3. Change only your own module folders. Need something in `core/`, `shared/` or someone else's module?
   Open an issue and tag the owner.
4. Need data from another module? Call its `service.py` functions — never query its tables yourself.
5. Every table holds `company_id` and every query filters by it (`TenantMixin` + `get_company_id`).
6. Never commit `.env`, passwords, keys, or real patient files. Fake data only.
7. Stuck on a merge conflict for 30 minutes? Ask Yogendra. Never `git push --force` on shared branches.

## Testing and sign-off

- Each "Done when" in the sheet should become at least one test in your module's `tests/` folder.
- Yogendra files bugs as GitHub Issues (bug template, labels `bug` + module code). Fix them on a `fix/…`
  branch and write `Fixes #<issue number>` in the PR.
- On the module's sign-off day Yogendra merges `develop` into `main` and tags it.
