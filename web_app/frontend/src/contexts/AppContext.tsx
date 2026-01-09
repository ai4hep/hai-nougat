import React, { createContext, useState, useCallback, ReactNode, useEffect } from 'react';
import { message } from 'antd';
import { uploadPDF, checkHealth } from '../services/api';
import { AppContextValue, AppState } from '../types/app.types';
import { FileInfo, ParseResult } from '../types/file.types';

const AppContext = createContext<AppContextValue | undefined>(undefined);

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, setState] = useState<AppState>({
    selectedFile: null,
    uploadStatus: { isUploading: false, progress: 0, error: null },
    parseResult: null,
    healthStatus: null,
  });

  // Check health on mount
  useEffect(() => {
    checkHealth()
      .then(data => {
        setState(prev => ({ ...prev, healthStatus: data }));
        if (!data.hepai_configured) {
          console.warn('HepAI API key not configured');
        }
      })
      .catch(error => {
        console.error('Backend health check failed:', error);
      });
  }, []);

  const setSelectedFile = useCallback((file: FileInfo | null) => {
    setState(prev => ({ ...prev, selectedFile: file }));
  }, []);

  const handleUpload = useCallback(async (file: File) => {
    setState(prev => ({
      ...prev,
      uploadStatus: { isUploading: true, progress: 0, error: null }
    }));

    try {
      const response = await uploadPDF(file, (progress) => {
        setState(prev => ({
          ...prev,
          uploadStatus: { ...prev.uploadStatus, progress }
        }));
      });

      const result: ParseResult = {
        content: response.content,
        filename: response.filename || file.name,
        timestamp: new Date(),
      };

      setState(prev => ({
        ...prev,
        parseResult: result,
        uploadStatus: { isUploading: false, progress: 100, error: null }
      }));

      message.success('PDF处理成功！');
    } catch (error: any) {
      const errorMsg = error.response?.data?.detail || '上传失败，请重试';
      setState(prev => ({
        ...prev,
        uploadStatus: { isUploading: false, progress: 0, error: errorMsg }
      }));
      message.error(errorMsg);
    }
  }, []);

  const clearResult = useCallback(() => {
    setState(prev => ({ ...prev, parseResult: null, selectedFile: null }));
  }, []);

  const downloadResult = useCallback(() => {
    if (!state.parseResult) return;

    const blob = new Blob([state.parseResult.content], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = state.parseResult.filename.replace('.pdf', '') + '.md';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    message.success('文件已下载');
  }, [state.parseResult]);

  const value: AppContextValue = {
    ...state,
    setSelectedFile,
    handleUpload,
    clearResult,
    downloadResult,
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
};

export default AppContext;
