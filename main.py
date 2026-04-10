# @title 🎬 Media Downloader Pro - Production Edition
"""
Media Downloader Pro - Production Edition
A professional video capture and metadata analysis tool for Google Colab.

Features:
- Multi-platform support (YouTube, Vimeo, and 1000+ video hosting sites)
- Real-time video metadata extraction
- Quality selection with file size estimation
- Professional UI with modern design system
- One-click video download with audio merging
- Responsive design for mobile and desktop

Requirements:
- yt-dlp >= 2024.1.0
- ipywidgets >= 7.6.0
- IPython
- Google Colab environment

Author: Your Name / Organization
License: MIT
Repository: https://github.com/yourusername/media-downloader-pro
"""

# ============================================================================
# DEPENDENCIES & IMPORTS
# ============================================================================

import yt_dlp
import os
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from google.colab import files
from datetime import datetime

print("✓ Media Downloader Pro initialized")

# ============================================================================
# CONFIGURATION
# ============================================================================

# Default download directory for processed videos
DOWNLOAD_DIR = "/content/downloads"

# Create downloads directory if it doesn't exist
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)
    print(f"✓ Created download directory: {DOWNLOAD_DIR}")

# ============================================================================
# DESIGN SYSTEM: Production Minimal
# ============================================================================
# 
# This design system implements IBM's Carbon Design principles:
# - Clean, minimal aesthetic
# - Clear visual hierarchy
# - Accessibility-first approach
# - Responsive layout for all device sizes
#

