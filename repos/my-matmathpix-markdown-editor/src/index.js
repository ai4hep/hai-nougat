import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { MathpixMarkdownModel as MM } from 'mathpix-markdown-it';

// 获取 Mathpix 的字体和主要样式
const mathFontsStyle = MM.getMathpixFontsStyle();
const mathpixStyles = MM.getMathpixStyle(true);

// 创建字体样式标签并设置内容
const fontStyleElement = document.createElement('style');
fontStyleElement.textContent = mathFontsStyle;

// 创建 Mathpix 样式标签并设置内容
const mathpixStyleElement = document.createElement('style');
mathpixStyleElement.textContent = mathpixStyles;

// 将样式标签插入到文档头部
document.head.appendChild(fontStyleElement);
document.head.appendChild(mathpixStyleElement);

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();