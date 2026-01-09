// File Related Types

export interface FileInfo {
  file: File;
  name: string;
  size: number;
  type: string;
  url?: string; // Object URL for preview
}

export interface UploadStatus {
  isUploading: boolean;
  progress: number;
  error: string | null;
}

export interface ParseResult {
  content: string;
  filename: string;
  timestamp: Date;
}
