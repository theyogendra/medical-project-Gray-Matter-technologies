# Database Design

## Database strategy

A single PostgreSQL database is used for the complete application. The schema intentionally centers on shared identity, authorisation, scheduling, patient, clinical, and financial data.

## Core models

- User
- RefreshToken
- AuditLog
- Appointment
- MedicalRecord
- Invoice

## Key design choices

- One-to-many relationship between users and refresh tokens.
- Optional user association in audit logs.
- Patient and doctor relations in appointments and medical records.
- Decimal fields for financial values.
- Indexes on high-lookup fields such as email, patient ID, and appointment times.

## Migration and schema management

The Prisma schema is the source of truth for database structure. Migrations are generated and applied through Prisma CLI commands in the backend workspace.

## Deletion and archival policies

- User deletion cascades refresh tokens.
- Audit logs retain history even when a user is removed.
- Appointments and invoices are kept intentionally separate from user deletion to preserve operational traceability.
- Financial records should eventually be archived instead of hard-deleted for compliance-oriented scenarios.
