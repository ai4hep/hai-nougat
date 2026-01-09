import React from 'react';
import { Alert } from 'antd';
import { AppProvider } from './contexts/AppContext';
import MainLayout from './layout/MainLayout';
import { useAppContext } from './hooks/useAppContext';
import './styles/index.css';

const AppContent: React.FC = () => {
  const { healthStatus } = useAppContext();

  return (
    <>
      {healthStatus && !healthStatus.hepai_configured && (
        <Alert
          message="警告"
          description="后端API密钥未配置，请检查.env文件中的HEPAI_API_KEY设置"
          type="warning"
          showIcon
          closable
          style={{
            margin: '20px',
            position: 'fixed',
            top: 0,
            left: 0,
            right: 0,
            zIndex: 1000
          }}
        />
      )}
      <MainLayout />
    </>
  );
};

const App: React.FC = () => {
  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
};

export default App;
