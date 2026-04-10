# 🚀 Media Downloader Pro - Setup Guide

Complete installation and configuration guide for developers and users.

## Prerequisites

### System Requirements
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 10GB free space in Google Colab
- **Internet**: Stable connection (minimum 5 Mbps recommended)
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)

### Software Requirements
- Python 3.7+ (pre-installed in Google Colab)
- Google account (for Colab access)
- No command-line knowledge required

## Installation Methods

### Method 1: Google Colab (Recommended)

**Easiest way to get started - no installation needed!**

1. **Open Google Colab**
   - Visit: https://colab.research.google.com/
   - Click "File" → "New Notebook"

2. **Install Dependencies**
   ```python
   !pip install -U yt-dlp ipywidgets -q
   ```
   Run this cell and wait for completion (30-60 seconds)

3. **Copy the Code**
   - Get the full code from `media_downloader_pro_en.py`
   - Paste into a new notebook cell
   - Click "Run" or press Ctrl+Enter

4. **Start Using**
   - The UI will appear immediately below the cell
   - Paste any video URL and click "Analyze"

### Method 2: Local Python Environment

For running on your local machine (advanced users):

1. **Create Virtual Environment**
   ```bash
   python3 -m venv media_downloader
   source media_downloader/bin/activate  # On Windows: media_downloader\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install yt-dlp ipywidgets jupyter ipython
   ```

3. **Create Script**
   - Save `media_downloader_pro_en.py` in your project folder
   - Modify the import statement (remove Google Colab imports):
   ```python
   # Remove this line:
   # from google.colab import files
   
   # Add this instead:
   import webbrowser
   import json
   ```

4. **Run Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
   - Create new notebook or use the script
   - Follow same usage as Colab

**Note**: Local version requires additional setup for file downloads

### Method 3: Command-Line Download

Direct download without notebook interface:

```bash
# Install yt-dlp directly
pip install yt-dlp

# Download single video
yt-dlp -f "best[height<=1080]" "YOUR_VIDEO_URL"

# Download with audio merge
yt-dlp -f "best[height<=1080]+bestaudio" "YOUR_VIDEO_URL"
```

## Configuration

### Custom Download Directory

In Google Colab, files are saved to `/content/downloads/`

To use Google Drive instead:

```python
# Add to top of script
from google.colab import drive
drive.mount('/content/drive')

# Change this line:
DOWNLOAD_DIR = "/content/downloads"

# To this:
DOWNLOAD_DIR = "/content/drive/My Drive/Downloads"
```

### Quality Preferences

Modify default quality in `handle_download()`:

```python
# Current (best quality + best audio)
opts = {
    'format': f"{format_dropdown.value}+bestaudio/best",
}

# For faster downloads (lower quality + audio)
opts = {
    'format': f"best[height<=720]+bestaudio/best",
}

# For maximum quality
opts = {
    'format': f"best+bestaudio/best",
}
```

### UI Customization

#### Color Scheme

In `style_css`, modify these colors:

```css
/* Dark mode example */
body {
    background: #1a1a1a;
    color: #ffffff;
}

.main-container {
    background: #1a1a1a;
}

.widget-text input {
    background: #2d2d2d !important;
    color: #ffffff !important;
    border-color: #404040 !important;
}

.btn-download {
    background: #0066cc !important;
    border-color: #0066cc !important;
}
```

#### Font Changes

Replace IBM Plex with system fonts:

```css
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
}

.logo-text {
    font-family: 'Courier New', monospace;
}
```

#### Responsive Width

Change `max-width` of container:

```css
.main-container {
    max-width: 100%;  /* Full width */
    /* or */
    max-width: 1200px;  /* Wider layout */
}
```

## Troubleshooting Setup

### pip install fails

**Error**: "Command 'pip' not found"

**Solution**:
```bash
# Use pip3 instead
python3 -m pip install yt-dlp ipywidgets

# Or for Colab
!pip3 install -U yt-dlp ipywidgets -q
```

### Import errors

**Error**: "No module named 'yt_dlp'"

**Solution**:
1. Restart the kernel/notebook
2. Re-run the pip install command
3. Check Python version: `python --version`

### Display issues in Colab

**Issue**: UI doesn't appear or looks broken

**Solution**:
```python
# Try restarting the kernel
import IPython
IPython.display.clear_output(wait=True)

# Or restart runtime: Runtime → Restart Runtime
```

### Network errors during download

**Error**: "Connection refused" or "Timeout"

**Solutions**:
1. Check internet connection
2. Try downloading during off-peak hours
3. Use VPN if your region blocks certain platforms
4. Check if platform is down (visit in browser)

