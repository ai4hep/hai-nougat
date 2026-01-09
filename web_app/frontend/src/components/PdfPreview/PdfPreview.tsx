import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import { Button, Space, Typography, Empty } from 'antd';
import { LeftOutlined, RightOutlined, ZoomInOutlined, ZoomOutOutlined } from '@ant-design/icons';
import { useAppContext } from '../../hooks/useAppContext';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import 'react-pdf/dist/Page/TextLayer.css';
import styles from './PdfPreview.module.css';

// Configure PDF.js worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

const { Text } = Typography;

const PdfPreview: React.FC = () => {
  const { selectedFile } = useAppContext();
  const [numPages, setNumPages] = useState<number>(0);
  const [pageNumber, setPageNumber] = useState<number>(1);
  const [scale, setScale] = useState<number>(1.0);

  const onDocumentLoadSuccess = ({ numPages }: { numPages: number }) => {
    setNumPages(numPages);
    setPageNumber(1);
  };

  if (!selectedFile) {
    return (
      <div className={styles.emptyState}>
        <Empty description="请先上传PDF文件" />
      </div>
    );
  }

  return (
    <div className={styles.pdfPreview}>
      <div className={styles.pdfControls}>
        <Space>
          <Button
            icon={<LeftOutlined />}
            onClick={() => setPageNumber(Math.max(1, pageNumber - 1))}
            disabled={pageNumber <= 1}
          />
          <Text>
            {pageNumber} / {numPages}
          </Text>
          <Button
            icon={<RightOutlined />}
            onClick={() => setPageNumber(Math.min(numPages, pageNumber + 1))}
            disabled={pageNumber >= numPages}
          />
        </Space>

        <Space>
          <Button
            icon={<ZoomOutOutlined />}
            onClick={() => setScale(Math.max(0.5, scale - 0.1))}
            disabled={scale <= 0.5}
          />
          <Text>{Math.round(scale * 100)}%</Text>
          <Button
            icon={<ZoomInOutlined />}
            onClick={() => setScale(Math.min(2.0, scale + 0.1))}
            disabled={scale >= 2.0}
          />
        </Space>
      </div>

      <div className={styles.pdfContainer}>
        <Document
          file={selectedFile.url}
          onLoadSuccess={onDocumentLoadSuccess}
          className={styles.document}
        >
          <Page
            pageNumber={pageNumber}
            scale={scale}
            className={styles.page}
          />
        </Document>
      </div>
    </div>
  );
};

export default PdfPreview;
