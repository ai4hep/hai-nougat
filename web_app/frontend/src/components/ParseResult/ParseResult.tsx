import React from 'react';
import ReactMarkdown from 'react-markdown';
import { Empty, Typography, Spin } from 'antd';
import { useAppContext } from '../../hooks/useAppContext';
import styles from './ParseResult.module.css';

const { Text } = Typography;

const ParseResult: React.FC = () => {
  const { parseResult, uploadStatus } = useAppContext();

  if (uploadStatus.isUploading) {
    return (
      <div className={styles.loadingState}>
        <Spin size="large" />
        <Text>处理中... {uploadStatus.progress}%</Text>
      </div>
    );
  }

  if (!parseResult) {
    return (
      <div className={styles.emptyState}>
        <Empty description="运行后结果将在这里显示" />
      </div>
    );
  }

  return (
    <div className={styles.resultContainer}>
      <div className={styles.markdownContent}>
        <ReactMarkdown>{parseResult.content}</ReactMarkdown>
      </div>
    </div>
  );
};

export default ParseResult;
