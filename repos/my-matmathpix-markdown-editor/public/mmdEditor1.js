import React, { useState, useEffect, useRef } from 'react';
import { MathpixMarkdownModel as MM } from 'mathpix-markdown-it';

const MarkdownEdit = () => {
  const [inputText, setInputText] = useState(''); 
  const [htmlString, setHtmlString] = useState(''); 
  const fileInputRef = useRef(null); 

  const options = {
    htmlTags: true,
    outMath: {
      include_mathml: true,
      include_asciimath: true,
      include_latex: true,
      include_svg: true, 
      include_tsv: true,
      include_table_html: true, 
    },
    codeHighlight: {
      auto: true,
      code: true,
    },
  };

  const parse = (text) => {
    setHtmlString(MM.markdownToHTML(text, options));
  };

  const handleButtonClick = () => {
    fileInputRef.current.click(); 
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    const allowedExtensions = /(\.md|\.mmd)$/i; 
    if (!allowedExtensions.exec(file.name)) {
      alert('只能上传.md和.mmd为后缀的文件');
      return;
    }
  
    const reader = new FileReader();
    reader.onload = (e) => {
      const fileContent = e.target.result;
      setInputText(fileContent); 
      parse(fileContent); 
    };
    reader.readAsText(file);
  };

  useEffect(() => {
    const mathFontsStyle = MM.getMathpixFontsStyle();
    const mathpixStyles = MM.getMathpixStyle(true);

    const fontStyleElement = document.createElement('style');
    fontStyleElement.textContent = mathFontsStyle;

    const mathpixStyleElement = document.createElement('style');
    mathpixStyleElement.textContent = mathpixStyles;

    document.head.appendChild(fontStyleElement);
    document.head.appendChild(mathpixStyleElement);

    return () => {
      document.head.removeChild(fontStyleElement);
      document.head.removeChild(mathpixStyleElement);
    };
  }, []);

  return (
    <div className="markdownEditContainer">
      <div className="toolbar">
         <button className="upload-btn" onClick={handleButtonClick}>
         <div className="arrow-container">
        <div className="arrow-up"></div>
        <div className="arrow-stem"></div>
        <div className="upload-bar"></div>
      </div>
          上传文件
        </button>
        <input 
          type="file" 
          ref={fileInputRef} 
          style={{ display: 'none' }} 
          onChange={handleFileChange} 
        />
      </div>
      <main className="mmdContainer-main">
        <div className="mmdedit-container">
          <textarea
            className="mmdedit"
            value={inputText} 
            onChange={(e) => {
              setInputText(e.target.value);
              parse(e.target.value); 
            }}
          />
        
        <div className="mmdshow">
          <div
            id="preview"
            style={{ justifyContent: 'center', overflowY: 'unset', willChange: 'transform' }}
          >
            <div id="container-ruller"></div>
            <div
              id="setText"
              style={{ display: 'block', justifyContent: 'inherit' }}
              dangerouslySetInnerHTML={{ __html: htmlString }}
            ></div>
          </div>
        </div>
        </div>
      </main>
    </div>
  );
};

export default MarkdownEdit;