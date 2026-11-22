# Data Dictionary — Medical Appointment No Shows

## Source

| Item | Detail |
|---|---|
| Dataset | Medical Appointment No Shows (Kaggle, uploaded by Joni Hoppen) |
| Expected file | `KaggleV2-May-2016.csv` |
| Location in project | `data/raw/` (not committed to Git) |
| Origin | Public medical appointments in Vitória, Espírito Santo, Brazil |
| Time period | Appointments from roughly April–June 2016 |
| Expected size | About 110,527 rows and 14 columns |
| License | Listed on Kaggle as CC BY-NC-SA 4.0 — confirm on the dataset page before download |

> **Status:** The dataset has not been downloaded yet. Everything below is the
> *expected* structure, based on the public dataset description. Each item should be
> checked against the real file during Milestone 2 (data ingestion and cleaning).

## Columns

Original column names are kept exactly as they appear in the file, including the
original spelling mistakes. The "Planned name" column shows the cleaned
`snake_case` name we expect to use after cleaning.

| Original column | Planned name | Expected raw type | Planned type | Meaning |
|---|---|---|---|---|
| `PatientId` | `patient_id` | float (shown in scientific notation) | string | Anonymized patient identifier. One patient can have many appointments. |
| `AppointmentID` | `appointment_id` | integer | integer | Unique identifier for each appointment. |
| `Gender` | `gender` | string (`F` / `M`) | category | Recorded gender of the patient. |
| `ScheduledDay` | `scheduled_datetime` | string (ISO datetime, e.g. `2016-04-29T18:38:08Z`) | datetime | Date and time the appointment was booked. |
| `AppointmentDay` | `appointment_date` | string (ISO datetime) | date | Date of the appointment itself. |
| `Age` | `age` | integer | integer | Patient age in years. |
| `Neighbourhood` | `neighbourhood` | string | category | Neighbourhood where the appointment takes place (about 80 values). |
| `Scholarship` | `scholarship` | integer (0/1) | boolean | 1 if the patient is enrolled in *Bolsa Família*, a Brazilian social welfare program. |
| `Hipertension` | `hypertension` | integer (0/1) | boolean | 1 if the patient has a recorded hypertension condition. |
| `Diabetes` | `diabetes` | integer (0/1) | boolean | 1 if the patient has a recorded diabetes condition. |
| `Alcoholism` | `alcoholism` | integer (0/1) | boolean | 1 if the patient has a recorded alcoholism condition. |
| `Handcap` | `handicap_count` | integer (0–4) | integer | Number of recorded disabilities. Not a simple yes/no flag. |
| `SMS_received` | `sms_received` | integer (0/1) | boolean | 1 if the patient was sent at least one SMS reminder. |
| `No-show` | `no_show` | string (`Yes` / `No`) | integer (0/1) | **Target variable** — see below. |

### Planned derived features (created during cleaning, not in the raw file)

| Feature | Definition |
|---|---|
| `lead_time_days` | Days between `scheduled_datetime` and `appointment_date`. |
| `appointment_weekday` | Day of the week of the appointment. |
| `prior_no_show_count` | Number of earlier no-shows for the same patient (must only use *past* appointments to avoid leaking future information). |

## Target variable

- **Column:** `No-show`
- **Meaning:** `Yes` means the patient **did not attend** the appointment.
  `No` means the patient **attended**.
- **Planned encoding:** `no_show = 1` for missed, `0` for attended.
- **Expected class balance:** About 20% of appointments are no-shows. The classes
  are imbalanced, so accuracy alone is a misleading metric. Recall, precision, and
  ROC-AUC will also be reported.

The wording is easy to misread ("No-show = No" means they showed up), so the
encoding will be covered by an automated test.

## Expected data-quality issues

| Issue | Columns | Planned handling |
|---|---|---|
| Misspelled column names (`Hipertension`, `Handcap`, `Neighbourhood` spelling varies by region) | several | Rename during cleaning; keep a mapping in code. |
| Hyphen in column name (`No-show`) | `No-show` | Rename to `no_show`. |
| Patient IDs stored as floats, which can lose precision or display as `2.98e+13` | `PatientId` | Read as string or convert to integer then string. |
| Invalid ages (at least one negative value, e.g. `-1`) | `Age` | Remove or flag rows with age < 0. |
| Very high ages (above 100) | `Age` | Keep but review; possible but rare. |
| Many age-0 rows | `Age` | Likely infants; keep, but note in limitations. |
| Appointment time is always `00:00:00` (only the date is known) | `AppointmentDay` | Treat as a date only. Same-day lead time = 0. |
| Some appointments scheduled *after* the appointment date (negative lead time) | `ScheduledDay`, `AppointmentDay` | Flag and remove; these are likely data-entry errors. |
| `Handcap` has values 0–4, not just 0/1 | `Handcap` | Keep as a count; optionally add a 0/1 flag. |
| Same patient appears many times | `PatientId` | Split train/test by patient to avoid the model memorizing individuals. |
| Short time window (about 3 months, one city) | all | Document as a limitation; results may not generalize. |
| Possible duplicate appointment records | `AppointmentID` | Check uniqueness during ingestion. |
| Missing values | all | None are expected, but this will be verified. |

## Ethical and privacy note

- **Anonymized public data.** The dataset is publicly available on Kaggle and
  uses anonymized patient identifiers. It has no names, addresses, contact details,
  or other direct identifiers. We will not try to re-identify any individual or
  link this data to other sources.
- **Educational purpose only.** ConnectToCare is a student portfolio project. It is
  not a clinical tool and must not be used to make decisions about real patients.
- **Decision support, not decisions.** Any risk score is meant to help a coordinator
  prioritize supportive outreach (such as a reminder call). It must never be used
  to deny, delay, or overbook care for a patient.
- **Sensitive attributes.** Columns such as gender, age, neighbourhood, welfare
  enrollment (`Scholarship`), health conditions, and disability count can act as
  stand-ins for socioeconomic status or protected characteristics. Model results
  will be checked across these groups for unequal error rates, and any concerns
  will be documented.
- **No medical advice.** The project does not diagnose conditions or recommend
  treatments. The health-condition columns are used only as recorded attributes.
- **Data handling.** The raw file stays in `data/raw/` and is excluded from Git.
  Only code, documentation, and small summary outputs are committed.
