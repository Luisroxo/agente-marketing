# Marketing Agent API Documentation

## Overview

A API do Agente Marketing fornece endpoints para processamento de dados, análise e geração de relatórios de marketing.

## Base URL
- **Development**: `http://localhost:8501` (Streamlit)
- **Future API**: `http://localhost:3001/api` (Planejado)

## Current Implementation (Streamlit)

### Data Upload
O sistema atualmente suporta upload através da interface Streamlit:
- **CSV Files**: Upload direto via file uploader
- **Excel Files**: Suporte a múltiplas planilhas
- **Google Sheets**: Integração via API

### Data Processing Endpoints

#### Process CSV Data
```python
# Via Streamlit interface
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = data_processor.process_csv(uploaded_file)
```

#### Google Sheets Integration
```python
# Via Google Sheets API
sheet_data = google_sheets_api.get_data(spreadsheet_id, range_name)
processed_data = data_processor.clean_data(sheet_data)
```

## Future API Specification

### Authentication
```
Authorization: Bearer <jwt_token>
```

### Response Format
All API responses will follow this structure:
```json
{
  "success": true,
  "data": {},
  "message": "Success message",
  "timestamp": "2025-09-22T00:00:00Z"
}
```

### Planned Endpoints

#### Data Management
- `POST /api/data/upload` - Upload CSV/Excel files
- `GET /api/data/sheets/{id}` - Get Google Sheets data
- `PUT /api/data/process` - Process uploaded data
- `DELETE /api/data/{id}` - Delete dataset

#### Analysis
- `POST /api/analysis/basic` - Run basic statistical analysis
- `POST /api/analysis/personas` - Generate customer personas
- `POST /api/analysis/insights` - Generate marketing insights

#### Reports
- `GET /api/reports/{id}` - Get generated report
- `POST /api/reports/generate` - Generate new report
- `GET /api/reports/export/{id}` - Export report (PDF/DOCX)

### Error Handling
Error responses include:
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {}
  },
  "timestamp": "2025-09-22T00:00:00Z"
}
```

## Data Models

### Dataset
```json
{
  "id": "string",
  "name": "string",
  "source": "csv|excel|google_sheets",
  "rows": "number",
  "columns": "number",
  "created_at": "datetime",
  "processed": "boolean"
}
```

### Analysis Result
```json
{
  "id": "string",
  "dataset_id": "string",
  "type": "basic|personas|insights",
  "results": "object",
  "created_at": "datetime"
}
```

### Report
```json
{
  "id": "string",
  "title": "string",
  "content": "string",
  "format": "html|pdf|docx",
  "download_url": "string",
  "created_at": "datetime"
}
```

## Rate Limiting
- **Current**: No limits (single user)
- **Planned**: 100 requests per minute per user

## Examples

### Upload and Process Data (Future)
```bash
# Upload file
curl -X POST \
  http://localhost:3001/api/data/upload \
  -H "Authorization: Bearer <token>" \
  -F "file=@data.csv"

# Process data
curl -X PUT \
  http://localhost:3001/api/data/process \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"dataset_id": "123"}'
```

### Generate Report (Future)
```bash
curl -X POST \
  http://localhost:3001/api/reports/generate \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "dataset_id": "123",
    "type": "full_analysis",
    "format": "pdf"
  }'
```

## Migration Path

### Phase 1: Current (Streamlit)
- Interface web integrada
- Processamento em tempo real
- Sem autenticação

### Phase 2: Hybrid (Streamlit + FastAPI)
- Streamlit frontend mantido
- FastAPI backend para processamento
- Autenticação básica

### Phase 3: Full API (NestJS)
- API completa RESTful
- Documentação OpenAPI
- Autenticação JWT robusta
- Rate limiting e monitoramento