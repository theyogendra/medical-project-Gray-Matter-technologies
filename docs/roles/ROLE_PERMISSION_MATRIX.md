# Role Permission Matrix

| Role | Login | Dashboard | Patient Management | Appointments | Clinical Records | Billing | Admin Settings |
|---|---:|---:|---:|---:|---:|---:|---:|
| Admin | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Doctor | Yes | Yes | View/Edit assigned records | Yes | Yes | No | No |
| Nurse | Yes | Yes | View assigned records | Yes | Yes | No | No |
| Receptionist | Yes | Yes | Limited | Yes | No | Yes | No |
| Patient | Yes | Limited | Limited self access | Limited | Limited | Limited | No |

## Notes

The matrix is intentionally a foundation. Detailed role-based permissions should be finalized from the original workbook before feature implementation.
