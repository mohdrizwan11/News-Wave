# News Wave - Deployment Guide

## Production Environment Variables

Set these environment variables on your production server:

```bash
NEWS_API_KEY=your_actual_newsapi_key
FLASK_CONFIG=production
SECRET_KEY=your_super_secret_production_key
PORT=5000
```

## Heroku Deployment

1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create app: `heroku create your-app-name`
4. Set environment variables:
   ```bash
   heroku config:set NEWS_API_KEY=your_api_key
   heroku config:set FLASK_CONFIG=production
   heroku config:set SECRET_KEY=your_secret_key
   ```
5. Deploy: `git push heroku main`

## Local Production Testing

```bash
# Set production environment
export FLASK_CONFIG=production
export FLASK_DEBUG=False

# Run with Gunicorn
gunicorn wsgi:app
```

## Security Checklist

- [ ] API keys in environment variables
- [ ] Debug mode disabled in production
- [ ] Strong secret key set
- [ ] Error logging configured
- [ ] HTTPS enabled (handled by platform)
- [ ] Environment variables secured on hosting platform
