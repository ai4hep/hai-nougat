import React, { useState } from 'react';
import { MathpixMarkdown, MathpixLoader } from '@mathpix/markdown-it';

const App = () => {
  const [markdownText, setMarkdownText] = useState('');

  return (
    <div className="App">
      <textarea
        value={markdownText}
        onChange={(e) => setMarkdownText(e.target.value)}
        placeholder="Enter Markdown text with math equations here..."
        style={{ width: "100%", height: "200px" }}
      />
      <MathpixLoader>
        <MathpixMarkdown text={markdownText} />
      </MathpixLoader>
    </div>
  );
};

export default App;