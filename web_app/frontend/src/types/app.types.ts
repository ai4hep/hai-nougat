// Application State Types

import { FileInfo, ParseResult, UploadStatus } from './file.types';
import { HealthResponse } from './api.types';

export interface AppState {
  selectedFile: FileInfo | null;
  uploadStatus: UploadStatus;
  parseResult: ParseResult | null;
  healthStatus: HealthResponse | null;
}

export interface AppContextValue extends AppState {
  setSelectedFile: (file: FileInfo | null) => void;
  handleUpload: (file: File) => Promise<void>;
  clearResult: () => void;
  downloadResult: () => void;
}
