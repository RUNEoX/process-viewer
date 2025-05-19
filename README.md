📊 Process Viewer
Process Viewer is a lightweight, blazing-fast, and stealthy process monitoring tool for Windows. Built with a minimal modern GUI, it delivers real-time system insights and powerful process management without hogging your resources.

✨ Features
Modern Minimalist GUI
Smooth, clean interface with four dynamic themes: Dark, Light, Pink, Purple

Customizable Look & Feel
Easily tweak colors, fonts, and layout preferences to your liking

Real-Time Monitoring Dashboard
Track CPU Usage, RAM Usage, Thread Count, and Open File Descriptors (FDs) live
Adjustable refresh intervals for optimal performance
Switch between concise single-line summaries or detailed full views

Advanced Process Filtering & Sorting
Filter by Process Name, User, Port, Command-line Regex
Sort dynamically by any column in real-time

Process Tree View
Visualize parent-child relationships with an intuitive tree structure

Stealth Mode
Hide the tool’s own process from system listings to stay under the radar
Quiet startup option (-q flag) suppresses banners and logs

Powerful Process Controls
Change process priority and CPU affinity instantly
Suspend and resume processes seamlessly
Send signals like SIGTERM, SIGKILL, or custom ones

Scripting & Automation
Export process data as JSON or CSV 
Trigger user-defined scripts on custom watch conditions
Built-in network commands (netsh/ipconfig) for quick system tweaks


Alerts & Logging
Set CPU, memory, and I/O soft/hard thresholds
Get desktop notifications or console alerts on violations
Event log with rotation to keep history tidy

Plugin Architecture
Extend functionality by dropping plugins into the plugins/ folder
Auto-discovery keeps the core fast and clean

🛠️ Installation
Clone the repo:

git clone https://github.com/RUNEoX/process-viewer.git
cd process-viewer
Install dependencies:

pip install -r requirements.txt
🚀 Usage
Run the app:
python main.py

Start in stealth mode:
python -m process_viewer.main -q

Or just use the prebuilt executable on the releases page.
      
📜 License
 MIT License.
