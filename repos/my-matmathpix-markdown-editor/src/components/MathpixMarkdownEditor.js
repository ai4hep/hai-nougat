import React, { useState, useEffect} from 'react';
import { MathpixMarkdownModel as MM } from 'mathpix-markdown-it';

const MarkdownEdit = () => {
    const [htmlString, setHtmlString] = useState('');  // 存储解析后的html字符串

    // 设置 MathpixMarkdown 解析选项
    const options = {
    htmlTags: true,
    width: 800,
    outMath: { //You can set which formats should be included into html result
        include_mathml: true,
        include_asciimath: true,
        include_latex: true,
        include_svg: true, // sets in default
        include_tsv: true,
        include_table_html: true, // sets in default
    },
    codeHighlight: {
        auto: true,
        code: true
    }
    };

    const parse = (text) => {
    setHtmlString(MM.markdownToHTML(text, options));
    };
    

    return (
    <div className="markdownEditContainer">
        <main className="mmdContainer-main">
            <textarea
                className="edit"
                onChange={(e) => parse(e.target.value)}
            />
            <div
                className="show"
                id="write"
                dangerouslySetInnerHTML={{ __html: htmlString }}   
            />
        </main>
    </div>
    );
};

export default MarkdownEdit;