# 🌊 News Wave - Global News Aggregation App

[![Live Demo](https://img.shields.io/badge/🌍_Live_Demo-Visit_App-blue?style=for-the-badge)](https://newswave-psi.vercel.app)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![Deployed on Vercel](https://img.shields.io/badge/Deployed_on-Vercel-black?style=flat-square&logo=vercel)](https://vercel.com)

A modern, responsive news aggregation web application that brings real-time global news to your fingertips. Built with Flask and powered by NewsAPI.

## 🚀 Live Application

**🌍 [Visit News Wave - Live Demo](https://newswave-psi.vercel.app)**

## ✨ Features

- **🔍 Smart Search** - Search for news by keywords across global sources
- **📱 Responsive Design** - Optimized for mobile, tablet, and desktop
- **🌍 Category Filtering** - Browse news by categories (Technology, Business, Sports, Health, etc.)
- **⚡ Fast Performance** - Intelligent caching system for optimal loading speed
- **🛡️ Rate Limiting Protection** - Handles API limits gracefully with fallback content
- **📊 Real-time Monitoring** - API usage tracking and status monitoring
- **🎨 Modern UI** - Clean, intuitive interface built with Bootstrap

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **API:** NewsAPI for real-time news data
- **Caching:** Flask-Caching for performance optimization
- **Deployment:** Vercel (Serverless)
- **Version Control:** Git, GitHub

## 🏗️ Architecture

- **Production-ready** configuration with environment-based settings
- **Caching layer** to optimize API usage and improve performance
- **Error handling** with custom error pages and graceful fallbacks
- **Security** features with environment variables and secret management

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/mohdrizwan11/News-Wave.git
cd News-Wave
```

2. **Create virtual environment:**
```bash
python -m venv venv
```

3. **Activate virtual environment:**
```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Set up environment variables:**
Create a `.env` file in the root directory:
```env
NEWS_API_KEY=your_newsapi_key_here
FLASK_CONFIG=development
SECRET_KEY=your_secret_key_here
```

6. **Run the application:**
```bash
# Quick start (Windows)
.\run.ps1

# Or manually
python app/app.py
```

7. **Open your browser:**
Navigate to `http://127.0.0.1:5000`

## 🌐 Deployment

This application is optimized for deployment on:
- **Vercel** (Current deployment: [newswave-psi.vercel.app](https://newswave-psi.vercel.app))
- **Render**
- **Heroku**
- **Railway**

### Deploy to Vercel
1. Fork this repository
2. Connect your GitHub account to Vercel
3. Import the project
4. Set environment variables
5. Deploy!

## 📊 API Usage

The app uses [NewsAPI](https://newsapi.org/) to fetch real-time news data. Features include:
- Global news sources
- Category filtering
- Keyword search
- Rate limiting protection (100 requests/day on free tier)

## 🔧 Configuration

### Environment Variables
- `NEWS_API_KEY`: Your NewsAPI key
- `FLASK_CONFIG`: `development` or `production`
- `SECRET_KEY`: Flask secret key for security

### Development vs Production
- **Development**: Debug mode enabled, detailed error messages
- **Production**: Optimized for performance, secure error handling

## 📁 Project Structure

```
News-Wave/
├── app/
│   ├── __init__.py
│   ├── app.py              # Main Flask application
│   ├── static/
│   │   └── styles.css      # Custom CSS
│   └── templates/
│       ├── news.html       # Main news page
│       ├── 404.html        # Error pages
│       ├── 500.html
│       ├── error.html
│       └── limit_reached.html
├── config.py               # Configuration management
├── wsgi.py                 # WSGI entry point
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel deployment config
├── runtime.txt            # Python runtime specification
├── run.ps1                # Quick start script
└── README.md

```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mohd Rizwan**
- GitHub: [@mohdrizwan11](https://github.com/mohdrizwan11)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/mohdrizwan11/)
- Portfolio: [News Wave Live Demo](https://newswave-psi.vercel.app)

## 🙏 Acknowledgments

- [NewsAPI](https://newsapi.org/) for providing the news data
- [Flask](https://flask.palletsprojects.com/) for the amazing web framework
- [Bootstrap](https://getbootstrap.com/) for the responsive UI components
- [Vercel](https://vercel.com/) for seamless deployment

---

⭐ **If you found this project helpful, please give it a star!** ⭐

**🌍 Live Demo:** [https://newswave-psi.vercel.app](https://newswave-psi.vercel.app)