## Performance Optimization

### For Slow Connections

```python
# Download smaller files first to test
# Use 480p or 720p instead of 1080p

# Increase timeout in yt-dlp options
ydl_opts = {
    'quiet': True,
    'noplaylist': True,
    'no_warnings': True,
    'socket_timeout': 30,  # Increase from default
}
```

### For Large Files

```python
# Enable resumable downloads
opts = {
    'format': f"{format_dropdown.value}+bestaudio/best",
    'continue_dl': True,  # Resume interrupted downloads
    'fragment_retries': 10,  # Retry fragments
}
```

### Memory Issues

If notebook crashes on large files:

```python
# Reduce quality to 720p
opts = {
    'format': 'best[height<=720]+bestaudio/best',
}

# Or restart runtime and download one at a time
```

## Advanced Configuration

### Proxy Setup

For restricted networks:

```python
ydl_opts = {
    'proxy': 'http://proxy.example.com:8080',
}

# Or with authentication:
ydl_opts = {
    'proxy': 'http://user:password@proxy.example.com:8080',
}
```

### Custom Headers

For sites requiring specific headers:

```python
ydl_opts = {
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0',
        'Accept-Language': 'en-US,en;q=0.9',
    }
}
```

### Authentication

For age-restricted or private videos:

```python
# YouTube with login (requires cookies)
ydl_opts = {
    'cookiesfrombrowser': 'chrome',  # Uses Chrome cookies
    'quiet': True,
}

# Note: YouTube account authentication is complex
# Consider using direct downloads when possible
```

## Version Management

### Check Installed Versions

```python
import yt_dlp
import ipywidgets
print(f"yt-dlp: {yt_dlp.__version__}")
print(f"ipywidgets: {ipywidgets.__version__}")
```

### Update Packages

```python
!pip install --upgrade yt-dlp ipywidgets
```

### Pin Specific Versions

For reproducibility:

```bash
pip install yt-dlp==2024.1.0
pip install ipywidgets==7.6.5
```

Add to `requirements.txt`:

```
yt-dlp==2024.1.0
ipywidgets==7.6.5
jupyter==1.0.0
ipython==8.0.0
```

Install from requirements:
```bash
pip install -r requirements.txt
```

## Docker Setup (Advanced)

For containerized deployment:

**Dockerfile**:
```dockerfile
FROM jupyter/base-notebook:latest

RUN pip install --no-cache-dir \
    yt-dlp==2024.1.0 \
    ipywidgets==7.6.5

COPY media_downloader_pro_en.py /home/jovyan/work/

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0"]
```

**Build & Run**:
```bash
docker build -t media-downloader .
docker run -p 8888:8888 media-downloader
```

## Git Setup for Developers

**Clone Repository**:
```bash
git clone https://github.com/yourusername/media-downloader-pro.git
cd media-downloader-pro
```

**Create Branch**:
```bash
git checkout -b feature/your-feature
```

**Make Changes & Commit**:
```bash
git add .
git commit -m "Add feature: your feature description"
git push origin feature/your-feature
```

**File Structure**:
```
media-downloader-pro/
├── README.md                          # Main documentation
├── SETUP.md                          # This file
├── LICENSE                           # MIT License
├── CONTRIBUTING.md                   # Contribution guidelines
├── media_downloader_pro_en.py         # Main script
├── requirements.txt                  # Python dependencies
├── Dockerfile                        # Container config
└── docs/
    ├── API.md                        # API reference
    ├── TROUBLESHOOTING.md           # Common issues
    └── EXAMPLES.md                   # Usage examples
```

## Getting Help

1. **Check Documentation**
   - README.md - Overview
   - SETUP.md - Installation (you are here)
   - TROUBLESHOOTING.md - Common issues

2. **Search Issues**
   - GitHub Issues tab
   - Look for similar error messages

3. **Ask Community**
   - Create new issue with details
   - Join discussions

4. **Debug Steps**
   ```python
   # Enable detailed logging
   import logging
   logging.basicConfig(level=logging.DEBUG)
   
   # Test URL
   from yt_dlp import YoutubeDL
   ydl = YoutubeDL({'quiet': False})  # Set False to see details
   info = ydl.extract_info("YOUR_URL", download=False)
   ```

## Next Steps

1. ✅ Complete installation
2. 📖 Read README.md for features overview
3. 🎬 Try your first video download
4. 🔧 Customize settings as needed
5. 📢 Share feedback and report issues

---

**Questions?** Check TROUBLESHOOTING.md or create a GitHub issue

**Happy downloading!** 🚀
