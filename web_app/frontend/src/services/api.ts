import axios, { AxiosInstance, AxiosProgressEvent } from 'axios';
import { UploadResponse, HealthResponse, ProgressCallback } from '../types/api.types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const apiClient: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'multipart/form-data',
  },
});

/**
 * Upload PDF file for processing
 */
export const uploadPDF = async (
  file: File,
  onProgress?: ProgressCallback
): Promise<UploadResponse> => {
  const formData = new FormData();
  formData.append('file', file);

  const config = {
    onUploadProgress: (progressEvent: AxiosProgressEvent) => {
      if (progressEvent.total) {
        const percentCompleted = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total
        );
        onProgress?.(percentCompleted);
      }
    },
  };

  const response = await apiClient.post<UploadResponse>('/upload', formData, config);
  return response.data;
};

/**
 * Check API health status
 */
export const checkHealth = async (): Promise<HealthResponse> => {
  const response = await apiClient.get<HealthResponse>('/health');
  return response.data;
};

export default apiClient;
