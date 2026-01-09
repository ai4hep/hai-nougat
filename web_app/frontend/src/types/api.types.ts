// API Response Types

export interface UploadResponse {
  message: string;
  content: string;
  filename: string | null;
}

export interface HealthResponse {
  status: string;
  version: string;
  hepai_configured: boolean;
}

export interface ErrorResponse {
  detail: string;
  status_code: number;
}

export type ProgressCallback = (progress: number) => void;
