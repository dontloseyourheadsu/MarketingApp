# 🚨 Error Handling & Status Codes

## Standard Response Format

```json
{
  "success": true|false,
  "data": { /* Response payload when success is true */ },
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": { /* Optional additional error context */ }
  }
}
```

## HTTP Status Codes

- **2xx - Success**

  - 200: OK (Default success)
  - 201: Created (Resource creation)
  - 204: No Content (Successful deletion)

- **4xx - Client Errors**

  - 400: Bad Request (Invalid input, validation errors)
  - 401: Unauthorized (Missing or invalid authentication)
  - 403: Forbidden (Authenticated but insufficient permissions)
  - 404: Not Found (Resource doesn't exist)
  - 409: Conflict (Resource state conflict)
  - 422: Unprocessable Entity (Semantic validation errors)
  - 429: Too Many Requests (Rate limiting)

- **5xx - Server Errors**
  - 500: Internal Server Error (Unexpected server exception)
  - 502: Bad Gateway (Upstream service error)
  - 503: Service Unavailable (Temporary outage)

## Common Error Types

- **Validation Errors**

  ```json
  {
    "success": false,
    "error": {
      "code": "VALIDATION_ERROR",
      "message": "Invalid input parameters",
      "details": {
        "fields": {
          "email": "Must be a valid email address",
          "name": "Cannot be empty"
        }
      }
    }
  }
  ```

- **Authentication Errors**

  ```json
  {
    "success": false,
    "error": {
      "code": "UNAUTHORIZED",
      "message": "Authentication required"
    }
  }
  ```

- **Authorization Errors**
  ```json
  {
    "success": false,
    "error": {
      "code": "FORBIDDEN",
      "message": "Insufficient permissions to access this resource"
    }
  }
  ```
