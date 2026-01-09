# HaiNougat Web Application

一个基于 React + FastAPI 的前后端分离架构，用于将 PDF 文档转换为 Markdown 格式。

## 项目结构

```
web_app/
├── frontend/          # React 前端应用
│   ├── public/        # 静态资源
│   ├── src/
│   │   ├── components/    # React 组件
│   │   ├── services/      # API 服务
│   │   └── styles/        # 样式文件
│   ├── package.json
│   └── .env           # 前端环境变量
│
└── backend/           # FastAPI 后端应用
    ├── app/
    │   ├── routers/       # API 路由
    │   ├── services/      # 业务逻辑
    │   ├── utils/         # 工具函数
    │   ├── models/        # 数据模型
    │   ├── config.py      # 配置管理
    │   └── main.py        # 应用入口
    ├── requirements.txt
    └── .env           # 后端环境变量
```

## 功能特性

- **PDF 上传**: 支持拖拽上传和点击选择
- **实时处理**: 显示上传进度和处理状态
- **结果展示**: Markdown 格式渲染
- **复制/下载**: 一键复制或下载转换结果
- **并发控制**: 限制最大并发请求数
- **文件验证**: 类型和大小验证

## 技术栈

### 前端
- React 18
- Ant Design (UI 组件库)
- React-Dropzone (文件上传)
- React-Markdown (Markdown 渲染)
- Axios (HTTP 客户端)

### 后端
- FastAPI (Web 框架)
- Uvicorn (ASGI 服务器)
- Pydantic (数据验证)
- HepAI SDK (AI 模型调用)

## 快速开始

### 后端设置

1. 进入后端目录:
```bash
cd web_app/backend
```

2. 安装依赖:
```bash
pip install -r requirements.txt
```

3. 配置环境变量:
```bash
cp .env.example .env
# 编辑 .env 文件，设置 HEPAI_API_KEY
```

4. 启动后端服务:
```bash
# 开发环境
python -m app.main

# 或使用 uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

后端服务将在 `http://localhost:8000` 启动

API 文档: `http://localhost:8000/api/v1/docs`

### 前端设置

1. 进入前端目录:
```bash
cd web_app/frontend
```

2. 安装依赖:
```bash
npm install
```

3. 配置环境变量:
```bash
cp .env.example .env
# 默认配置指向 http://localhost:8000
```

4. 启动前端开发服务器:
```bash
npm start
```

前端应用将在 `http://localhost:3000` 启动

## 环境变量配置

### 后端 (.env)
```env
HEPAI_API_KEY=your_api_key_here          # HepAI API 密钥 (必需)
HEPAI_API_URL=https://aiapi.ihep.ac.cn  # HepAI API 地址
HEPAI_MODEL=hepai/hainougat              # 使用的模型
HEPAI_TIMEOUT=3000                        # 请求超时时间(秒)

HOST=0.0.0.0                              # 服务器地址
PORT=8000                                 # 服务器端口

CORS_ORIGINS=http://localhost:3000       # 允许的跨域源
MAX_CONCURRENT_REQUESTS=5                # 最大并发请求数
UPLOAD_MAX_SIZE=10485760                 # 最大上传文件大小(字节)
```

### 前端 (.env)
```env
REACT_APP_API_URL=http://localhost:8000/api/v1  # 后端 API 地址
REACT_APP_MAX_FILE_SIZE=10485760                # 最大文件大小(字节)
```

## API 接口

### 上传 PDF
```
POST /api/v1/upload
Content-Type: multipart/form-data

Body:
- file: PDF 文件

Response:
{
  "message": "File processed successfully",
  "content": "转换后的 Markdown 内容",
  "filename": "原始文件名.pdf"
}
```

### 健康检查
```
GET /api/v1/health

Response:
{
  "status": "healthy",
  "version": "1.0.0",
  "hepai_configured": true
}
```

## 生产部署

### 后端部署

使用 Gunicorn + Uvicorn:
```bash
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### 前端部署

1. 构建生产版本:
```bash
cd web_app/frontend
npm run build
```

2. 使用 Nginx 部署:
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # 前端静态文件
    location / {
        root /path/to/web_app/frontend/build;
        try_files $uri /index.html;
    }

    # 后端 API 代理
    location /api/ {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 开发说明

### 后端代码结构

- `app/main.py`: FastAPI 应用入口
- `app/routers/`: API 路由定义
- `app/services/`: 业务逻辑层
  - `pdf_service.py`: PDF 文件处理
  - `hai_service.py`: HaiNougat 模型调用
- `app/utils/`: 工具函数
  - `validators.py`: 文件验证
  - `limiter.py`: 并发限制
- `app/models/`: Pydantic 数据模型
- `app/config.py`: 配置管理

### 前端代码结构

- `src/App.jsx`: 主应用组件
- `src/components/`:
  - `Upload.jsx`: 文件上传组件
  - `Result.jsx`: 结果展示组件
- `src/services/api.js`: API 调用封装
- `src/styles/`: CSS 样式文件

## 常见问题

### 1. 后端启动失败
- 检查 Python 版本 (推荐 3.8+)
- 确认所有依赖已安装
- 检查 `.env` 文件中的 API Key 配置

### 2. 前端无法连接后端
- 确认后端服务已启动
- 检查 `.env` 文件中的 `REACT_APP_API_URL` 配置
- 查看浏览器控制台是否有 CORS 错误

### 3. 文件上传失败
- 确认文件是有效的 PDF 格式
- 检查文件大小是否超过限制
- 查看后端日志获取详细错误信息

## 许可证

本项目遵循原项目许可协议。

## 联系方式

如有问题或建议，请联系项目维护者。