style_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #ffffff;
        color: #161616;
    }

    /* === MAIN CONTAINER === */
    .main-container {
        background: #ffffff;
        padding: 56px 48px;
        max-width: 960px;
        margin: 0 auto;
    }

    /* === HEADER SECTION === */
    .header-section {
        margin-bottom: 56px;
        border-bottom: 1px solid #e0e0e0;
        padding-bottom: 32px;
    }

    .logo-line {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 12px;
    }

    .logo-icon {
        font-size: 18px;
    }

    .logo-text {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #525252;
        display: inline-block;
    }

    .title {
        font-size: 36px;
        font-weight: 700;
        color: #161616;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 13px;
        color: #8d8d8d;
        letter-spacing: 0.5px;
        font-weight: 500;
    }

    /* === INPUT SECTION === */
    .input-section {
        display: flex;
        gap: 12px;
        margin-bottom: 40px;
    }

    .widget-text input {
        background: #f4f4f4 !important;
        color: #161616 !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 4px !important;
        padding: 11px 14px !important;
        font-size: 13px !important;
        font-family: 'IBM Plex Sans', sans-serif !important;
        transition: all 0.15s ease !important;
        flex: 1;
        font-weight: 400 !important;
    }

    .widget-text input::placeholder {
        color: #8d8d8d !important;
    }

    .widget-text input:focus {
        background: #ffffff !important;
        border-color: #161616 !important;
        outline: none !important;
        box-shadow: none !important;
    }

    /* === BUTTON STYLES === */
    .btn-base {
        font-family: 'IBM Plex Sans', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 4px !important;
        border: 1px solid #e0e0e0 !important;
        padding: 11px 20px !important;
        font-size: 12px !important;
        cursor: pointer;
        transition: all 0.15s ease !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        background: #f4f4f4 !important;
        color: #161616 !important;
        min-height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .btn-analyze {
        white-space: nowrap;
        min-width: 130px;
        border-color: #161616 !important;
        background: #ffffff !important;
    }

    .btn-analyze:hover {
        background: #161616 !important;
        color: #ffffff !important;
    }

    .btn-download {
        width: 100% !important;
        margin-top: 24px !important;
        background: #161616 !important;
        color: #ffffff !important;
        border: 1px solid #161616 !important;
        min-height: 42px;
    }

    .btn-download:hover:not(:disabled) {
        background: #383838 !important;
        border-color: #383838 !important;
    }

    .btn-download:disabled {
        opacity: 0.5 !important;
        cursor: not-allowed !important;
    }

    /* === VIDEO PREVIEW CARD === */
    .video-card {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        margin-bottom: 32px;
        overflow: hidden;
        transition: border-color 0.15s ease;
    }

    .video-card:hover {
        border-color: #a8a8a8;
    }

    .video-preview {
        position: relative;
        width: 100%;
        background: #f4f4f4;
        overflow: hidden;
    }

    .preview-img {
        width: 100%;
        height: 320px;
        object-fit: cover;
        display: block;
    }

    .preview-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.25) 100%);
        padding: 32px 24px 24px;
        color: #ffffff;
    }

    .video-title {
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 12px;
        line-height: 1.35;
    }

    .video-meta {
        font-size: 12px;
        color: #e0e0e0;
        display: flex;
        gap: 20px;
    }

    /* === INFO GRID === */
    .info-section {
        padding: 28px 24px;
        border-top: 1px solid #e0e0e0;
    }

    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 24px 32px;
    }

    .info-item {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .info-label {
        font-size: 11px;
        font-weight: 600;
        color: #525252;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .info-value {
        font-size: 14px;
        font-weight: 500;
        color: #161616;
        word-break: break-word;
    }

    .info-value.secondary {
        font-size: 13px;
        color: #8d8d8d;
        font-weight: 400;
    }

    /* === QUALITY SELECTION SECTION === */
    .quality-section {
        margin-bottom: 32px;
    }

    .section-label {
        font-size: 11px;
        font-weight: 700;
        color: #525252;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 12px;
        display: block;
    }

    .quality-group {
        background: #fafafa;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        overflow: hidden;
    }

    .widget-dropdown select {
        background: #fafafa !important;
        color: #161616 !important;
        border: none !important;
        border-radius: 0 !important;
        padding: 14px 14px 14px 14px !important;
        font-family: 'IBM Plex Sans', sans-serif !important;
        font-size: 13px !important;
        transition: all 0.15s ease !important;
        cursor: pointer;
        width: 100% !important;
        font-weight: 500 !important;
        appearance: none !important;
        min-height: 48px !important;
        line-height: 1.5 !important;
        background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e") !important;
        background-repeat: no-repeat !important;
        background-position: right 14px center !important;
        background-size: 20px !important;
        padding-right: 40px !important;
    }

    .widget-dropdown select:hover {
        background-color: #f0f0f0 !important;
    }

    .widget-dropdown select:focus {
        outline: none !important;
        background-color: #ffffff !important;
        border: 1px solid #161616 !important;
    }

    /* === STATUS MESSAGES === */
    .status-message {
        padding: 13px 16px;
        border-left: 4px solid #161616;
        margin-bottom: 20px;
        font-size: 13px;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 12px;
        background: #fafafa;
        border-radius: 2px;
    }

    .status-loading {
        border-left-color: #161616;
        color: #161616;
    }

    .status-success {
        border-left-color: #24a148;
        color: #24a148;
        background: #f1fbf8;
    }

    .status-error {
        border-left-color: #da1e28;
        color: #da1e28;
        background: #fff0f1;
    }

    /* === ANIMATIONS === */
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    .spinner {
        display: inline-block;
        width: 14px;
        height: 14px;
        border: 2px solid currentColor;
        border-top-color: transparent;
        border-radius: 50%;
        animation: spin 0.6s linear infinite;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .info-section {
        animation: fadeInUp 0.3s ease-out;
    }

    /* === RESPONSIVE DESIGN === */
    @media (max-width: 768px) {
        .main-container {
            padding: 32px 20px;
        }
        .title {
            font-size: 28px;
        }
        .input-section {
            flex-direction: column;
        }
        .btn-analyze {
            width: 100%;
            min-width: unset;
        }
        .preview-img {
            height: 220px;
        }
        .info-grid {
            grid-template-columns: 1fr;
            gap: 16px;
        }
    }
</style>
"""

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_info(url):
    """
    Extract video metadata and available quality options.
    
    Args:
        url (str): Video URL from supported platforms
        
    Returns:
        tuple: (info_dict, formats_list)
            - info_dict: Complete metadata dictionary
            - formats_list: List of tuples (display_name, format_id)
                           sorted by resolution (highest first)
    
    Raises:
        yt_dlp.utils.DownloadError: If URL is invalid or unsupported
    """
    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
        'no_warnings': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = []
        seen = set()
        
        # Iterate through available formats
        for f in info.get('formats', []):
            res = f.get('height')
            fps = f.get('fps')
            
            # Filter: only MP4 format with valid resolution
            if f.get('ext') == 'mp4' and res and res not in seen:
                size = (f.get('filesize') or f.get('filesize_approx') or 0) / (1024 * 1024)
                fps_str = f" • {int(fps)}fps" if fps else ""
                formats.append((f"{res}p ({size:.0f} MB){fps_str}", f['format_id']))
                seen.add(res)
        
        # Return top 8 qualities sorted by resolution (descending)
        return info, sorted(formats, key=lambda x: int(x[0].split('p')[0]), reverse=True)[:8]


def format_number(n):
    """
    Format large numbers using K (thousands) and M (millions) notation.
    
    Args:
        n (int): Number to format
        
    Returns:
        str: Formatted number (e.g., "1.5M", "523K", "42")
    
    Examples:
        >>> format_number(1500000)
        '1.5M'
        >>> format_number(42000)
        '42K'
    """
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.0f}K"
    return str(n)


def format_date(date_str):
    """
    Convert YouTube date format (YYYYMMDD) to human-readable format.
    
    Args:
        date_str (str): Date in YYYYMMDD format (e.g., "20240115")
        
    Returns:
        str: Formatted date (e.g., "15 Jan 2024") or "N/A" if invalid
    
    Examples:
        >>> format_date("20240115")
        '15 Jan 2024'
        >>> format_date(None)
        'N/A'
    """
    if not date_str:
        return "N/A"
    try:
        d = datetime.strptime(date_str, '%Y%m%d')
        return d.strftime('%d %b %Y')
    except (ValueError, TypeError):
        return date_str

# ============================================================================
# UI COMPONENTS
# ============================================================================

# Header section with branding and description
header = widgets.HTML(style_css + """
    <div class='header-section'>
        <div class='logo-line'>
            <span class='logo-icon'>▶</span>
            <span class='logo-text'>Media Downloader</span>
        </div>
        <h1 class='title'>Downloader Pro</h1>
        <p class='subtitle'>Professional Video Capture & Analysis Tool</p>
    </div>
""")

# URL input field
url_input = widgets.Text(
    placeholder='Paste video URL (YouTube, Vimeo, etc.)...',
    layout=widgets.Layout(width='78%')
)
url_input.add_class("widget-text")

# Analyze button to fetch metadata
analyze_btn = widgets.Button(
    description="Analyze",
    layout=widgets.Layout(width='20%')
)
analyze_btn.add_class("btn-base")
analyze_btn.add_class("btn-analyze")

# Output area for video info and messages
output_display = widgets.Output()

# Quality/format dropdown selector
format_dropdown = widgets.Dropdown(
    description='',
    options=[('Select quality...', None)],
    layout=widgets.Layout(width='100%')
)
format_dropdown.add_class("widget-dropdown")

# Download button
download_btn = widgets.Button(
    description="Download as MP4",
    layout=widgets.Layout(width='100%'),
    disabled=True
)
download_btn.add_class("btn-base")
download_btn.add_class("btn-download")

# ============================================================================
# STATE MANAGEMENT
# ============================================================================

# Global state dictionary to track current video
state = {
    'current_url': None,        # Currently analyzed URL
    'current_info': None        # Extracted metadata for current URL
}

# ============================================================================
# EVENT HANDLERS
# ============================================================================

def handle_analyze(_):
    """
    Handle 'Analyze' button click event.
    
    Performs the following:
    1. Validates URL input
    2. Extracts video metadata asynchronously
    3. Displays video preview card with metadata
    4. Populates quality dropdown
    5. Enables download button
    6. Handles errors gracefully with user feedback
    """
    if not url_input.value.strip():
        return
    
    state['current_url'] = url_input.value
    
    with output_display:
        clear_output()
        
        # Show loading spinner
        display(widgets.HTML(f"""
            <div class='status-message status-loading'>
                <span class='spinner'></span>
                <span>Analyzing video metadata...</span>
            </div>
        """))
        
        try:
            # Extract metadata
            info, formats = get_info(url_input.value)
            state['current_info'] = info
            clear_output()
            
            # === Format video duration ===
            duration = info.get('duration', 0)
            minutes, seconds = divmod(int(duration), 60)
            hours, minutes = divmod(minutes, 60)
            if hours > 0:
                duration_str = f"{hours}h {minutes}m {seconds}s"
            else:
                duration_str = f"{minutes}m {seconds}s"
            
            # === Extract metadata fields ===
            view_count = info.get('view_count', 0)
            like_count = info.get('like_count', 0)
            upload_date = format_date(info.get('upload_date', ''))
            uploader = info.get('uploader', 'N/A')
            
            # === Display video preview card ===
            display(widgets.HTML(f"""
                <div class='video-card'>
                    <div class='video-preview'>
                        <img src='{info['thumbnail']}' class='preview-img' alt='Preview'>
                        <div class='preview-overlay'>
                            <div class='video-title'>{info['title'][:90]}{'...' if len(info['title']) > 90 else ''}</div>
                            <div class='video-meta'>
                                <span>▶ {duration_str}</span>
                                <span>📊 Ready for download</span>
                            </div>
                        </div>
                    </div>
                    <div class='info-section'>
                        <div class='info-grid'>
                            <div class='info-item'>
                                <span class='info-label'>Channel</span>
                                <span class='info-value'>{uploader}</span>
                            </div>
                            <div class='info-item'>
                                <span class='info-label'>Duration</span>
                                <span class='info-value'>{duration_str}</span>
                            </div>
                            <div class='info-item'>
                                <span class='info-label'>Views</span>
                                <span class='info-value'>{format_number(view_count)}</span>
                            </div>
                            <div class='info-item'>
                                <span class='info-label'>Likes</span>
                                <span class='info-value'>{format_number(like_count) if like_count else 'N/A'}</span>
                            </div>
                            <div class='info-item'>
                                <span class='info-label'>Upload Date</span>
                                <span class='info-value secondary'>{upload_date}</span>
                            </div>
                            <div class='info-item'>
                                <span class='info-label'>Available Resolutions</span>
                                <span class='info-value'>{len(formats)} options</span>
                            </div>
                        </div>
                    </div>
                </div>
            """))
            
            # Update quality dropdown and enable download
            format_dropdown.options = formats
            download_btn.disabled = False
            
        except Exception as e:
            # Display error message
            display(widgets.HTML(f"""
                <div class='status-message status-error'>
                    <span>✕</span>
                    <span>Error: {str(e)[:120]}</span>
                </div>
            """))


def handle_download(_):
    """
    Handle 'Download as MP4' button click event.
    
    Performs the following:
    1. Validates state (URL, metadata, quality selection)
    2. Shows progress indicator
    3. Downloads video and audio streams
    4. Merges audio and video into single MP4 file
    5. Calculates file size
    6. Initiates browser download
    7. Displays success/error message
    
    Note: Audio merging is handled automatically by yt-dlp
    """
    if not state['current_url'] or not state['current_info'] or format_dropdown.value is None:
        return
    
    # Disable button and update label
    download_btn.disabled = True
    original_text = download_btn.description
    download_btn.description = "Downloading..."
    
    with output_display:
        try:
            # Show progress message
            display(widgets.HTML(f"""
                <div class='status-message status-loading'>
                    <span class='spinner'></span>
                    <span>Processing video (encoding + audio merge)...</span>
                </div>
            """))
            
            # === Configure download options ===
            opts = {
                'format': f"{format_dropdown.value}+bestaudio/best",  # Video + best audio
                'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
                'merge_output_format': 'mp4',
                'quiet': True,
                'no_warnings': True
            }
            
            # === Execute download and merge ===
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(state['current_url'], download=True)
                path = ydl.prepare_filename(info).rsplit('.', 1)[0] + ".mp4"
                filename = os.path.basename(path)
                file_size = os.path.getsize(path) / (1024 * 1024)
                
                # Show success message
                clear_output()
                display(widgets.HTML(f"""
                    <div class='status-message status-success'>
                        <span>✓</span>
                        <span><strong>{filename}</strong> ({file_size:.1f} MB) — Download complete</span>
                    </div>
                """))
                
                # Trigger browser download
                files.download(path)
                
        except Exception as e:
            # Display error message
            clear_output()
            display(widgets.HTML(f"""
                <div class='status-message status-error'>
                    <span>✕</span>
                    <span>Download error: {str(e)[:100]}</span>
                </div>
            """))
        finally:
            # Restore button state
            download_btn.disabled = False
            download_btn.description = original_text


# Attach event handlers
analyze_btn.on_click(handle_analyze)
download_btn.on_click(handle_download)

# ============================================================================
# UI ASSEMBLY
# ============================================================================

# Input section: URL field + Analyze button
input_box = widgets.HBox([url_input, analyze_btn])
input_box.add_class("input-section")

# Quality selection section
quality_section = widgets.VBox([
    widgets.HTML("<span class='section-label'>Video Quality</span>"),
    widgets.HTML("<div class='quality-group'>"),
    format_dropdown,
    widgets.HTML("</div>")
])
quality_section.add_class("quality-section")

# Control section: Quality selector + Download button
controls = widgets.VBox([
    quality_section,
    download_btn
])

# Main UI container
main_ui = widgets.VBox([
    header,
    input_box,
    output_display,
    controls
], layout=widgets.Layout(padding='0px'))
main_ui.add_class("main-container")

# === RENDER UI ===
display(main_ui)
print("✓ UI rendered successfully")
