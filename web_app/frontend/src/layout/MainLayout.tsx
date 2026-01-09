import React from 'react';
import { Layout } from 'antd';
import Header from './Header';
import LeftSidebar from './LeftSidebar';
import CenterPanel from './CenterPanel';
import RightPanel from './RightPanel';
import styles from './MainLayout.module.css';

const { Header: AntHeader, Content } = Layout;

const MainLayout: React.FC = () => {
  return (
    <Layout className={styles.mainLayout}>
      <AntHeader className={styles.header}>
        <Header />
      </AntHeader>
      <Content className={styles.content}>
        <div className={styles.threeColumnLayout}>
          <aside className={styles.leftSidebar}>
            <LeftSidebar />
          </aside>
          <main className={styles.centerPanel}>
            <CenterPanel />
          </main>
          <aside className={styles.rightPanel}>
            <RightPanel />
          </aside>
        </div>
      </Content>
    </Layout>
  );
};

export default MainLayout;
