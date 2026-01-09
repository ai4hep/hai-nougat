# HaiNougat - 快速启动指南

## 项目已成功创建！

前后端分离架构已完成，包含以下内容：

### 📁 项目结构
```
web_app/
├── backend/          # FastAPI 后端
│   ├── app/          # 应用代码
│   ├── .env          # 环境配置（需要设置 API Key）
│   ├── requirements.txt
│   └── start.sh      # 启动脚本
│
├── frontend/         # React 前端
│   ├── src/          # 源代码
│   ├── public/       # 静态资源
│   ├── package.json
│   └── start.sh      # 启动脚本
│
└── README.md         # 详细文档
```

## 🚀 快速启动

### 1. 启动后端（必需）

```bash
cd web_app/backend

# 方式1: 使用启动脚本
./start.sh

# 方式2: 直接运行
python -m app.main
```

后端将在 http://localhost:8000 启动

**重要**: 在 `backend/.env` 中设置你的 `HEPAI_API_KEY`

### 2. 启动前端

在新的终端窗口中：

```bash
cd web_app/frontend

# 首次运行需要安装依赖
npm install

# 方式1: 使用启动脚本
./start.sh

# 方式2: 直接运行
npm start
```

前端将在 http://localhost:3000 启动

## ✅ 验证安装

### 测试后端
```bash
# 健康检查
curl http://localhost:8000/api/v1/health

# 访问 API 文档
浏览器打开: http://localhost:8000/api/v1/docs
```

### 测试前端
浏览器打开: http://localhost:3000

## ⚙️ 配置说明

### 后端配置 (backend/.env)
```bash
# 必需配置
HEPAI_API_KEY=your_actual_api_key_here

# 可选配置
HEPAI_API_URL=https://aiapi.ihep.ac.cn
MAX_CONCURRENT_REQUESTS=5
PORT=8000
```

### 前端配置 (frontend/.env)
```bash
# API 地址（默认已配置）
REACT_APP_API_URL=http://localhost:8000/api/v1
```

## 📝 使用流程

1. ✅ 后端已启动 → 访问 http://localhost:8000/api/v1/docs 查看 API 文档
2. ✅ 前端已启动 → 访问 http://localhost:3000 使用应用
3. 📤 上传 PDF 文件
4. ⏳ 等待处理完成
5. 📄 查看 Markdown 结果，可复制或下载

## 🔧 常见问题

### 后端启动失败
```bash
# 检查依赖
pip install -r requirements.txt

# 检查 .env 配置
cat .env

# 查看详细错误
python -m app.main
```

### 前端启动失败
```bash
# 重新安装依赖
rm -rf node_modules package-lock.json
npm install

# 检查 Node.js 版本
node --version  # 需要 14+
```

### 无法连接后端
1. 确认后端正在运行: `curl http://localhost:8000/api/v1/health`
2. 检查 `frontend/.env` 中的 `REACT_APP_API_URL`
3. 查看浏览器控制台的错误信息

## 📚 详细文档

- 完整文档: `web_app/README.md`
- 后端部署: `web_app/backend/DEPLOYMENT.md`
- 前端部署: `web_app/frontend/DEPLOYMENT.md`

## 🎯 下一步

1. **开发测试**: 上传 PDF 文件测试功能
2. **配置优化**: 根据需要调整并发数、文件大小限制等
3. **生产部署**: 参考 DEPLOYMENT.md 进行生产环境部署

## 💡 提示

- 开发时保持两个终端窗口：一个运行后端，一个运行前端
- 后端支持热重载（修改代码自动重启）
- 前端支持热更新（修改代码自动刷新浏览器）
- API 文档自动生成，访问 /api/v1/docs 查看

---

**问题反馈**: 如有问题，请查看日志输出或参考详细文档
