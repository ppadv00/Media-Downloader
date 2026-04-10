# 🎬 Media Downloader Pro

**A professional video capture and metadata analysis tool for Google Colab**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-2024.1.0+-green.svg)](https://github.com/yt-dlp/yt-dlp)

## Features

✨ **Multi-Platform Support**
- YouTube, Vimeo, and 1000+ video hosting platforms
- Support for both single videos and playlists
- Adaptive quality detection

📊 **Real-Time Metadata Extraction**
- Video title, duration, and upload date
- View counts and engagement metrics
- Channel/uploader information
- Thumbnail preview

🎯 **Smart Quality Selection**
- Multiple resolution options with estimated file sizes
- FPS information for each quality level
- Automatic audio merging with selected video quality

💻 **Professional UI**
- Modern, minimal design system (IBM Carbon principles)
- Responsive layout for mobile and desktop
- Real-time progress indicators
- Accessible color contrast and typography

⚡ **One-Click Download**
- Seamless video + audio merging
- Automatic file size calculation
- Direct browser download integration
- Comprehensive error handling

## Getting Started

### Requirements

- **Python**: 3.7 or higher
- **Google Colab**: Active environment with internet access
- **Packages**:
  - `yt-dlp >= 2024.1.0`
  - `ipywidgets >= 7.6.0`
  - `IPython` (pre-installed in Colab)

### Installation

1. Open this notebook in [Google Colab](https://colab.research.google.com/)
2. Run the first cell to install dependencies:

```python
!pip install -U yt-dlp ipywidgets -q
```

3. Run all cells to initialize the application
4. The UI will appear in the output area

### Quick Start

```python
# 1. Copy the script into a Google Colab notebook cell
# 2. Run the cell
# 3. Paste a video URL in the input field
# 4. Click "Analyze" to fetch metadata
# 5. Select your desired quality from the dropdown
# 6. Click "Download as MP4" to start the download
```

## Usage

### Basic Workflow

**Step 1: Analyze Video**
```
Input: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Click: "Analyze" button
Output: Video preview card with metadata
```

**Step 2: Select Quality**
```
Choose from available resolutions in dropdown
(e.g., "1080p (120 MB) • 60fps")
```

**Step 3: Download**
```
Click: "Download as MP4" button
Wait for processing (video encoding + audio merge)
File downloads automatically to your computer
```

### Supported Platforms

- **YouTube** - Full support (respects download restrictions)
- **Vimeo** - High quality available
- **Dailymotion**, **Twitch**, **Facebook** - Supported
- **1000+ other platforms** - Via yt-dlp compatibility

### Quality Options Explained

```
1080p (250 MB) • 60fps
├── 1080p = Video resolution
├── 250 MB = Estimated file size
└── 60fps = Frames per second
```

## Architecture

### Core Components

```
┌─────────────────────────────────────────────┐
│          UI Layer (ipywidgets)              │
│  ┌─────────────┐  ┌──────────────────────┐  │
│  │   Header    │  │   Input Controls     │  │
│  └─────────────┘  └──────────────────────┘  │
│  ┌─────────────────────────────────────┐    │
│  │       Video Preview Card            │    │
│  │  ┌──────────┐  ┌─────────────────┐  │    │
│  │  │ Thumbnail│  │ Metadata Grid   │  │    │
│  │  └──────────┘  └─────────────────┘  │    │
│  └─────────────────────────────────────┘    │
│  ┌──────────────────────────────────────┐   │
│  │ Quality Selector + Download Button   │   │
│  └──────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────┐
│      Business Logic Layer (Python)          │
│  ┌──────────────────────────────────────┐   │
│  │  get_info(url)  - Metadata Extractor │   │
│  │  format_number() - Number Formatter  │   │
│  │  format_date()  - Date Formatter     │   │
│  └──────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────┐
│      Media Layer (yt-dlp)                   │
│  ├── Video Stream Detection                 │
│  ├── Audio Stream Detection                 │
│  ├── Format & Quality Resolution            │
│  └── Download & Merge Engine                │
└─────────────────────────────────────────────┘
```

### Data Flow

```
URL Input
   ↓
[Validation]
   ↓
yt-dlp Extraction → Metadata Dict
   ↓
Format Filtering (MP4 only, valid resolutions)
   ↓
Quality Dropdown Population
   ↓
[User Selects Quality]
   ↓
Download Handler → yt-dlp Download + Merge
   ↓
Browser Download
```

## Configuration

### Default Settings

```python
# Download directory
DOWNLOAD_DIR = "/content/downloads"

# yt-dlp options for metadata extraction
ydl_opts = {
    'quiet': True,           # Suppress output
    'noplaylist': True,      # Single video only
    'no_warnings': True      # Clean logs
}

# Download options with audio merge
opts = {
    'format': 'VIDEO_ID+bestaudio/best',  # Video + best audio
    'merge_output_format': 'mp4',         # Output format
    'quiet': True,
    'no_warnings': True
}
```

### Customization

**Change download directory:**
```python
DOWNLOAD_DIR = "/path/to/your/directory"
```

**Modify quality filter:**
```python
# In get_info() function, change the format filter:
if f.get('ext') == 'mkv' and res:  # Changed from 'mp4'
```

**Adjust UI styling:**
Edit the `style_css` variable to customize colors, fonts, and layout.

## Limitations

⚠️ **Important Considerations**

1. **Download Rights**: Respect copyright and terms of service
   - Some platforms prohibit downloading
   - Always check creator permissions
   - For YouTube: personal use only, no redistribution

2. **Platform Restrictions**
   - Age-restricted videos may require authentication
   - Live streams cannot be downloaded
   - Geo-blocked content may not be accessible

3. **File Size Constraints**
   - Colab storage: ~100GB total
   - Download speed depends on your internet connection
   - Large 4K files may require significant processing time

4. **Performance**
   - Processing time increases with video length
   - High resolutions (4K) require more resources
   - Audio encoding is CPU-intensive

## Troubleshooting

### "Error: Unsupported URL"
```
Solution: Verify the URL is directly to a video page
❌ Wrong: https://www.youtube.com/watch?v=... (playlist page)
✓ Correct: https://www.youtube.com/watch?v=... (single video)
```

### "Download button is disabled"
```
Solution: Complete the analysis step first
1. Paste URL in input field
2. Click "Analyze" button
3. Wait for metadata to load
4. Then select quality and download
```

### "Download fails with network error"
```
Solutions:
1. Check internet connection
2. Verify URL is still valid
3. Try a different video to isolate issue
4. Clear browser cache and restart Colab session
```

### "File size is inaccurate"
```
Note: File sizes shown are estimates based on available metadata.
Actual file size may vary due to:
- Video codec efficiency
- Audio quality variation
- Container overhead
```

## API Reference

### Functions

#### `get_info(url)`
Extract video metadata and available formats.

**Parameters:**
- `url` (str): Video URL from supported platform

**Returns:**
- `tuple`: (info_dict, formats_list)
  - `info_dict`: Complete metadata from yt-dlp
  - `formats_list`: List of (display_name, format_id) tuples

**Raises:**
- `yt_dlp.utils.DownloadError`: Invalid or unsupported URL

**Example:**
```python
info, formats = get_info("https://www.youtube.com/watch?v=...")
print(info['title'])
print(formats[0])  # ('1080p (250 MB) • 60fps', 'format_id_123')
```

#### `format_number(n)`
Format large numbers using K/M notation.

**Parameters:**
- `n` (int): Number to format

**Returns:**
- `str`: Formatted number

**Example:**
```python
format_number(1500000)  # Returns '1.5M'
format_number(42000)    # Returns '42K'
format_number(100)      # Returns '100'
```

#### `format_date(date_str)`
Convert YouTube date format to readable string.

**Parameters:**
- `date_str` (str): Date in YYYYMMDD format

**Returns:**
- `str`: Formatted date or "N/A"

**Example:**
```python
format_date("20240115")  # Returns '15 Jan 2024'
format_date(None)        # Returns 'N/A'
```

## Contributing

We welcome contributions! Here's how to help:

### Code Style
- Follow PEP 8 guidelines
- Add docstrings to all functions
- Use type hints where applicable
- Comment complex logic sections

### Submitting Changes
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and test thoroughly
4. Submit a pull request with clear description

### Testing
```bash
# Test with various URLs
urls = [
    "https://www.youtube.com/watch?v=...",
    "https://vimeo.com/...",
    "https://www.dailymotion.com/..."
]

for url in urls:
    info, formats = get_info(url)
    assert info is not None
    assert len(formats) > 0
```

## Security Considerations

🔒 **Privacy & Safety**

- **Data Privacy**: No user data is collected or transmitted
- **URL Handling**: Only used locally for metadata extraction
- **Downloaded Files**: Stored only in your Google Drive
- **Third-Party APIs**: Only yt-dlp makes external requests (to video platforms)

## Performance Benchmarks

| Task | Time | Notes |
|------|------|-------|
| Metadata Extraction | 2-5s | Depends on network speed |
| 720p Download | 1-3 min | Typical video length |
| 1080p Download | 2-5 min | Includes encoding |
| 4K Download | 5-15 min | Requires significant processing |

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses
- **yt-dlp**: [Unlicense](https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE)
- **ipywidgets**: [BSD 3-Clause](https://github.com/jupyter-widgets/ipywidgets/blob/master/LICENSE)
- **IBM Plex Fonts**: [SIL Open Font License 1.1](https://github.com/IBM/plex/blob/main/LICENSE.txt)

## Roadmap

### Planned Features
- [ ] Batch download support
- [ ] Video format conversion (MP4, MKV, WebM)
- [ ] Audio extraction (MP3)
- [ ] Subtitle download
- [ ] Playlist support with selective downloads
- [ ] Download progress bar with speed estimation
- [ ] Cloud storage integration (Google Drive, Dropbox)
- [ ] Download history and favorites
- [ ] Custom output naming templates

### Version History
- **v1.0.0** (2024-01-15): Initial release
  - Multi-platform support
  - Metadata extraction
  - One-click download with audio merge

## FAQ

**Q: Is this tool legal?**
A: The tool itself is legal. Usage legality depends on the content's terms of service and copyright laws in your jurisdiction. Always respect creator rights.

**Q: Can I download entire playlists?**
A: Currently, single videos only. Playlist support is planned for v2.0.

**Q: What video formats are supported?**
A: MP4 is the default output. Support for MKV, WebM, and other formats is planned.

**Q: Can I run this offline?**
A: No, you need internet connection for metadata extraction and downloading.

**Q: Where are my files stored?**
A: Downloaded files are in Google Colab's `/content/downloads` directory and can be exported to your computer or Google Drive.

## Support

Need help? Here are your options:

1. **Check the Troubleshooting section** above
2. **Search existing GitHub issues**
3. **Create a new issue** with:
   - Error message (full traceback)
   - URL you were trying to download
   - Video platform name
   - Steps to reproduce

## Changelog

### v1.0.0 - Initial Release
- ✨ Multi-platform video support
- 📊 Real-time metadata extraction
- 🎯 Quality selection with file size estimation
- 💻 Professional responsive UI
- ⚡ One-click download with audio merging
- 🎨 IBM Carbon design system

## Credits

**Built with:**
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video downloader framework
- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) - Interactive UI
- [IBM Plex](https://github.com/IBM/plex) - Typography system

---

**Made with ❤️ for the open-source community**

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 🤝 Contributing improvements
- 📢 Sharing with others

**Last updated**: January 2024
