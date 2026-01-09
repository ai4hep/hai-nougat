import React from 'react';
import { Typography, Space, Badge, Tooltip } from 'antd';
import { ApiOutlined, CheckCircleOutlined, WarningOutlined } from '@ant-design/icons';
import { useAppContext } from '../hooks/useAppContext';
import styles from './Header.module.css';

const { Title, Text } = Typography;

const Header: React.FC = () => {
  const { healthStatus } = useAppContext();

  return (
    <div className={styles.headerContainer}>
      <Space size="large">
        <Title level={3} className={styles.title}>
          HaiNougat
        </Title>
        <Text className={styles.subtitle}>
          AI驱动的PDF转Markdown工具
        </Text>
      </Space>

      {healthStatus && (
        <Tooltip title={healthStatus.hepai_configured ? "API已配置" : "API未配置"}>
          <Badge
            status={healthStatus.hepai_configured ? "success" : "warning"}
            text={
              <Space style={{ color: 'white' }}>
                {healthStatus.hepai_configured ?
                  <CheckCircleOutlined /> :
                  <WarningOutlined />
                }
                <ApiOutlined />
              </Space>
            }
          />
        </Tooltip>
      )}
    </div>
  );
};

export default Header;
