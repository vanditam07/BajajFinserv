## README.md

# Lab Report Extraction API

This project provides a scalable and accurate solution to process lab report images and extract all lab test names, their corresponding values, and reference ranges. The extracted data is returned in a structured JSON format through a FastAPI service.

---

## Features

- **Image Upload:** Accepts lab report images as input.
- **OCR Processing:** Uses OCR to extract text from images.
- **Lab Test Extraction:** Identifies test names, values, reference ranges, and units.
- **Out-of-Range Detection:** Flags tests that are outside the normal reference range.
- **REST API:** Exposes a `/get-lab-tests` POST endpoint for integration.

---

## Example JSON Response

```json
{
  "is_success": true,
  "data": [
    {
      "test_name": "HB ESTIMATION",
      "test_value": "9.4",
      "bio_reference_range": "12.0-15.0",
      "test_unit": "g/dL",
      "lab_test_out_of_range": false
    },
    {
      "test_name": "PCV (PACKED CELL VOLUME)",
      "test_value": "48.7",
      "bio_reference_range": "36.0-46.0",
      "test_unit": "%",
      "lab_test_out_of_range": true
    }
  ]
}
```

---

## API Usage

### Endpoint

```
POST /get-lab-tests
```

### Request

- **Content-Type:** `multipart/form-data`
- **Body:** Image file (e.g., `.jpg`, `.png`) with key `file`

#### Example (using `curl`):

```bash
curl -X POST "https://your-api-url/get-lab-tests" \
  -H "accept: application/json" \
  -F "file=@/path/to/lab_report.jpg"
```

---

## Response

- **is_success**: Boolean indicating if the extraction was successful.
- **data**: List of lab test objects, each containing:
  - `test_name`
  - `test_value`
  - `bio_reference_range`
  - `test_unit`
  - `lab_test_out_of_range`

---

## Setup & Deployment

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```
4. **Deploy** to your preferred cloud platform (Render, Heroku, AWS, etc.)

---

## Notes

- Ensure your deployed API endpoint is accessible for evaluation.
- For more details, refer to the source code and documentation in the repository.

---

## Contact

For queries, contact: [vm1139@srmist.edu.in](mailto:vm1139@srmist.edu.in)

Citations:
[1] https://pplx-res.cloudinary.com/image/private/user_uploads/JyFejhKsZOvrMtX/image.jpg

---
