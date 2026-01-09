import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Typography, Button, message } from 'antd';
import { UploadOutlined, FileOutlined, DeleteOutlined } from '@ant-design/icons';
import { useAppContext } from '../../hooks/useAppContext';
import { FileInfo } from '../../types/file.types';
import styles from './FileSource.module.css';

const { Title, Text } = Typography;
const MAX_FILE_SIZE = parseInt(process.env.REACT_APP_MAX_FILE_SIZE || '10485760');

const FileSource: React.FC = () => {
  const { selectedFile, setSelectedFile } = useAppContext();

  const onDrop = useCallback((acceptedFiles: File[], rejectedFiles: any[]) => {
    if (rejectedFiles.length > 0) {
      const rejection = rejectedFiles[0];
      if (rejection.file.size > MAX_FILE_SIZE) {
        message.error(`文件大小不能超过 ${MAX_FILE_SIZE / (1024 * 1024)}MB`);
      } else {
        message.error('请上传PDF文件');
      }
      return;
    }

    if (acceptedFiles.length > 0) {
      const file = acceptedFiles[0];
      const fileInfo: FileInfo = {
        file,
        name: file.name,
        size: file.size,
        type: file.type,
        url: URL.createObjectURL(file),
      };
      setSelectedFile(fileInfo);
      message.success(`已选择文件: ${file.name}`);
    }
  }, [setSelectedFile]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { 'application/pdf': ['.pdf'] },
    maxSize: MAX_FILE_SIZE,
    multiple: false,
  });

  const handleRemove = () => {
    if (selectedFile?.url) {
      URL.revokeObjectURL(selectedFile.url);
    }
    setSelectedFile(null);
  };

  const formatFileSize = (bytes: number): string => {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(2) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
  };

  return (
    <div className={styles.fileSource}>
      <Title level={4}>文件来源</Title>

      <div
        {...getRootProps()}
        className={`${styles.dropzone} ${isDragActive ? styles.active : ''}`}
      >
        <input {...getInputProps()} />
        <div className={styles.dropzoneContent}>
          <UploadOutlined className={styles.uploadIcon} />
          {isDragActive ? (
            <Text>放开鼠标上传文件</Text>
          ) : (
            <>
              <Text>拖拽PDF文件到这里</Text>
              <Text type="secondary" className={styles.hint}>
                或点击选择文件
              </Text>
            </>
          )}
        </div>
      </div>

      {selectedFile && (
        <div className={styles.fileInfo}>
          <div className={styles.fileDetails}>
            <FileOutlined className={styles.fileIcon} />
            <div>
              <div className={styles.fileName}>{selectedFile.name}</div>
              <Text type="secondary" className={styles.fileSize}>
                {formatFileSize(selectedFile.size)}
              </Text>
            </div>
          </div>
          <Button
            type="text"
            danger
            icon={<DeleteOutlined />}
            onClick={handleRemove}
          />
        </div>
      )}
    </div>
  );
};

export default FileSource;
