import React from 'react';
import { Button, Typography } from 'antd';
import { PlayCircleOutlined } from '@ant-design/icons';
import PdfPreview from '../components/PdfPreview/PdfPreview';
import { useAppContext } from '../hooks/useAppContext';
import styles from './CenterPanel.module.css';

const { Title } = Typography;

const CenterPanel: React.FC = () => {
  const { selectedFile, handleUpload, uploadStatus } = useAppContext();

  const onRun = () => {
    if (selectedFile?.file) {
      handleUpload(selectedFile.file);
    }
  };

  return (
    <>
      <div className={styles.panelHeader}>
        <Title level={4} className={styles.panelTitle}>
          PDF预览
        </Title>
        <Button
          type="primary"
          icon={<PlayCircleOutlined />}
          onClick={onRun}
          disabled={!selectedFile || uploadStatus.isUploading}
          loading={uploadStatus.isUploading}
        >
          运行
        </Button>
      </div>
      <div className={styles.panelContent}>
        <PdfPreview />
      </div>
    </>
  );
};

export default CenterPanel;
