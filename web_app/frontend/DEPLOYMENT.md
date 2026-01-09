# Frontend Deployment Guide

## Development Environment

```bash
cd web_app/frontend
npm install
cp .env.example .env
npm start
```

The app will run at `http://localhost:3000`

## Production Build

```bash
npm run build
```

This creates an optimized production build in the `build/` directory.

## Deployment Options

### 1. Nginx

Install Nginx and configure:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Frontend
    location / {
        root /path/to/web_app/frontend/build;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # Backend API proxy
    location /api/ {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        proxy_read_timeout 300s;
    }
}
```

Enable and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/hainougat /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 2. Serve with Node.js

Install serve:
```bash
npm install -g serve
```

Serve the build:
```bash
serve -s build -l 3000
```

### 3. Deploy to Vercel

```bash
npm install -g vercel
vercel --prod
```

Configure environment variables in Vercel dashboard.

### 4. Deploy to Netlify

Create `netlify.toml`:

```toml
[build]
  command = "npm run build"
  publish = "build"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

Deploy:
```bash
npm install -g netlify-cli
netlify deploy --prod
```

### 5. Docker

Create `Dockerfile`:

```dockerfile
FROM node:18-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Create `nginx.conf`:

```nginx
server {
    listen 80;
    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
}
```

Build and run:
```bash
docker build -t hainougat-frontend .
docker run -d -p 80:80 hainougat-frontend
```

## Environment Variables

For production, update `.env`:

```env
REACT_APP_API_URL=https://api.yourdomain.com/api/v1
REACT_APP_MAX_FILE_SIZE=10485760
```

## Performance Optimization

### Enable Gzip Compression (Nginx)

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml+rss application/json;
```

### Enable Caching (Nginx)

```nginx
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### CDN Integration

Upload the `build/` directory to your CDN (e.g., Cloudflare, AWS CloudFront).

## SSL/HTTPS Setup

Using Let's Encrypt with Certbot:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

## Monitoring

Add analytics or monitoring:

```jsx
// In src/index.jsx
import ReactGA from 'react-ga4';

ReactGA.initialize('YOUR-GA-ID');
```

## Troubleshooting

### Build fails
- Check Node.js version (14+ required)
- Clear cache: `rm -rf node_modules package-lock.json && npm install`

### API connection issues
- Verify `REACT_APP_API_URL` in `.env`
- Check CORS settings on backend
- Verify backend is accessible from frontend host
