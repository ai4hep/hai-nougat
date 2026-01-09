import React from 'react';
import { Button, Typography } from 'antd';
import { DownloadOutlined } from '@ant-design/icons';
import ParseResult from '../components/ParseResult/ParseResult';
import { useAppContext } from '../hooks/useAppContext';
import styles from './RightPanel.module.css';

const { Title } = Typography;

const RightPanel: React.FC = () => {
  const { parseResult, downloadResult } = useAppContext();

  return (
    <>
      <div className={styles.panelHeader}>
        <Title level={4} className={styles.panelTitle}>
          运行结果
        </Title>
        {parseResult && (
          <Button
            type="primary"
            icon={<DownloadOutlined />}
            onClick={downloadResult}
          >
            下载
          </Button>
        )}
      </div>
      <div className={styles.panelContent}>
        <ParseResult />
      </div>
    </>
  );
};

export default RightPanel;
